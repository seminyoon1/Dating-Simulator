import pyautogui
import pygame
from pygame.locals import *

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

def run(): 
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

    UIElement.writeText("User Information:", fontsize/2, WHITE, (width/20, (height/16)), screen)
    UIElement.writeText("Level: Capped at 100, will receive 2 stat points per level.", fontsize/3, WHITE, (width/20, (height/16) + (3 * fontsize/6)), screen)
    UIElement.writeText("Experience: Needed to level up.", fontsize/3, WHITE, (width/20, (height/16) + (5 * fontsize/6)), screen)
    UIElement.writeText("Health: Receive up to 5 additional days upon death.", fontsize/3, WHITE, (width/20, (height/16) + (7 * fontsize/6)), screen)
    UIElement.writeText("Energy: Higher energy reduces the total amount of days. Reset every floor.", fontsize/3, WHITE, (width/20, (height/16) + (9 * fontsize/6)), screen)
    UIElement.writeText("Lifedrain: Received by beating normal enemies. Used to heal yourself.", fontsize/3, WHITE, (width/20, (height/16) + (11 * fontsize/6)), screen)
    UIElement.writeText("Days: Used to track progress and set record.", fontsize/3, WHITE, (width/20, (height/16) + (13 * fontsize/6)), screen)
    UIElement.writeText("Floor: Beat Floor 100 Boss to clear the game.", fontsize/3, WHITE, (width/20, (height/16) + (15 * fontsize/6)), screen)
    UIElement.writeText("Enemy Information:", fontsize/2, WHITE, (width/20, (height*5/16)), screen)
    UIElement.writeText("Enemy: Gives lifedrain when defeated. Higher floor enemies give less lifedrain.", fontsize/3, WHITE, (width/20, (height*5/16) + (3 * fontsize/6)), screen)
    UIElement.writeText("Boss: Every 5th boss will have a boost to one of their stats, 25th boss will have a boost to all stats.", fontsize/3, WHITE, (width/20, (height*5/16) + (5 * fontsize/6)), screen)
    UIElement.writeText("Enemy experience given will increase with higher floor level.", fontsize/3, WHITE, (width/20, (height*5/16) + (7 * fontsize/6)), screen)


    viewHelp = True
    while viewHelp:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            click.play()
            viewHelp = False    

        titleElement.draw(screen)

        pygame.display.flip()