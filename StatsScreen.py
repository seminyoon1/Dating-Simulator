import pyautogui
import pygame
from pygame.locals import *

import Character_Data.CharacterStats
import UIElement
import Game
import GameState

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def run():
    user = Game.user
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())

    # Display some text
    fontsize = 60

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # create ui elements
    defenseElement = UIElement.UITextElement(
        center_position=(width/6, height/ 6),
        font_size=fontsize*2/3,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Defense: " + str(user.getStats()[0]),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )
    evasivenessElement = UIElement.UITextElement(
        center_position=(width/6, height/ 6),
        font_size=fontsize*2/3,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Evasiveness: " + str(user.getStats()[1]),
        highlight_true = True,
        action= GameState.GameStates.GAME,
    )

    # Event loop
    while user.getStatPoints() > 0:
        mouse_up = False

        defenseElement = UIElement.UITextElement(
            center_position=(width/6, height/ 6),
            font_size=fontsize*2/3,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Defense: " + str(user.getStats()[0]),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )

        evasivenessElement = UIElement.UITextElement(
            center_position=(width/6, height*2/6),
            font_size=fontsize*2/3,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Evasiveness: " + str(user.getStats()[1]),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        defense_action = defenseElement.update(pygame.mouse.get_pos(), mouse_up)
        evasiveness_action = evasivenessElement.update(pygame.mouse.get_pos(), mouse_up)
        if defense_action is not None:
            user.maxHitpoints, user.maxEnergy, user.stats = Character_Data.CharacterStats.addDefense(user.maxHitpoints, user.maxEnergy, user.stats)
            user.changeStatPoints(-1)
        if evasiveness_action is not None:
            user.maxEnergy, user.stats = Character_Data.CharacterStats.addEvasiveness(user.maxEnergy, user.stats)
            user.changeStatPoints(-1)

        screen.fill(BLACK)
        defenseElement.draw(screen)
        evasivenessElement.draw(screen)
        pygame.display.flip()
