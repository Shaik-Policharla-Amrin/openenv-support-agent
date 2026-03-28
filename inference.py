from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    text: str

@app.post("/run")
def run(request: Request):
    return {
        "response": f"Support reply: {request.text}"
    }

@app.post("/reset")
def reset():
    return {"status": "reset done"}