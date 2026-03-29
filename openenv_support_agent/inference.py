import requests

BASE_URL = "http://127.0.0.1:8000"

def run():
    requests.post(f"{BASE_URL}/reset")

    response = requests.post(
        f"{BASE_URL}/step",
        json={"message": "My order is delayed"}
    )

    print(response.json())

if __name__ == "__main__":
    run()