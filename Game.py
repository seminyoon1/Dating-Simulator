import pyautogui
import pygame
from pygame.locals import *
import Main
from Character_Data.Character import Character
import Character_Data.CharacterStats

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
user = Character.newCharacter() 

def game(): 
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Calc Gang Dating Simulator')

    background = pygame.Surface(screen.get_size())

    #background = pygame.image.load('Assets\image.jpg')
    #background = pygame.transform.scale(background, (width, height))

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

    gameElement = UIElement.UITextElement(
        center_position=(width*1 / 4, height* 5 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Level: " + str(user.getLevel()),
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )

    expElement = UIElement.UITextElement(
        center_position=(width*1 / 4, height* 3 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Experience: " + str(user.getExperience()),
        highlight_true = False,
        action=None,
    )

    while 1:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        game_action = gameElement.update(pygame.mouse.get_pos(), mouse_up)
        exp_action = expElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            return Main.main()
        titleElement.draw(screen)
        if game_action is not None:
            user.addExperience()
            return game()
        gameElement.draw(screen)
        if exp_action is not None:
            return None
        expElement.draw(screen)
        #screen.blit(background, (0, 0))
        pygame.display.flip()
        