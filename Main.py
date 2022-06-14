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
    pygame.display.set_caption('Calc Gane Dating Simulator')

    # Fill background
    # background = pygame.Surface(screen.get_size())

    #Get Background image
    background = pygame.image.load('Assets\image.jpg')
    background = pygame.transform.scale(background, (width, height))

    # Display some text
    fontsize = 60
    font = pygame.font.Font(None, fontsize)
    font2 = pygame.font.Font(None, int(fontsize*2/3))
    text1 = font.render("TOWER TRIALS", 1, (BLACK))
    #textpos = text.get_rect(center=(width/2, height/2))
    #textpos.centerx = background.get_rect().centerx
    background.blit(text1, (width/8, height/4))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # create ui elements
    startElement = UIElement.UITextElement(
        center_position=(width/6, height* 3 / 6),
        font_size=fontsize*2/3,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Start",
        action= GameState.GameStates.START,
    )

    quitElement = UIElement.UITextElement(
        center_position=(width/6, height* 4 / 6),
        font_size=fontsize*2/3,
        bg_rgb=None,
        text_rgb=BLACK,
        text="Quit",
        action=GameState.GameStates.QUIT,
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