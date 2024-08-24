import gradio as gr
import time
from typing import Generator


def yield_message_succeeds(message):
    final_message = ""
    for char in message:
        time.sleep(0.2)
        final_message += char
        yield final_message


def yield_message_fails(message: str) -> Generator[str, None, None]:
    final_mesage = ""
    for char in message:
        time.sleep(1)
        final_mesage += char
        yield final_mesage


with gr.Blocks() as demo:
    message = gr.Textbox(label="Message", value="This is a yield test!")
    output = gr.Textbox(label="Output")
    output_failed = gr.Textbox(label="Output Failed")
    with gr.Row():
        btn_succeeds = gr.Button(value="Succeeds")
        btn_fails = gr.Button(value="Fails")
    btn_succeeds.click(fn=yield_message_succeeds, inputs=[message], outputs=[output])
    btn_fails.click(fn=yield_message_fails, inputs=[message], outputs=[output_failed])
