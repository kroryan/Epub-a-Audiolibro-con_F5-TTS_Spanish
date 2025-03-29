# Easy eBook to Audiobook Converter with F5-TTS

![image](https://github.com/user-attachments/assets/c2f134f7-7060-4cc5-8e59-177a3d681844)

Turn your eBooks into audiobooks using the F5-TTS text-to-speech model. This application allows you to upload an eBook file and a reference voice sample to generate a personalized audiobook. The app supports various eBook formats and provides advanced settings to customize the output.

HuggingFace Demo (extremely slow on free CPU tier, would recommend running locally with Docker, see below): https://huggingface.co/spaces/jdana/eBook_to_Audiobook_with_F5-TTS

## Features

- **Voice Customization**: Upload a voice sample (<15 seconds) to mimic in the generated audiobook.
- Requires 5GB of Vram
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
    * Copy the entire command, paste it into your terminal, and press Enter.
    * **Command:**
        ```bash
        curl -L "[https://huggingface.co/jdana/f5tts_offline_ebook_to_audiobook_Docker_image/resolve/main/f5tts_offline_ebook_to_audiobook_image.tar](https://huggingface.co/jdana/f5tts_offline_ebook_to_audiobook_Docker_image/resolve/main/f5tts_offline_ebook_to_audiobook_image.tar)" -o f5tts_offline_ebook_to_audiobook_image.tar && docker load < f5tts_offline_ebook_to_audiobook_image.tar && docker run --rm -it --gpus all -p 7860:7860 f5tts:latest && del f5tts_offline_ebook_to_audiobook_image.tar
        ```
        *(Note: On Linux/macOS, change the final `del` command to `rm`)*
    * **How it works:**
        * `curl -L "URL" -o filename.tar`: Downloads the file completely and saves it locally. `-L` follows redirects, `-o` specifies the output filename.
        * `&&`: Ensures the next command runs *only if* the previous one was successful.
        * `docker load < filename.tar`: Loads the image into Docker from the downloaded file.
        * `&&`: Ensures the `docker run` command starts *only if* the load was successful.
        * `docker run ...`: Runs the container using the `f5tts:latest` image. The `--rm` flag ensures the container is removed when stopped. `-it` runs it interactively. `--gpus all` provides GPU access. `-p 7860:7860` maps the port.
        * `&&`: Ensures the cleanup command runs *only if* `docker run` exits successfully (i.e., after you stop the container, typically with `Ctrl+C`).
        * `del filename.tar` (or `rm filename.tar` on Linux/macOS): Deletes the downloaded `.tar` file to save space.
    * **Be Patient:** This command still downloads a large file (5.8 GB), which will take time based on your internet speed. You will see download progress from `curl`. The subsequent `docker load` process also takes time. Wait for the command to complete the download and load steps before the application logs start appearing.

## Accessing the Application

* Once the container is running (you should eventually see log messages in the terminal, including something like `* Running on local URL: http://0.0.0.0:7860`), open your web browser.
* Navigate to the following address:
    **`http://localhost:7860`**
* You should now see the web interface for the TTS application.

## Stopping the Application

* To stop the application container, go back to the terminal window where it is running.
* Press `Ctrl + C` (hold the Control key and press C).
* The container will stop. Because the run command included the `--rm` flag, it will also be automatically removed. The final part of the single command (`del` or `rm`) should then execute to clean up the downloaded `.tar` file.

## License:

-   GPL-3.0

## Acknowledgments

-   This project uses code adapted from [fakerybakery](https://github.com/fakerybakery)'s Hugging Face space [E2-F5-TTS](https://huggingface.co/spaces/mrfakename/E2-F5-TTS) and [DrewThomasson](https://github.com/DrewThomasson)'s Hugging Face space [ebook2audiobook](https://huggingface.co/spaces/drewThomasson/ebook2audiobook). Thanks for your amazing work!
