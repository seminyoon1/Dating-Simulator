import pyautogui
import pygame
from pygame.locals import *
import Main
import Game

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

def EndScreen(): 
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())

    click = pygame.mixer.Sound('Assets\ClickSound.wav')

    fontsize = 60
    screen.blit(background, (0, 0))
    pygame.display.flip()

    titleElement = UIElement.UITextElement(
        center_position=(width*3 / 4, height* 5 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Back",
        highlight_true = True,
        action=GameState.GameStates.TITLE,
    )
    finishedGameElement = UIElement.UITextElement(
        center_position=(width*2 / 4, height* 1 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="You finished all 100 floors in " + str(round(Game.user.getDays() , 2)) + " Days",
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )

    for i in range(5):
        if Game.recordDays[i] == "---":
            Game.recordDays[i] = round(Game.user.getDays(), 2)
            break
        elif float(Game.recordDays[i]) >= round(Game.user.getDays(), 2):
            tempFirstData = Game.recordDays[i]
            Game.recordDays[i] = round(Game.user.getDays(), 2)
            for i in range(i,4):
                tempSecondData = Game.recordDays[i+1]
                Game.recordDays[i+1] = tempFirstData
                tempFirstData = tempSecondData
            break

    lines = open('Character_Data\GameData.txt', 'r').readlines()
    lines[3] = '101\n'
    lines[4] = str(Game.recordDays) + '\n'
    out = open('Character_Data\GameData.txt', 'w')
    out.writelines(lines)
    out.close()

    while 1:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            click.play()
            return Main.main()
        finishedGameElement.draw(screen)
        titleElement.draw(screen)

        pygame.display.flip()