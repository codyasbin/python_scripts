import os
import subprocess
import sys


#pyinstaller : It is used to convert python script into executable file. It is a third party library which is used to convert python script into executable file. It is used to create standalone executables, under Windows, Linux, and Mac OS X. 
# commands to use: pip install pyinstaller
#pyinstaller --onefile --windowed --name RMS rms_launcher.py
# create ico or add one 
# pyinstaller --onefile --windowed --name RMS --icon=rms.ico rms_launcher.py


URL = "https://rms.viotechnologies.com"


def find_edge():
    possible_paths = [
        os.path.join(
            os.environ.get("PROGRAMFILES(X86)", ""),
            "Microsoft",
            "Edge",
            "Application",
            "msedge.exe",
        ),
        os.path.join(
            os.environ.get("PROGRAMFILES", ""),
            "Microsoft",
            "Edge",
            "Application",
            "msedge.exe",
        ),
        os.path.join(
            os.environ.get("LOCALAPPDATA", ""),
            "Microsoft",
            "Edge",
            "Application",
            "msedge.exe",
        ),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None


def main():
    edge = find_edge()

    if edge is None:
        print("Microsoft Edge was not found.")
        input("Press Enter to exit...")
        sys.exit(1)

    subprocess.Popen([
        edge,
        "--kiosk",
        URL,
        "--edge-kiosk-type=fullscreen",
    ])


if __name__ == "__main__":
    main()