from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    ticket: str
    history: List[str]

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float
    reason: Optional[str] = None