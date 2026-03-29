from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

# ENV
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# STATE
state_data = {"step": 0}

# INPUT MODEL
class StepInput(BaseModel):
    task: str

# ROOT
@app.get("/")
def home():
    return {"status": "ok"}

# RESET
@app.post("/reset")
def reset():
    state_data["step"] = 0
    return {"state": state_data}

# STEP
@app.post("/step")
def step(data: StepInput):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": data.task}
            ]
        )

        output = response.choices[0].message.content

        state_data["step"] += 1

        return {
            "observation": output,
            "reward": 1.0,
            "done": state_data["step"] >= 1,
            "info": {},
            "state": state_data   # 🔥 VERY IMPORTANT
        }

    except Exception as e:
        return {
            "observation": str(e),
            "reward": 0.0,
            "done": True,
            "info": {"error": str(e)},
            "state": state_data
        }

# STATE
@app.get("/state")
def get_state():
    return state_data