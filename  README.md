Here is the updated `README.md` reflecting that the Hugging Face token is managed via a `.txt` file instead of the conventional `.env` file approach.

---

# 🎨 AI Text-to-Image Generator

A text-to-image generation web application built using PyTorch, Hugging Face Diffusers, and Gradio.

The application uses Stable Diffusion to generate high-quality AI images from natural language prompts.

---

# 🚀 Features

* 🖼️ Text-to-image generation using Stable Diffusion v1.5
* ⚡ GPU acceleration support with CUDA
* 🎛️ Adjustable Guidance Scale
* 🔄 Adjustable Inference Steps
* 🔑 Hugging Face Token authentication via localized text file loading
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
Gen_AI_Text_To_Image/
│
├── .gradio/
│   └── certificate.pem
│
├── .idea/
│   ├── inspectionProfiles/
│   │   └── profiles_settings.xml
│   ├── .gitignore
│   ├── Gen_AI_Text_To_Image.iml
│   ├── misc.xml
│   ├── modules.xml
│   └── vcs.xml
│
├── README.md
├── .gitignore
├── app.py
├── python_installer.exe
└── requirements.txt

```

---

# 🖼️ Application Screenshot

Here is a preview of the project structure inside the development environment:

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

# 🔐 Token Authentication

Instead of the conventional `.env` setup, this implementation reads the Hugging Face access token directly from a local text file within `app.py`.

### 1. Generate Your Token

* Create an account or log in to [https://huggingface.co](https://huggingface.co).
* Navigate to **Settings** → **Access Tokens** and generate a new token.

### 2. Configure the File

Create a file named `token.txt` (or your preferred text filename) in the root directory and paste your token inside it:

```text
hf_your_actual_token_here

```

### 3. Loading in app.py

The token is loaded and passed to the pipeline using standard Python file I/O operations:

```python
# Loading the token within app.py
with open("token.txt", "r") as f:
    hf_token = f.read().strip()

# Example usage with the pipeline
# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", use_auth_token=hf_token)

```

> ⚠️ **Important:** Remember to add `token.txt` to your `.gitignore` file to ensure your private credentials are never pushed to public repositories.

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
Generate a futuristic african city at sunset

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

## 🔗 Live Demo

[https://85d7672a8e379eead9.gradio.live/](https://85d7672a8e379eead9.gradio.live/)

---

# ⭐ Acknowledgements

* Stable Diffusion
* Hugging Face
* Gradio
* PyTorch
* Google Colab