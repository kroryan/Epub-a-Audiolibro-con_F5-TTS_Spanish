# eBook to Audiobook Converter with F5-TTS

Turn your eBooks into audiobooks using the F5-TTS text-to-speech model. This application allows you to upload an eBook file and a reference voice sample to generate a personalized audiobook. The app supports various eBook formats and provides advanced settings to customize the output.

## Features

- **Voice Customization**: Upload a voice sample (<15 seconds) to mimic in the generated audiobook.
- **Multiple eBook Formats**: Supports `.epub`, `.mobi`, `.pdf`, `.txt`, and `.html` files.
- **Batch Processing**: Upload multiple eBooks for batch conversion.
- **Advanced Settings**:
  - Reference text input for more accurate voice cloning.
  - Adjust speech speed.
  - Customize cross-fade duration between audio chunks.
- **Metadata Handling**: Extracts and embeds eBook metadata and cover images into the audiobook files.
- **Output Formats**: Generates audiobooks in `.mp3` and `.m4b` formats. (Previously `.m4b` format caused play/pause issues in some audiobook players.)
- **User-Friendly Interface**: Built with Gradio for an interactive web UI.

## Installation

CUDA GPU Recomended 

### Docker

- Install Docker

Run the following single command in Command Prompt to build and start the application, once running, open it by going to http://localhost:7860/

```bash
docker build -t ebook_to_audiobook:latest https://github.com/jondana/eBook_to_Audiobook_with_F5-TTS.git && docker run -d -p 7860:7860 ebook_to_audiobook:latest

```

If you donwnload the repository into a folder:

- Double click Build.bat, wait for it to finish
- Double click Run.bat to launch




