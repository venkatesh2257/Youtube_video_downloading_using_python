# YouTube Video Downloader

This project is a simple Python script that downloads YouTube videos in high resolution using `yt-dlp` and `ffmpeg`.

## Features

- Download videos from YouTube.
- Merge video and audio streams into a single MP4 file.
- High-quality downloads.

## Requirements

- Python 3.12 or higher
- `yt-dlp` Python package
- `ffmpeg` installed and accessible

## Installation

1. **Clone the Repository**:

   Open a terminal and run:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd your-repository
   ```

3. **Install Dependencies**:

   Ensure you have Python and pip installed. Install the required Python package with:
   ```bash
   pip install yt-dlp
   ```

4. **Install `ffmpeg`**:

   - **Windows**: Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add the `bin` directory to your PATH.
   - **Mac/Linux**: Install using package managers (e.g., `brew install ffmpeg` for Mac, `sudo apt-get install ffmpeg` for Ubuntu).

## Usage

1. **Update the Script**:

   Replace `YOUR_VIDEO_ID` in the script with the ID of the YouTube video you want to download.

   ```python
   video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
   ```

2. **Run the Script**:

   Execute the script using Python:
   ```bash
   python download_youtube_video.py
   ```

3. **Find the Downloaded Video**:

   The video will be saved in the same directory as the script with the name based on the video title.

## Example

For example, to download a video with the ID `B_S51m41ZPI`, you would:

1. Set `video_url` in the script to:
   ```python
   video_url = "https://www.youtube.com/watch?v=B_S51m41ZPI"
   ```

2. Run the script:
   ```bash
   python download_youtube_video.py
   ```

3. Check the directory for the downloaded file.

## Troubleshooting

- **Error: `ffmpeg` not found**: Ensure `ffmpeg` is installed and its path is correctly set in your environment variables.
- **Error: `yt-dlp` not found**: Ensure you have installed `yt-dlp` using `pip`.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, you can reach out to [your-email@example.com](mailto:vinodjc007@gmail.com).
