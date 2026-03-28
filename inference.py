import os
from openai import OpenAI
from env.environment import SupportEnv
from env.models import Action

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN")
)

MODEL_NAME = os.getenv("MODEL_NAME")

def run_task(task_name):
    env = SupportEnv(task_name)
    obs = env.reset()

    prompt = f"""
    You are a customer support agent.
    Ticket: {obs.ticket}
    Respond professionally.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=150
    )

    reply = response.choices[0].message.content

    obs, reward, done, _ = env.step(Action(response=reply))

    print(f"{task_name} score:", reward.score)
    return reward.score


if __name__ == "__main__":
    scores = []
    for t in ["easy", "medium", "hard"]:
        scores.append(run_task(t))

    print("Final Score:", sum(scores)/3)