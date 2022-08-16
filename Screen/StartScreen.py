import pyautogui
import pygame
from pygame.locals import *
import Main
import Game
import Screen.RecordScreen as RecordScreen

import GameState
import UIElement
import Opening

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

def StartScreen(): 
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())

    background = pygame.image.load('Assets\TowerBackground.jpg')
    background = pygame.transform.scale(background, (width, height))
    click = pygame.mixer.Sound('Assets\ClickSound.wav')

    fontsize = 60
    screen.blit(background, (0, 0))
    pygame.display.flip()

    titleElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 4 / 5),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Back",
        highlight_true = True,
        action=GameState.GameStates.TITLE,
    )
    newGameElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 1 / 5),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="New Game", # should be new game later on
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )
    loadGameElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 2 / 5),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Load Saved Game",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )
    recordElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 3 / 5),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="View Record",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )


    while 1:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        game_action = newGameElement.update(pygame.mouse.get_pos(), mouse_up)
        savedGame_action = loadGameElement.update(pygame.mouse.get_pos(), mouse_up)
        record_action = recordElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            click.play()
            return Main.main()
        if game_action is not None:
            click.play()
            Opening.main()
            return Game.newGame()
        if record_action is not None:
            click.play()
            return RecordScreen.recordScreen()
        recordElement.draw(screen)
        newGameElement.draw(screen)
        titleElement.draw(screen)

        gameFile = open('Character_Data/GameData.txt')
        gameDataText = gameFile.read()
        gameLines = open('Character_Data\GameData.txt', 'r').readlines()
        if savedGame_action is not None:
            if gameDataText != "":
                if int(gameLines[3]) <= 100:
                    click.play()
                    return Game.savedGame()
            
        loadGameElement.draw(screen)
        gameFile.close()

        pygame.display.flip()