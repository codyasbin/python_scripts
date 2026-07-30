"""Download a YouTube video from a URL using yt-dlp.

Usage:
    python youtube-video-downloader.py
    python youtube-video-downloader.py <youtube_url> [output_dir]
"""

import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("Missing dependency. Install it with: pip install yt-dlp")


def download_video(url: str, output_dir: str = "downloads") -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "progress_hooks": [_progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "video")
        print(f"\nDownloaded: {title}")


def _progress_hook(d: dict) -> None:
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "").strip()
        print(f"\rDownloading... {percent} at {speed}", end="", flush=True)
    elif d["status"] == "finished":
        print("\nProcessing download...")


def main() -> None:
    if len(sys.argv) > 1:
        url = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "downloads"
    else:
        url = input("Enter YouTube video URL: ").strip()
        output_dir = "downloads"

    if not url:
        sys.exit("No URL provided.")

    try:
        download_video(url, output_dir)
    except Exception as e:
        sys.exit(f"Download failed: {e}")


if __name__ == "__main__":
    main()
