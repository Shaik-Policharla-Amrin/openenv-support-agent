from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# STATE
state_data = {"step": 0}

# INPUT MODEL
class StepInput(BaseModel):
    task: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    state_data["step"] = 0
    return {"state": state_data}

@app.post("/step")
def step(data: StepInput):
    state_data["step"] += 1

    return {
        "observation": f"Processed: {data.task}",
        "reward": 1.0,
        "done": state_data["step"] >= 1,
        "info": {},
        "state": state_data
    }

@app.get("/state")
def get_state():
    return state_data