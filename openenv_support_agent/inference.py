import requests

BASE_URL = "http://localhost:7860"

def run():
    print("Running inference...")

    print(requests.post(f"{BASE_URL}/reset").json())

    tasks = ["hello", "Explain AI", "What is OpenEnv"]

    for t in tasks:
        res = requests.post(f"{BASE_URL}/step", json={"task": t})
        print(res.json())

    print(requests.get(f"{BASE_URL}/state").json())

if __name__ == "__main__":
    run()