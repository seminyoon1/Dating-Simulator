import pyautogui
import pygame
from pygame.locals import *
import Main

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def StartScreen(): 
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Calc Gang Dating Simulator')

    background = pygame.image.load('Assets\image.jpg')
    background = pygame.transform.scale(background, (width, height))

    fontsize = 60

    screen.blit(background, (0, 0))
    pygame.display.flip()

    titleElement = UIElement.UITextElement(
        center_position=(width*3 / 4, height* 5 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=BLACK,
        text="Back to Title Screen",
        action=GameState.GameStates.TITLE,
    )

    while 1:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            return Main.main()
        titleElement.draw(screen)
        #screen.blit(background, (0, 0))
        pygame.display.flip()
    
