import pyautogui #gonna need to pip install the library

pixel = 50
while True:
	pixel *= -1
	pyautogui.moveRel(0, pixel, duration=.2)
