from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

# ===== ENV VARIABLES =====
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# ===== STATE =====
current_step = 0

# ===== MODELS =====
class StepInput(BaseModel):
    task: str

# ===== ROUTES =====

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    global current_step
    current_step = 0
    return {"message": "environment reset"}

@app.post("/step")
def step(data: StepInput):
    global current_step

    # Call LLM (MANDATORY as per rules)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful AI agent."},
            {"role": "user", "content": data.task}
        ]
    )

    output = response.choices[0].message.content

    current_step += 1

    return {
        "observation": output,
        "reward": 1.0,
        "done": current_step >= 1,
        "info": {}
    }

@app.get("/state")
def state():
    return {
        "step": current_step
    }