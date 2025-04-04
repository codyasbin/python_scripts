import os
import subprocess
import pyautogui
import time

# Function to open the Photos app
def open_photos():
    # Use subprocess to open the Photos app
    subprocess.Popen('explorer.exe shell:AppsFolder\\Microsoft.Windows.Photos_8wekyb3d8bbwe!App')

def start_slideshow():
    # Allow some time for the Photos app to open
    time.sleep(5)
    
    # Simulate pressing 'F5' to start the slideshow
    pyautogui.press('f5')

# Open the Photos app
open_photos()

# Start the slideshow
start_slideshow()

