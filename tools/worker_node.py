from tools.ai_memory.brain_api import load, save

data, sha = load("brain/network/workers.json")

data["workers"].append("worker-01")

save("brain/network/workers.json", data, sha)