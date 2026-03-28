import gradio as gr
import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def support_agent(query):
    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent."},
            {"role": "user", "content": query}
        ],
        "max_tokens": 200
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    return data["choices"][0]["message"]["content"]

demo = gr.Interface(
    fn=support_agent,
    inputs=gr.Textbox(label="Customer Query"),
    outputs="text",
    title="AI Customer Support Agent"
)

demo.launch(server_name="0.0.0.0", server_port=7860)