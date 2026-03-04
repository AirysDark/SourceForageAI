const OWNER = "AirysDark"
const REPO = "SourceForageAI"

let token = localStorage.getItem("sf_token")

if(!token){

    token = prompt("Enter GitHub Personal Access Token")

    if(token)
        localStorage.setItem("sf_token",token)

}


/* -------------------------
   Reset token
------------------------- */

function resetToken(){

    localStorage.removeItem("sf_token")

    location.reload()

}


/* -------------------------
   Trigger workflow
------------------------- */

async function runWorkflow(workflow){

    const targetRepo =
        document.getElementById("repo")?.value || ""

    const url =
    `https://api.github.com/repos/${OWNER}/${REPO}/actions/workflows/${workflow}/dispatches`

    const body = {

        ref:"main",

        inputs:{
            repository:targetRepo
        }

    }

    try{

        const res = await fetch(url,{

            method:"POST",

            headers:{
                "Authorization":"token "+token,
                "Accept":"application/vnd.github+json"
            },

            body:JSON.stringify(body)

        })

        if(res.status === 204){

            alert("Workflow started")

            loadRuns()
            loadStats()

        }
        else{

            const text = await res.text()

            console.error(text)

            alert("Failed to start workflow")

        }

    }

    catch(err){

        console.error(err)

        alert("Network error")

    }

}


/* -------------------------
   Load workflow runs
------------------------- */

async function loadRuns(){

    const url =
    `https://api.github.com/repos/${OWNER}/${REPO}/actions/runs`

    try{

        const res = await fetch(url,{

            headers:{
                "Authorization":"token "+token
            }

        })

        const data = await res.json()

        const container =
            document.getElementById("runs")

        if(!container) return

        container.innerHTML = ""

        data.workflow_runs
            .slice(0,10)
            .forEach(run=>{

                const div =
                    document.createElement("div")

                div.className = "queue-item"

                let statusClass = ""

                if(run.conclusion === "success")
                    statusClass = "success"

                if(run.conclusion === "failure")
                    statusClass = "error"

                if(run.status === "in_progress")
                    statusClass = "warning"

                div.innerHTML =
                `${run.name}
                 <span class="badge ${statusClass}">
                 ${run.status}
                 </span>`

                container.appendChild(div)

            })

    }

    catch(err){

        console.error("Run fetch error",err)

    }

}


/* -------------------------
   Load system stats
------------------------- */

async function loadStats(){

    const url =
    `https://api.github.com/repos/${OWNER}/${REPO}/actions/runs`

    try{

        const res = await fetch(url,{

            headers:{
                "Authorization":"token "+token

            }

        })

        const data = await res.json()

        let running = 0
        let queued = 0
        let failed = 0
        let success = 0

        data.workflow_runs.forEach(run=>{

            if(run.status === "in_progress")
                running++

            if(run.status === "queued")
                queued++

            if(run.conclusion === "failure")
                failed++

            if(run.conclusion === "success")
                success++

        })

        const total = success + failed

        const rate = total > 0
            ? Math.round((success / total) * 100)
            : 0


        document.getElementById("running").innerText = running
        document.getElementById("queued").innerText = queued
        document.getElementById("failed").innerText = failed
        document.getElementById("success").innerText = rate + "%"

    }

    catch(err){

        console.error("Stats fetch error",err)

    }

}


/* -------------------------
   Auto refresh
------------------------- */

function startRefresh(){

    loadRuns()
    loadStats()

    setInterval(()=>{

        loadRuns()
        loadStats()

    },10000)

}


/* -------------------------
   Start dashboard
------------------------- */

startRefresh()