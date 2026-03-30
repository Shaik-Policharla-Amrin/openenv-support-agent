simport requests
import time

BASE_URL = "http://localhost:7860"

def safe_post(url, payload=None):
    for _ in range(3):
        try:
            return requests.post(url, json=payload, timeout=5).json()
        except:
            time.sleep(1)
    return {"error": "request failed"}

def run():
    print("Running inference...")

    print(safe_post(f"{BASE_URL}/reset"))

    tasks = ["hello", "Explain AI", "What is OpenEnv"]

    scores = []

    for t in tasks:
        res = safe_post(f"{BASE_URL}/step", {"task": t})
        print(res)

        if "observation" in res:
            scores.append(1.0)
        else:
            scores.append(0.0)

    print("Final Score:", sum(scores) / len(scores))

    print(requests.get(f"{BASE_URL}/state").json())

if __name__ == "__main__":
    run()