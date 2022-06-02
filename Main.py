#!/usr/bin/python
import pyautogui
import os
import pygame
from pygame.locals import *

import numpy as np
import cv2

import GameState
import UIElement
import StartScreen

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    # Get Screensize
    width, height = pyautogui.size()

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Calc Gang Dating Simulator')

    # Fill background
    # background = pygame.Surface(screen.get_size())


    #Get Background image
    background = pygame.image.load('Assets\image.jpg')
    background = pygame.transform.scale(background, (width, height))

    # Display some text
    font = pygame.font.Font(None, 60)
    text = font.render("CALC GANG DATING SIM", 1, (BLUE))
    textpos = text.get_rect(center=(width/2, height/2))
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # create ui elements
    quitElement = UIElement.UIElement(
        center_position=(width*3 / 4, height* 5 / 6),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="Quit",
        action=GameState.GameStates.QUIT,
    )
    startElement = UIElement.UIElement(
        center_position=(width / 2, height* 5 / 6),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="Start",
        action= GameState.GameStates.START,
    )

    # Event loop
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
        start_action = startElement.update(pygame.mouse.get_pos(), mouse_up)
        if start_action is not None:
            return StartScreen.StartScreen()
        quitElement.draw(screen)
        startElement.draw(screen)
        #screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()