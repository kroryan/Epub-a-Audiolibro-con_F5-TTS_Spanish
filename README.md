# eBook a Audiolibro con F5-TTS (Español)

Este repositorio convierte eBooks en audiolibros usando el modelo F5-TTS afinado para español.

Este fork incluye ajustes y correcciones para usar el modelo español de `jpgallegoar/F5-Spanish` y soluciónes específicas para entornos Windows con GPU NVIDIA (por ejemplo, RTX 5060 Ti).

Resumen rápido
- Modelo: jpgallegoar/F5-Spanish (model_1200000.safetensors usado por defecto aquí)
- Vocabulario: `spanish_vocab.txt` (vocab del modelo)
- Interfaz: Gradio (app.py)

Cambios importantes en este fork
- Desactivada la conversión automática de texto a pinyin en `f5_tts_working_code/infer/utils_infer.py` para que el sistema funcione correctamente con texto en español.
- Añadida lógica para forzar el uso de `spanish_vocab.txt` si está presente en la raíz del proyecto.
- Parámetros del modelo ajustados en `app.py` para coincidir con la arquitectura del modelo español (dim=1024, depth=22, heads=16, ff_mult=2, text_dim=512, conv_layers=4).

Licencia y creditos
- Basado en el proyecto original F5-TTS de SWivid y el modelo finetuneado de jpgallegoar.
# Easy eBook to Audiobook Converter with F5-TTS

