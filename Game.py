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
    hit_sound = pygame.mixer.Sound('Assets/HitSound.mp3')

    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Calc Gang Dating Simulator')

    background = pygame.Surface(screen.get_size())

    #background = pygame.image.load('Assets\image.jpg')
    #background = pygame.transform.scale(background, (width, height))

    fontsize = 60
    gameTextSize = int(fontsize*1/3)

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
        center_position=(width*1 / 6, height* 1 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Level: " + str(user.getLevel()),
        highlight_true = False,
        action=None,
    )

    expElement = UIElement.UITextElement(
        center_position=(width*1 / 6, (height* 1 / 6) + gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Experience: " + str(user.getExperience()),
        highlight_true = False,
        action=None,
    )

    getExpElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 5 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Click for EXP",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )

    daysElement = UIElement.UITextElement(
        center_position=(width*9 / 10, height* 1 / 10),
        font_size=gameTextSize*2,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Days: " + str(int(user.getDays())),
        highlight_true = False,
        action=None,
    )

    healthElement = UIElement.UITextElement(
        center_position=(width*1 / 6, (height* 1 / 6) + 2*gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Health: " + str(int(user.getHitpoints())) + " / " + str(int(user.getMaxHitpoints())),
        highlight_true = False,
        action=None,
    )

    hitElement = UIElement.UITextElement(
        center_position=(width*3 / 6, height* 5 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Click to get Hit",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )

    while 1:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        getExp_action = getExpElement.update(pygame.mouse.get_pos(), mouse_up)
        hit_action = hitElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            return Main.main()
        if getExp_action is not None:
            user.addExperience()
            user.addDays(1/3)
            return game()
        if hit_action is not None:
            user.getHit(10)
            pygame.mixer.Sound.play(hit_sound)
            return game()
        getExpElement.draw(screen)      
        titleElement.draw(screen)
        gameElement.draw(screen)
        expElement.draw(screen)
        daysElement.draw(screen)
        healthElement.draw(screen)
        hitElement.draw(screen)
        
        #screen.blit(background, (0, 0))
        pygame.display.flip()
