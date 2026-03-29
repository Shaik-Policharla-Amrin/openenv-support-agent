import requests
import os

BASE_URL = os.getenv("API_BASE_URL")

def run():
    print("Running inference...")

    # RESET
    r = requests.post(f"{BASE_URL}/reset")
    print("Reset:", r.json())

    # TASKS (3 REQUIRED)
    tasks = ["Say hello", "Explain AI", "What is OpenEnv?"]

    for t in tasks:
        r = requests.post(f"{BASE_URL}/step", json={"task": t})
        print("Step:", r.json())

    # STATE
    r = requests.get(f"{BASE_URL}/state")
    print("State:", r.json())

if __name__ == "__main__":
    run()