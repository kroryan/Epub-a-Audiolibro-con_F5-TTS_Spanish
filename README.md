# Easy eBook to Audiobook Converter with F5-TTS

![image](https://github.com/user-attachments/assets/c2f134f7-7060-4cc5-8e59-177a3d681844)


Turn your eBooks into audiobooks using the F5-TTS text-to-speech model. This application allows you to upload an eBook file and a reference voice sample to generate a personalized audiobook. The app supports various eBook formats and provides advanced settings to customize the output.

HuggingFace Demo (extremely slow on free CPU tier, would recommend running locally with Docker, see below): https://huggingface.co/spaces/jdana/eBook_to_Audiobook_with_F5-TTS

## Features

- **Voice Customization**: Upload a voice sample (<15 seconds) to mimic in the generated audiobook.
- **Multiple eBook Formats**: Supports `.epub`, `.mobi`, `.pdf`, `.txt`, and `.html` files.
- **Batch Processing**: Upload multiple eBooks for batch conversion.
- **Advanced Settings**:
  - Reference text input for more accurate voice cloning.
  - Adjust speech speed.
  - Customize cross-fade duration between audio chunks.
- **Metadata Handling**: Extracts and embeds eBook metadata and cover images into the audiobook files.
- **Output Formats**: Generates audiobooks with book covers embedded in `.mp3` format. (`.m4b` format caused play/pause issues in some audiobook players.)
- **User-Friendly Interface**: Built with Gradio for an interactive web UI.

## Installation

# How to Run the Offline F5 TTS Docker Application

These instructions will guide you through loading and running the pre-packaged offline Text-to-Speech (TTS) Docker image. This image includes all necessary models, so it does not require an internet connection after setup.

## Prerequisites

Before you begin, ensure you have the following installed and configured on your system:

1.  **Docker Desktop:** Install Docker for your operating system (Windows, macOS, or Linux). You can find it here: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2.  **NVIDIA GPU Drivers:** You need an NVIDIA graphics card (GPU) and the appropriate drivers installed. Check the NVIDIA website for the latest drivers for your specific GPU.
3.  **NVIDIA Container Toolkit:** This allows Docker to access your NVIDIA GPU. Installation instructions depend on your OS (primarily Linux, or WSL2 on Windows). Follow the official guide: [https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

*(Note: Running this application requires a compatible NVIDIA GPU properly configured for Docker.)*

# Instructions

1.  **Download the Offline Docker Image:**
    * Download the required Docker image archive (`.tar` file) from Hugging Face Hub:
        **[Download f5tts_offline_ebook_to_audiobook_image.tar (5.8 GB)](https://huggingface.co/jdana/f5tts_offline_ebook_to_audiobook_Docker_image/resolve/main/f5tts_offline_ebook_to_audiobook_image.tar)**
    * Save this file to a known location on your computer.

2.  **Open a Terminal or Command Prompt:**
    * (Same instructions as before...)

3.  **Navigate to the File Location (Optional but Recommended):**
    * (Same instructions as before...)

4.  **Load the Docker Image:**
    * Run the `docker load` command:
        ```bash
        docker load -i f5tts_offline_ebook_to_audiobook_image.tar
        ```

5.  **Run the Application Container:**
    * Run the `docker run` command using the loaded image tag (`f5tts:offline`):
        ```bash
        docker run --rm -it --gpus all -p 7860:7860 f5tts:offline
        ```
    * **Explanation of options:**
        * `--rm`: Automatically removes the container when you stop it (keeps things clean).
        * `-it`: Runs the container interactively so you can see its logs in the terminal.
        * `--gpus all`: Gives the container access to all your available NVIDIA GPUs.
        * `-p 7860:7860`: Maps port `7860` from your computer to port `7860` inside the container, allowing you to access the web UI.
        * `f5tts:offline`: The name of the Docker image to run.
    * You should see log messages in your terminal, indicating the application is starting. Look for a line similar to `* Running on local URL: http://0.0.0.0:7860`.

## Accessing the Application

* Once the container is running and you see the confirmation message in the terminal, open your web browser (like Chrome, Firefox, Edge).
* Navigate to the following address:
    **`http://localhost:7860`**
* You should now see the web interface for the TTS application.

## Stopping the Application

* To stop the application container, go back to the terminal window where it is running.
* Press `Ctrl + C` (hold the Control key and press C).
* The container will stop, and because we used the `--rm` flag, it will also be automatically removed.
If you donwnload the repository into a folder:

1. Double click Build.bat, wait for it to finish
2. Double click Run.bat to launch


## License:
- GPL-3.0

## Acknowledgments

- This project uses code adapted from [fakerybakery](https://github.com/fakerybakery)'s Hugging Face space [E2-F5-TTS](https://huggingface.co/spaces/mrfakename/E2-F5-TTS) and [DrewThomasson](https://github.com/DrewThomasson)'s Hugging Face space [ebook2audiobook](https://huggingface.co/spaces/drewThomasson/ebook2audiobook). Thanks for your amazing work!

