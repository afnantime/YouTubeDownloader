# YouTubeDownloader

A simple Flask application to download YouTube videos or audio with an option to select the resolution for videos.

## Features
- Download video in MP4 format with selectable resolution.
- Download audio in MP3 format.
- Caching mechanism to avoid redundant downloads.

## Requirements
- Python 3.x
- `pytube` library
- `pydub` library
- `ffmpeg`

## Installation

1. **Install Python 3.x**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Install required libraries**:
    ```bash
    pip install Flask pytube pydub
    ```

3. **Install `ffmpeg`**:
    - **For Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add the path to the `ffmpeg` bin directory to your system's PATH.
    - **For macOS**: Use Homebrew
        ```bash
        brew install ffmpeg
        ```
    - **For Linux (Debian-based)**:
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/afnantime/YouTubeDownloader.git
    cd YouTubeDownloader
    ```

2. Run the application:
    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000`.

4. Follow the prompts:
    - Enter the YouTube video URL.
    - Enter 'mp3' to download audio or 'mp4' to download video.
    - If downloading video, enter the desired resolution (e.g., '720p') or press Enter to download the highest resolution available.

## Disclaimer
This script is for educational purposes only. Please respect YouTube's Terms of Service and do not use this script to download copyrighted content without permission.
