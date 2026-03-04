import subprocess
import shutil


def call_local_model(prompt, model="deepseek-coder", timeout=300):

    """
    Call a local Ollama model and return the response text.
    """

    if not prompt:
        return ""

    # verify ollama exists
    if not shutil.which("ollama"):
        print("Ollama not found in PATH")
        return ""

    try:

        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if proc.returncode != 0:

            print("Local model error:")
            print(proc.stderr)

            return ""

        return proc.stdout.strip()

    except subprocess.TimeoutExpired:

        print("Local model timeout")

        return ""

    except Exception as e:

        print("Local model failed:", e)

        return ""