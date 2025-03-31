\

import pyautogui
import pytesseract
import time
import keyboard
from PIL import Image
import cv2
import numpy as np



def capture_and_type():
    # Set the path to tesseract.exe if needed (for Windows users)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    # Delay before starting (switch to the MonkeyType window)
    time.sleep(3)

    # Take a screenshot of the typing area (modify region to fit your screen)
    x, y, width, height = 469, 360, 968, 161  # Adjust these values
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Convert to grayscale and preprocess the image
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    # Save and debug the captured image (optional)
    cv2.imwrite("screenshot.png", img)

    # Extract text from the processed image
    text = pytesseract.image_to_string(Image.fromarray(img), config='--psm 6')

    # Clean and split words
    word_list = text.strip().split()

    # Remove unwanted words
    unwanted_words = {'EE', 'EEE', 'OE', '0E', 'ee', 'eE', 'eEE', 'OEE', '0EE', 'OEE', '0EE', 'OEE', '0EE', 'OEE', '0EE', 'yu', 'Vwpm', 'WPM', 'Wpm', 'wpm', 'WPM', '>' }
    filtered_words = [word for word in word_list if word not in unwanted_words]

    print("Extracted Words:", filtered_words)  # Debugging

    # Wait for hotkey press before typing
    print("Press 'Alt+;' to start typing...")
    keyboard.wait('alt+;')
    time.sleep(0.5)  # Small delay to ensure the hotkey is registered

    # Type each word
    for word in filtered_words:
     pyautogui.write(word, interval=0.03)  # Adjust typing speed
    pyautogui.press("space")



""" 



import pyautogui

print("Move your mouse around. Press Ctrl+C to stop.")
while True:
    x, y = pyautogui.position()
    print(f"Mouse Position: x={x}, y={y}", end="\r")
"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

def start_typing_race():
    # Set up Selenium WebDriver (Make sure you have the correct driver installed)
    driver = webdriver.Chrome()
    driver.get("https://play.typeracer.com/")
    
    time.sleep(5)  # Wait for the page to load
    
    # Click on 'Enter a Typing Race' (adjust if needed)
    try:
        enter_race_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Enter a Typing Race')]")
        enter_race_button.click()
        time.sleep(10)  # Wait for race to start
    except Exception as e:
        print("Couldn't find the race button:", e)
        driver.quit()
        return
    
    # Find the text to type
    try:
        text_element = driver.find_element(By.CLASS_NAME, "inputPanel")
        text_to_type = text_element.text
        print("Text to type:", text_to_type)
    except Exception as e:
        print("Couldn't find the text element:", e)
        driver.quit()
        return
    
    # Click on the input field
    try:
        input_field = driver.find_element(By.CLASS_NAME, "txtInput")
        time.sleep(1)  # Wait for the input field to be ready
        input_field.click()
        print("Input field clicked.")
    except Exception as e:
        print("Couldn't find the input field:", e)
        driver.quit()
        return
    
    time.sleep(1)
    
    # Type the text using PyAutoGUI
    for char in text_to_type:
        pyautogui.typewrite(char)  # Adjust typing speed
        #time.sleep(0.001)  # Simulate human-like delay
    
    print("Typing complete!")
    
    time.sleep(3)  # Keep the browser open for a while
    driver.quit()


question = input("Human benchmark or typeracer? (h/t): ").strip().lower()
if question == 'h': 
    capture_and_type()
elif question == 't':
    start_typing_race()
