import requests
import time
import subprocess

BASE_URL = "http://localhost:7860"

def start_server():
    subprocess.Popen(
        ["python3", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # wait until server responds
    for _ in range(10):
        try:
            requests.get(BASE_URL, timeout=1)
            return
        except:
            time.sleep(0.5)

def safe_post(url, payload=None):
    for _ in range(3):
        try:
            res = requests.post(url, json=payload, timeout=3)
            return res.json() if res.content else {}
        except:
            time.sleep(0.5)
    return {}
def run():
    task_name = "openenv_tasks"

    print(f"[START] task={task_name}", flush=True)

    safe_post(f"{BASE_URL}/reset")

    tasks = ["hello", "Explain AI", "What is OpenEnv"]
    scores = []

    for i, t in enumerate(tasks, start=1):
        res = safe_post(f"{BASE_URL}/step", {"task": t})

        reward = 1.0 if "observation" in res else 0.0
        scores.append(reward)

        print(f"[STEP] step={i} reward={reward}", flush=True)

    final_score = sum(scores) / len(scores)

    print(f"[END] task={task_name} score={final_score} steps={len(tasks)}", flush=True)
    
if __name__ == "__main__":
    run()
