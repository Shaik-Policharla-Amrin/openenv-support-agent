import gradio as gr

def reset():
    return {
        "ticket": "Customer: My order is delayed. Where is it?",
        "history": []
    }

demo = gr.Interface(
    fn=reset,
    inputs=[],
    outputs="json",
    title="OpenEnv Support Agent"
)

demo.launch(server_name="0.0.0.0", server_port=7860)