#!/usr/bin/python3
import schedule
import pyautogui
import time

# google tab
first_tab = (158, 10)
left_side = (324, 184)

# photo folder tab
second_tab = (327, 6)
right_side_one = (900, 131)
right_side_two = (866, 131)
print(pyautogui.position())
print(pyautogui.size())

def job():
    print('Clicking the first tab Google Photos')
    pyautogui.click(first_tab)
    time.sleep(1)
    print('Reloading the window')
    pyautogui.hotkey("ctrlleft", "r")
    time.sleep(4)

    print('Clicking the second tab Photos Folder')
    pyautogui.click(second_tab)
    time.sleep(1)
    print('Selecting all the photos')
    pyautogui.click(right_side_one)

    pyautogui.hotkey("ctrlleft", "a")
    time.sleep(5)
    pyautogui.moveTo(right_side_two) 

    pyautogui.dragTo(left_side, duration = 2)

# schedule.every().day.at("19:30").do(job)
schedule.every().day.at("00:13").do(job)


while True:
    schedule.run_pending()
    time.sleep(20)