import pyautogui
import pygame
from pygame.locals import *

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

musicOn = True
healOn = True
def run(): 
    global musicOn, healOn
    if musicOn == True:
        text = "ON"
    else:
        text = "OFF"
    if healOn == True:
        heal = "ON"
    else:
        heal = "OFF"
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
    musicElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 1 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Music: " + text,
        highlight_true = True,
        action=GameState.GameStates.MUSIC,
    )
    healElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 2 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Auto Heal: " + heal,
        highlight_true = True,
        action=GameState.GameStates.MUSIC,
    )
    viewSettings = True
    while viewSettings:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        music_action = musicElement.update(pygame.mouse.get_pos(), mouse_up)
        heal_action = healElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            click.play()
            viewSettings = False
        if music_action is not None:
            click.play()
            if text == "ON":
                text = "OFF"
                musicOn = False
                pygame.mixer.music.pause()
                screen.fill(BLACK)
                pygame.display.flip()

                musicElement = UIElement.UITextElement(
                    center_position=(width*1 / 6, height* 1 / 6),
                    font_size=int(fontsize*2/3),
                    bg_rgb=None,
                    text_rgb=WHITE,
                    text="Music: " + text,
                    highlight_true = True,
                    action=GameState.GameStates.MUSIC,
                )
            else:
                text = "ON"
                musicOn = True
                pygame.mixer.music.unpause()
                screen.fill(BLACK)
                pygame.display.flip()
                musicElement = UIElement.UITextElement(
                    center_position=(width*1 / 6, height* 1 / 6),
                    font_size=int(fontsize*2/3),
                    bg_rgb=None,
                    text_rgb=WHITE,
                    text="Music: " + text,
                    highlight_true = True,
                    action=GameState.GameStates.MUSIC,
                )
        if heal_action is not None:
            click.play()
            if heal == "ON":
                heal = "OFF"
                healOn = False
                screen.fill(BLACK)
                pygame.display.flip()

                healElement = UIElement.UITextElement(
                    center_position=(width*1 / 6, height* 2 / 6),
                    font_size=int(fontsize*2/3),
                    bg_rgb=None,
                    text_rgb=WHITE,
                    text="Auto Heal: " + heal,
                    highlight_true = True,
                    action=GameState.GameStates.HEAL,
                )
            else:
                heal = "ON"
                healOn = True
                screen.fill(BLACK)
                pygame.display.flip()
                healElement = UIElement.UITextElement(
                    center_position=(width*1 / 6, height* 2 / 6),
                    font_size=int(fontsize*2/3),
                    bg_rgb=None,
                    text_rgb=WHITE,
                    text="Auto Heal: " + heal,
                    highlight_true = True,
                    action=GameState.GameStates.HEAL,
                )
        healElement.draw(screen)
        musicElement.draw(screen)
        titleElement.draw(screen)

        pygame.display.flip()