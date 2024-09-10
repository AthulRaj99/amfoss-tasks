# 🎬 Subtitle Downloader CLI

Welcome to the Subtitle Downloader CLI! This command-line tool helps you effortlessly download subtitles for your favorite movies from OpenSubtitles. Whether you're working with a single movie file or need to process an entire directory in batch mode, this tool has you covered. Plus, it supports subtitles in multiple languages!

## 🚀 Features

- **IMDb ID Extraction**: Automatically extracts IMDb ID from movie filenames.
- **Multi-Language Support**: Download subtitles in your preferred language using ISO language codes (e.g., `eng` for English, `spa` for Spanish).
- **Batch Mode**: Process all video files in a directory at once.
- **Supports Multiple Formats**: Works with `.mp4`, `.mkv`, `.avi`, and `.mpeg4` files.

## 📥 Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

### Command-Line Options

- `-o`, `--output`: Specify the output folder for downloaded subtitles (default: current directory).
- `-b`, `--batch-download`: Enable batch mode to process all movies in a directory.
- `-l`, `--language`: Choose the subtitle language using ISO 639-2 codes (e.g., `eng`, `spa`, `rus`).

### Examples

#### Single File

To download Spanish subtitles for a specific movie file:

```bash
python3 main.py /path/to/your/movie.mp4 --language spa

