# eBook to Audiobook Converter with F5-TTS

![image](https://github.com/user-attachments/assets/1a2c43ed-d35a-46df-ae39-538eae3b7734)


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

Run the following single command in Command Prompt to build and start the application, once running, view the UI by going to http://localhost:7860/

```bash
docker build -t ebook_to_audiobook:latest https://github.com/jondana/eBook_to_Audiobook_with_F5-TTS.git && docker run -d -p 7860:7860 --name ebook_to_audiobook_container ebook_to_audiobook:latest && docker logs -f ebook_to_audiobook_container

```

If you donwnload the repository into a folder:

- Double click Build.bat, wait for it to finish
- Double click Run.bat to launch




