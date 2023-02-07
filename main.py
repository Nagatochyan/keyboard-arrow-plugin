import keyboard
import pyautogui
import pyperclip
def test():
  if keyboard.is_pressed("esc+right"):
    pyperclip.copy("→")
    pyautogui.hotkey('ctrl', 'v')
  if keyboard.is_pressed("esc+left"):
    pyperclip.copy("←")
    pyautogui.hotkey('ctrl', 'v')
  if keyboard.is_pressed("esc+up"):
    pyperclip.copy("↑")
    pyautogui.hotkey('ctrl', 'v')
  if keyboard.is_pressed("esc+down"):
    pyperclip.copy("↓")
    pyautogui.hotkey('ctrl', 'v')
while True:
  test()
    
