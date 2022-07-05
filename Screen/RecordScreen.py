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

def recordScreen(): 
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
    topElement = UIElement.UITextElement(
        center_position=(width*1 / 2, (height* 1 / 6) - fontsize),
        font_size=int(fontsize),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Current Records:",
        highlight_true = True,
        action=GameState.GameStates.TITLE,
    )
    recordOneElement = UIElement.UITextElement(
        center_position=(width*1 / 2, height* 1 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="1. " + str(Game.recordDays[0]) + " Days",
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )
    recordTwoElement = UIElement.UITextElement(
        center_position=(width*1 / 2, (height* 1 / 6) + 2 * fontsize/3),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="2. " + str(Game.recordDays[1]) + " Days",
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )
    recordThreeElement = UIElement.UITextElement(
        center_position=(width*1 / 2, (height* 1 / 6) + 4 * fontsize/3),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="3. " + str(Game.recordDays[2]) + " Days",
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )
    recordFourElement = UIElement.UITextElement(
        center_position=(width*1 / 2, (height* 1 / 6) + 6 * fontsize/3),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="4. " + str(Game.recordDays[3]) + " Days",
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )
    recordFiveElement = UIElement.UITextElement(
        center_position=(width*1 / 2, (height* 1 / 6) + 8 * fontsize/3),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="5. " + str(Game.recordDays[4]) + " Days",
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )
    viewRecord = True
    while viewRecord:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            click.play()
            viewRecord = False
        recordOneElement.draw(screen)
        recordTwoElement.draw(screen)
        recordThreeElement.draw(screen)
        recordFourElement.draw(screen)
        recordFiveElement.draw(screen)
        topElement.draw(screen)
        titleElement.draw(screen)

        pygame.display.flip()
    return Main.main()