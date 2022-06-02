import pyautogui
import pygame
from pygame.locals import *

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def startScreen(): 
    width, height = pyautogui.size()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Calc Gang Dating Simulator')

    background = pygame.Surface(screen.get_size())

    font = pygame.font.Font(None, 60)
    text = font.render("CALC GANG DATING SIM", 1, (BLUE))
    textpos = text.get_rect(center=(width/2, height/2))
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    quitElement = UIElement.UIElement(
        center_position=(width*3 / 4, height* 5 / 6),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="Quit",
        action=GameState.GameStates.QUIT,
    )

    while 1:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        quit_action = quitElement.update(pygame.mouse.get_pos(), mouse_up)
        if quit_action is not None:
            return
        quitElement.draw(screen)
        #screen.blit(background, (0, 0))
        pygame.display.flip()
    
