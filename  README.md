# 🎨 AI Text-to-Image Generator

A text-to-image generation web application built using ‪⁠entity⁠‬["software","PyTorch","machine learning framework"]‬, ‪⁠entity⁠‬["software","Hugging Face Diffusers","library for running diffusion models"]‬, and ‪⁠entity⁠‬["software","Gradio","Python UI library for ML apps"]‬.

The application uses Stable Diffusion to generate high-quality AI images from natural language prompts.

---

# 🚀 Features

* 🖼️ Text-to-image generation using Stable Diffusion v1.5
* ⚡ GPU acceleration support with CUDA
* 🎛️ Adjustable Guidance Scale
* 🔄 Adjustable Inference Steps
* 🔐 Hugging Face Token support using environment variables
* 🌐 Public sharing with Gradio
* ☁️ Google Colab deployment support

---

# 🧠 Tech Stack

* Python
* PyTorch
* Diffusers
* Transformers
* Gradio
* Stable Diffusion v1.5
* Google Colab GPU

---

# 📂 Project Structure

```bash
text-to-image-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── assets/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/text-to-image-ai.git
cd text-to-image-ai
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

This project uses a Hugging Face access token stored securely using environment variables.

Create a `.env` file in the root directory:

```env
HF_TOKEN=your_huggingface_token_here
```

---

# 🔑 Getting a Hugging Face Token

1. Create an account at:
   [https://huggingface.co](https://huggingface.co)

2. Go to:
   Settings → Access Tokens

3. Generate a new token

4. Paste it into your `.env` file

---

# ▶️ Running the Application

```bash
python app.py
```

If using Google Colab:

```python
# app.launch(share=True)
```

This generates a public Gradio link.

---

# 🎛️ Generation Controls

## Guidance Scale

The application includes configurable guidance scale support.

Guidance scale controls:

* Prompt adherence
* Creativity vs accuracy balance
* Image consistency

### Lower Guidance Scale

* More creative
* Less strict prompt following

### Higher Guidance Scale

* More accurate to prompt
* More constrained outputs

Example:

```python
guidance_scale=7.5
```

---

## Inference Steps

Inference steps determine how many refinement iterations the diffusion model performs during image generation.

### Lower Steps

* Faster generation
* Less detail

### Higher Steps

* Better image quality
* Slower generation

Example:

```python
num_inference_steps=50
```

---

# 🖼️ Example Prompt

```text
A futuristic cyberpunk city at sunset with neon lights and flying cars
```

---

# ⚡ GPU Support

This application supports GPU acceleration using CUDA.

The model automatically detects GPU availability:

```python
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
```

The Stable Diffusion pipeline is moved to GPU using:

```python
# pipe = pipe.to(device)
```

---

# ☁️ Google Colab Deployment

This project can be deployed and tested using free Google Colab GPUs.

Steps:

1. Open Google Colab
2. Enable GPU runtime
3. Upload project files
4. Run `app.py`
5. Use Gradio public share link

---

# 📦 requirements.txt

Example dependencies:

```txt
torch
diffusers
transformers
gradio
accelerate
safetensors
python-dotenv
```

---

# 📌 Notes

* Stable Diffusion models are large and may take time to download initially.
* Google Colab share links are temporary and expire when sessions disconnect.
* GPU performance depends on the allocated Colab hardware.

---

# 🔮 Future Improvements

* SDXL support
* Image upscaling
* Negative prompts
* Prompt history
* Seed control
* Model switching
* Image-to-image generation

---

# 👨‍💻 Author

Built as a Generative AI and Stable Diffusion experimentation project focused on:

* Deep Learning
* Diffusion Models
* GPU Inference
* AI Deployment
* Real-time Image Generation

---

# ⭐ Acknowledgements

* Stable Diffusion
* Hugging Face
* Gradio
* PyTorch
* Google Colab