![image](https://github.com/user-attachments/assets/d286b6e4-7a73-4e9d-88af-dc910652d743)


Turn your eBooks into audiobooks using the F5-TTS text-to-speech model. This application allows you to upload an eBook file and a reference voice sample to generate a personalized audiobook. The app supports various eBook formats and provides advanced settings to customize the output.

Copy and paste this single command line into command prompt to get the app running locally in Docker (Nvidia card accelerated)(11GB)(can take a long time to load, check CPU usage once download is finished, if CPU usage is high, it is loading correctly):

```bash
curl -L "https://huggingface.co/jdana/f5tts_offline_ebook_to_audiobook_Docker_image/resolve/main/f5tts-app-preloaded_2025-05-29.tar" -o f5tts-app-preloaded_2025-05-29.tar && docker load < f5tts-app-preloaded_2025-05-29.tar && docker tag 21fad7b5127e f5tts:latest && docker run --rm -it --gpus all -p 7860:7860 f5tts:latest && del f5tts-app-preloaded_2025-05-29.tar

```

## Features

- **Voice Customization**: Upload a voice sample (<15 seconds) to mimic in the generated audiobook.
- Requires 5GB of Vram
- **Estimated Remaining Time**: See how much time is left to finish each ebook, calculated automatically
- **Multiple eBook Formats**: Supports `.epub`, `.mobi`, `.pdf`, `.txt`, and `.html` files.
- **Batch Processing**: Upload multiple eBooks for batch conversion.
- **Advanced Settings**:
  - Reference text input for more accurate voice cloning.
  - Adjust speech speed.
  - Customize cross-fade duration between audio chunks.
- **Metadata Handling**: Extracts and embeds eBook metadata and cover images into the audiobook files.
- **Output Formats**: Generates audiobooks with book covers embedded in `.mp3` format. (`.m4b` format caused play/pause issues in some audiobook players.)
- **User-Friendly Interface**: Built with Gradio for an interactive web UI.

# How to Run the Offline F5 TTS Docker Application

These instructions will guide you through running the pre-packaged offline Text-to-Speech (TTS) Docker image using a single command. This image includes all necessary models, so it does not require an internet connection *after* the initial download step.

## Prerequisites

Before you begin, ensure you have the following installed and configured on your system:

1.  **Docker Desktop:** Install Docker for your operating system (Windows, macOS, or Linux). You can find it here: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2.  **NVIDIA GPU Drivers:** You need a compatible NVIDIA graphics card (GPU). Install the latest drivers from the NVIDIA website.
3.  **NVIDIA Container Toolkit:** This allows Docker to access your NVIDIA GPU. Installation instructions depend on your OS (primarily Linux, or WSL2 on Windows). Follow the official guide: [https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
4.  **Sufficient VRAM:** Ensure your NVIDIA GPU has at least **5 GB of Video RAM (VRAM)** available for the application to run smoothly.
5.  **`curl` Command-Line Tool:** This tool is used within the single command to download the image. It's pre-installed on most Linux and macOS systems, and usually included in modern Windows 10/11. You can verify it's available by opening your terminal/command prompt and typing `curl --version`.

*(Note: Running this application requires a compatible NVIDIA GPU meeting the VRAM requirement, properly configured for Docker with the NVIDIA Container Toolkit.)*

## Instructions

1.  **Open a Terminal or Command Prompt:**
    * **Windows:** Open Command Prompt, PowerShell, or the terminal in Windows Subsystem for Linux (WSL).
    * **macOS:** Open the Terminal application (found in Applications > Utilities).
    * **Linux:** Open your preferred terminal application.

2.  **Download, Load, and Run (Single Command):**
    * The single command below performs all the necessary steps sequentially: downloads the Docker image (~5.8 GB) from Hugging Face saving it temporarily, loads it into your Docker engine, starts the application container, and finally cleans up the downloaded file *after* you stop the container.
    * This method is more robust against download interruptions than piping the download directly.
    # eBook a Audiolibro con F5-TTS (Español)

    Convierte eBooks en audiolibros usando el modelo F5-TTS afinado para español.

    Este fork está pensado para entornos Windows con GPU NVIDIA (por ejemplo, RTX 5060 Ti) y contiene correcciones para asegurar una síntesis coherente en español.

    Resumen rápido
    - Modelo por defecto: `jpgallegoar/F5-Spanish` (se recomienda `model_1200000.safetensors` en este repositorio)
    - Vocabulario: `spanish_vocab.txt` (vocab del modelo)
    - Interfaz: Gradio (archivo `app.py`)

    Cambios importantes en este fork
    - Se desactivó la conversión automática de caracteres a pinyin en `f5_tts_working_code/infer/utils_infer.py` para evitar que el texto español se convierta a pinyin chino.
    - Se añadió detección automática y uso de `spanish_vocab.txt` en la raíz del proyecto si existe.
    - Se ajustaron y forzaron los parámetros del modelo en `app.py` para coincidir con la arquitectura del modelo español (dim=1024, depth=22, heads=16, ff_mult=2, text_dim=512, conv_layers=4).

    Requisitos mínimos
    - Python 3.11
    - GPU NVIDIA con drivers compatibles (se probó en RTX 5060 Ti con CUDA 12.8)
    - ffmpeg en PATH

    Instalación rápida (PowerShell)

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    pip install python-magic-bin       # Windows: si falla python-magic
    pip install torchcodec             # Opcional, si hay problemas con torchaudio/TorchCodec
    ```

    Instalar PyTorch (ejemplo para CUDA 12.8)

    ```powershell
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
    ```

    Descargar modelo y vocabulario
    - Descarga `model_1200000.safetensors` desde `jpgallegoar/F5-Spanish` y ponlo en la caché de Hugging Face o en la ruta mostrada por `app.py` al arrancar.
    - Descarga `vocab.txt` desde el mismo repositorio y guárdalo como `spanish_vocab.txt` en la raíz del proyecto.

    Ejecutar la aplicación

    ```powershell
    $env:GRADIO_SERVER_PORT="7861"; python app.py
    ```

    Abre en el navegador: `http://localhost:7861`.

    Uso recomendado
    - Sube una muestra de voz en español (<=15s) con buena calidad.
    - Proporciona la transcripción en español (esto mejora la clonación de voz).

    Créditos
    - Fork basado en el proyecto original F5-TTS (SWivid).
    - Modelo finetuneado para español por `jpgallegoar` (jpgallegoar/F5-Spanish).
    - Este fork por `kroryan` contiene ajustes y documentación en español.

    Licencia
    - Respeta las licencias de los proyectos originales y del modelo (revisa la página del modelo en Hugging Face para detalles).

    Agradecimientos
    - Gracias a SWivid por el proyecto base F5-TTS y a jpgallegoar por el modelo español. También se hace referencia a los espacios de Hugging Face que inspiraron la interfaz original.
