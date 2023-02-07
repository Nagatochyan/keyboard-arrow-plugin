import pyautogui
import keyboard
while True:
  if keyboard.read_key() == "shift+right":
    pyautogui.write("→")
  if keyboard.read_key() == "shift+left":
    pyautogui.write("←")
  if keyboard.read_key() == "shift+up":
    pyautogui.write("↑")
  if keyboard.read_key() == "shift+down": 
    pyautogui.write("↓")
    
    
