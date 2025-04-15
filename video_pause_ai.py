import cv2
import numpy as np
import pyautogui
import time

# Function to detect video pause icon
def detect_video_pause(frame, template_path):
    template = cv2.imread(template_path, 0)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    return len(loc[0]) > 0

# Main loop
def monitor_and_act():
    template_path = "pause_icon.png"
    while True:
        # Capture the screen (use ADB or screen recording libraries)
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        
        if detect_video_pause(screen_np, template_path):
            print("Video paused! Performing action...")
            # Overlay drawing
            pyautogui.moveTo(100, 100)
            pyautogui.dragTo(200, 200, duration=1)
            
            # Simulate scrolling
            pyautogui.scroll(-500)

        time.sleep(1)

monitor_and_act()
