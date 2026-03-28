from env.models import Observation, Action, Reward
from env.tasks import TASKS
from env.graders import grade_response

class SupportEnv:
    def __init__(self, task_name="easy"):
        self.task = TASKS[task_name]
        self.history = []
        self.done = False

    def reset(self):
        self.history = []
        self.done = False
        return Observation(ticket=self.task["ticket"], history=[])

    def step(self, action: Action):
        if self.done:
            return None

        self.history.append(action.response)

        score = grade_response(action.response, self.task["expected_keywords"])

        reward = Reward(score=score)

        self.done = len(self.history) >= 2  # single step episode

        return Observation(
            ticket=self.task["ticket"],
            history=self.history
        ), reward, self.done, {}

    def state(self):
        return {
            "history": self.history,
            "done": self.done
        }