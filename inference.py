from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/run")
def run(data: Input):
    return {"response": f"Support reply: {data.text}"}

@app.post("/reset")
def reset():
    return {"status": "ok"}