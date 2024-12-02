# eBook to Audiobook Converter with F5-TTS

![image](https://github.com/user-attachments/assets/0075b81c-8a51-4cc6-b9ff-2cda45ea187a)


Turn your eBooks into audiobooks using the F5-TTS text-to-speech model. This application allows you to upload an eBook file and a reference voice sample to generate a personalized audiobook. The app supports various eBook formats and provides advanced settings to customize the output.

HuggingFace Demo (extremely slow on free CPU tier, would reccomend running locally with Docker, see below): https://huggingface.co/spaces/jdana/eBook_to_Audiobook_with_F5-TTS

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

CUDA GPU Recomended 

## Docker

1. Install Docker

2. Run the following single command in Command Prompt to build and start the application, once running, view the UI by going to http://localhost:7860/

```bash
docker build -t ebook_to_audiobook:latest https://github.com/jondana/eBook_to_Audiobook_with_F5-TTS.git && docker run -d --gpus all -p 7860:7860 --name ebook_to_audiobook_container ebook_to_audiobook:latest && docker logs -f ebook_to_audiobook_container

```

If you donwnload the repository into a folder:

1. Double click Build.bat, wait for it to finish
2. Double click Run.bat to launch


## License:
- GPL-3.0

## Acknowledgments

- This project uses code adapted from [fakerybakery](https://github.com/fakerybakery)'s Hugging Face space [E2-F5-TTS](https://huggingface.co/spaces/mrfakename/E2-F5-TTS) and [DrewThomasson](https://github.com/DrewThomasson)'s Hugging Face space [ebook2audiobook](https://huggingface.co/spaces/drewThomasson/ebook2audiobook). Thanks for your amazing work!

