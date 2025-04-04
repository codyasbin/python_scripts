from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

def set_system_volume_to_80():
    # First, mute the system volume to ensure a consistent starting point
    #for _ in range(50):
       # pyautogui.press("volumedown")
        #time.sleep(0.05)  # Small delay between key presses

    # Now, increase the volume to 80% by pressing volume up key 40 times
    for _ in range(40):
        pyautogui.press("volumeup")
        time.sleep(0.05)  # Small delay between key presses

def enter_full_screen1():
    # Simulate pressing F11 to enter full screen mode
    pyautogui.press("f11")
    time.sleep(2)  # Small delay to ensure the action is registered

def enter_full_screen2():
    # Simulate pressing F11 to enter full screen mode
    pyautogui.press("f")
    time.sleep(2)  # Small delay to ensure the action is registered
try:

    # Initialize the WebDriver without specifying the path to ChromeDriver
    driver = webdriver.Chrome()

    # Open YouTube
    driver.get('https://www.youtube.com')
    time.sleep(3)  # Wait for the page to load

       # Enter full screen mode
    enter_full_screen1()
    # Find the search bar using its name attribute value
    search_box = driver.find_element(By.NAME, 'search_query')

    # Type the search query and hit Enter
    search_query = 'nidari by bartika eam rai'
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for the search results to load

    # Find the first video in the search results and click on it
    first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
    first_video.click()


    print("Playing the video...")
    # Set system volume to 80%
    set_system_volume_to_80()
        # Enter full screen mode
    enter_full_screen2()

    # Wait for the video to start playing (adjust sleep time if needed)
    time.sleep(10)  # Increase if needed

    # Wait for the video to finish playing (adjust sleep time if needed)
    time.sleep(1000)  # Adjust as needed

finally:
    # Close the browser window
    driver.quit()
