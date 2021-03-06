from pyautogui import *
from datetime import datetime
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput


def get_time_stamp():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S)")

def start_game_are_u_sure():
    print(get_time_stamp(), "\n***\n\nStarting the game.")
    print(get_time_stamp(), "Botting started.")
    keyboard.press("s")
    time.sleep(0.2)
    keyboard.release("s")

    keyboard.press("space")
    time.sleep(0.2)
    keyboard.release("space")

def ens_season_are_u_sure():
    print(get_time_stamp(), "Ending the season.")
    keyboard.press("s")
    time.sleep(0.2)
    keyboard.release("s")

    keyboard.press("space")
    time.sleep(0.2)
    keyboard.release("space")

def go_to_next_game():
    print(get_time_stamp(), "Navigating to next game.")
    keyboard.press("d")
    time.sleep(0.2)
    keyboard.release("d")

def skip_all_star():
    print(get_time_stamp(), "Skipping all star games.")

    while pyautogui.locateOnScreen('assets/allstar.png', grayscale=True, confidence=0.8) is not None:
        keyboard.press("d")
        time.sleep(0.2)
        keyboard.release("d")

def skip_to_sub_in():
    print(get_time_stamp(), "Skipping to next appearance.")
    keyboard.press("x")
    time.sleep(5)
    keyboard.release("x")


print(get_time_stamp(), "Welcome to 2K21 VC MyCareer Bot, to quit it press Q on the keyboard.");
numberOfGames = 0

while keyboard.is_pressed('q') == False:
    win = gw.getWindowsWithTitle('NBA 2K20')

    if len(win) > 0:
       win[0].activate()
    else:
        print(get_time_stamp(), "NBA 2K20 is not running. Exiting.")
        break;

    if pyautogui.locateOnScreen('assets/playgame.png', grayscale=True, confidence=0.8) is not None:
        start_game_are_u_sure()
        numberOfGames += 1
        print("Game number " + str(numberOfGames) + " starting")
    elif pyautogui.locateOnScreen('assets/endseason.png', grayscale=True, confidence=0.8) is not None:
        ens_season_are_u_sure()
    elif pyautogui.locateOnScreen('assets/allstar.png', grayscale=True, confidence=0.8) is not None:
        skip_all_star()
    elif pyautogui.locateOnScreen('assets/teampractice.png', grayscale=True, confidence=0.8) is not None:
        go_to_next_game()
    elif pyautogui.locateOnScreen('assets/simToNext.png', grayscale=True, confidence=0.8) is not None:
        skip_to_sub_in()
    elif pyautogui.locateOnScreen('assets/simulator.png', grayscale=True, confidence=0.8) is not None:
        skip_to_sub_in()
        print(get_time_stamp(), "Player back in the game")
    else:
        pydirectinput.press('space')
        pydirectinput.press('x')