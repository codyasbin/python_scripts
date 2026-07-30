"""Download a YouTube video from a URL using yt-dlp.

Usage:
    python youtube-video-downloader.py
    python youtube-video-downloader.py <youtube_url> [output_dir]
"""

import shutil
import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("Missing dependency. Install it with: pip install yt-dlp")

# Fallback path in case ffmpeg was just installed and isn't on PATH yet
# for the current process (common right after a winget install).
_FFMPEG_FALLBACK_DIR = (
    Path.home()
    / "AppData/Local/Microsoft/WinGet/Packages"
    / "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    / "ffmpeg-8.1.2-full_build/bin"
)


def _find_ffmpeg() -> str | None:
    if shutil.which("ffmpeg"):
        return None  # let yt-dlp find it on PATH
    if (_FFMPEG_FALLBACK_DIR / "ffmpeg.exe").exists():
        return str(_FFMPEG_FALLBACK_DIR)
    return None


def _list_video_formats(info: dict) -> list[dict]:
    best_by_height: dict[int, dict] = {}
    for f in info.get("formats", []):
        height = f.get("height")
        if not height or f.get("vcodec") == "none":
            continue
        current = best_by_height.get(height)
        is_avc1 = (f.get("vcodec") or "").startswith("avc1")
        if current is None or (is_avc1 and not (current.get("vcodec") or "").startswith("avc1")):
            best_by_height[height] = f
    return sorted(best_by_height.values(), key=lambda f: f["height"], reverse=True)


def _prompt_format_choice(info: dict) -> tuple[str, list[dict]]:
    formats = _list_video_formats(info)

    print(f"\n{info.get('title', 'Video')}")
    print("0) Best available (auto)")
    for i, f in enumerate(formats, start=1):
        size = f.get("filesize") or f.get("filesize_approx")
        size_str = f"~{size / 1_048_576:.1f} MB" if size else "size unknown"
        print(f"{i}) {f['height']}p  ({f.get('ext')}, {f.get('vcodec')})  {size_str}")
    audio_choice = len(formats) + 1
    print(f"{audio_choice}) Audio only (mp3)")

    raw = input(f"Select quality [0]: ").strip() or "0"

    if raw == str(audio_choice):
        return "bestaudio/best", [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ]

    if raw == "0" or not raw.isdigit() or not (1 <= int(raw) <= len(formats)):
        return "bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", []

    fmt = formats[int(raw) - 1]
    return f"{fmt['format_id']}+bestaudio/best", []


def download_video(url: str, output_dir: str = "downloads") -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    base_opts = {"noplaylist": True, "quiet": True}
    ffmpeg_dir = _find_ffmpeg()
    if ffmpeg_dir:
        base_opts["ffmpeg_location"] = ffmpeg_dir

    with yt_dlp.YoutubeDL(base_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    format_str, postprocessors = _prompt_format_choice(info)

    ydl_opts = {
        **base_opts,
        "format": format_str,
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "postprocessors": postprocessors,
        "progress_hooks": [_progress_hook],
        "quiet": False,
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
