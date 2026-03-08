import os
import requests
import time

# Brain connection settings
BRAIN_URL = os.getenv("BRAIN_URL", "http://localhost:8080")
BRAIN_TOKEN = os.getenv("BRAIN_TOKEN", "MASTER_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {BRAIN_TOKEN}",
    "Content-Type": "application/json"
}


def store_failure(build_type, log):

    payload = {
        "time": int(time.time()),
        "type": build_type,
        "log": log[-2000:]
    }

    requests.post(
        f"{BRAIN_URL}/memory/failure",
        json=payload,
        headers=HEADERS
    )


def store_fix(patch):

    payload = {
        "patch": patch,
        "time": int(time.time())
    }

    requests.post(
        f"{BRAIN_URL}/memory/fix",
        json=payload,
        headers=HEADERS
    )


def search_memory(log):

    payload = {
        "log": log[:2000]
    }

    r = requests.post(
        f"{BRAIN_URL}/memory/search",
        json=payload,
        headers=HEADERS
    )

    if r.status_code != 200:
        return None

    data = r.json()

    return data.get("patch")
