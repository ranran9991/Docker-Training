import gradio as gr

# Simple Gradio interface for text reversal
def reverse_text(text):
    return text[::-1]

interface = gr.Interface(
    fn=reverse_text,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Textbox(label="Reversed text")
)
interface.launch(server_name="0.0.0.0", server_port=8501)