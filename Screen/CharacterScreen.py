import pyautogui
import pygame
from pygame.locals import *

import UIElement
import Game
import GameState

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

def run(): 
    user = Game.user
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
        text="Back to Game",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )
    textElement = UIElement.UITextElement(
        center_position=(width/6, height/ 8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Select a skill:",
        highlight_true = False,
        action=None,
    )
    defenseElement = UIElement.UITextElement(
        center_position=(width/6, height*2/ 8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Defense: " + str('%.1f'%(user.getStats()[0])),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )
    evasivenessElement = UIElement.UITextElement(
        center_position=(width/6, height*3/8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Evasiveness: " + str('%.1f'%(user.getStats()[1])),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )
    intelligenceElement = UIElement.UITextElement(
        center_position=(width/6, height*4/ 8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Intelligence: " + str('%.1f'%(user.getStats()[2])),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )
    attackElement = UIElement.UITextElement(
        center_position=(width/6, height*5/ 8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Attack: " + str('%.1f'%(user.getStats()[3])),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )
    powerElement = UIElement.UITextElement(
        center_position=(width/6, height*6/ 8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Power: " + str('%.1f'%(user.getStats()[4])),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )
    criticalElement = UIElement.UITextElement(
        center_position=(width/6, height*7/ 8),
        font_size=fontsize/2,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Critical: " + str('%.1f'%(user.getStats()[5])),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )


    viewCharacter = True
    while viewCharacter:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            click.play()
            viewCharacter = False    

        titleElement.draw(screen)
        allElements = [defenseElement, evasivenessElement, intelligenceElement, attackElement, powerElement, criticalElement]
        for i in range(len(allElements)):
            allElements[i].draw(screen)

        pygame.display.flip()