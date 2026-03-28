from fastapi import FastAPI
from env.environment import SupportEnv
from env.models import Action

app = FastAPI()

env = SupportEnv()

@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, _ = env.step(act)
    
    return {
        "observation": obs.dict(),
        "reward": reward.score,
        "done": done
    }

@app.get("/state")
def state():
    return env.state()