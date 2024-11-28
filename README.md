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
- **Output Formats**: Generates audiobooks in `.mp3` format `.m4b`. was causing play/pause issues in my audiobook player
- **User-Friendly Interface**: Built with Gradio for an interactive web UI.

## Installation

### Prerequisites

- Python 3.7 or higher
- [Calibre](https://calibre-ebook.com/download) (for eBook conversion and metadata extraction)
- [FFmpeg](https://ffmpeg.org/download.html) (for audio processing)

### Clone the Repository

```bash
git clone https://github.com/jdana/ebook-to-audiobook-f5tts.git
cd ebook-to-audiobook-f5tts
