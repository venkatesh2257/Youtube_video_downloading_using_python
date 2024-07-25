import yt_dlp

def download_youtube_video(url):
    try:
        # Define download options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
            'merge_output_format': 'mp4',  # Merge video and audio into an mp4 file
            'outtmpl': '%(title)s.%(ext)s',  # Name the output file with the title of the video
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Video downloaded successfully from URL: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your YouTube video URL
video_url = "https://www.youtube.com/watch?v=F9UC9DY-vIU"
download_youtube_video(video_url)
