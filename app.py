import os
import torch
import gradio as gr
from diffusers import StableDiffusionPipeline


# Read Hugging Face token from text file
with open("HG_Token.txt", "r") as f:
    HF_TOKEN = f.read().strip()


MODEL_ID = "runwayml/stable-diffusion-v1-5"

# Select device
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

print(f"Loading model on {DEVICE}...")

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    token=HF_TOKEN,
    torch_dtype=DTYPE
)

pipe.to(DEVICE)
pipe.enable_attention_slicing()


def generate_image(prompt, negative_prompt="", guidance_scale=7.5, num_inference_steps=50):
    if not prompt.strip():
        raise gr.Error("Please enter a prompt.")

    image = pipe(prompt, negative_prompt=negative_prompt, guidance_scale=guidance_scale,
                 num_inference_steps=num_inference_steps).images[0]  # Generate image with new parameters
    return image  # Return generated image


app = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="Enter Image Description (Prompt)"),
        gr.Textbox(label="Enter things to exclude (Negative Prompt)", value="blurred, out of focus, noisy, low quality"),
        gr.Slider(minimum=0, maximum=20, value=7.5, step=0.5, label="Guidance Scale"),
        gr.Slider(minimum=10, maximum=150, value=50, step=10, label="Inference Steps")
    ],
    outputs=gr.Image(type="pil", label="Generated Image"),
    title="AI Text-to-Image Generator",
    description="Type a description and generate an image using Stable Diffusion."
)


if __name__ == "__main__":
    app.launch(share= True, server_name="0.0.0.0", server_port=8080)

