from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "openenv agent running"}

@app.get("/reset")
def reset():
    return {
        "ticket": "Customer: My order is delayed. Where is it?",
        "history": []
    }