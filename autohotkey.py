import pyautogui
import subprocess

def send_text():
    pyautogui.typewrite('623723\t73223\t83832')

# Run xdotool command to listen for the 'q' keypress event
subprocess.Popen(['xdotool', 'keydown', 'q', 'type', '--clearmodifiers', '--delay', '100', 'keyup', 'q'], stdout=subprocess.PIPE)

# Call the send_text function when 'q' is pressed
pyautogui.hotkey('q', send_text)
