import keyboard
import pyautogui
import pyperclip
def test():
  if keyboard.is_pressed("shift+right"):
    pyperclip.copy("→")
    pyautogui.hotkey('ctrl', 'v')
  if keyboard.is_pressed("shift+left"):
    pyperclip.copy("←")
    pyautogui.hotkey('ctrl', 'v')
  if keyboard.is_pressed("shift+up"):
    pyperclip.copy("↑")
    pyautogui.hotkey('ctrl', 'v')
  if keyboard.is_pressed("shift+down"):
    pyperclip.copy("↓")
    pyautogui.hotkey('ctrl', 'v')
while True:
  test()
