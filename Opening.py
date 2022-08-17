import pyautogui
import pygame as py
import time
import UIElement

WHITE = (255, 255, 255)
def main():
    clock = py.time.Clock()
    width, height = pyautogui.size()
    screen = py.display.set_mode((width, height))
    text_arr = ["The worlds currently engaged in a universal war,",
                "Sought a hero to finally end it all.",
                "The Galaxy Alliance chose 100 members to enter the Tower,",
                "A place where death is meaningless as long as one completes it in time",
                "And you were the last one chosen to represent and save humanity.",
                "",
                "Objective: Clear the 100 floor tower within 300 days."]
    surf_done = False

    while surf_done == False:
        for i in range(len(text_arr)):
            num = 0
            for _ in range(16):
                scale = (num, num, num)
                UIElement.writeText(text_arr[i], 40, scale, (width/12, height/6 + (60 * i)), screen)
                py.time.delay(80)
                num = num + 16
                py.display.flip()

        time.sleep(4)
        surf_done = True