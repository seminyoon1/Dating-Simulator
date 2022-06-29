import pyautogui
import pygame
from pygame.locals import *
import Main
from Character_Data.Character import Character
import Character_Data.CharacterStats as CharacterStats
import Screen.StatsScreen as StatsScreen
import Screen.EnemyScreen as EnemyScreen
import Screen.BossScreen as BossScreen
import Screen.EndScreen as EndScreen
import Character_Data.Healing as Healing

import GameState
import UIElement

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

user = Character.newCharacter()
towerFloor = 1
recordDays = ["---", "---", "---", "---", "---"]
heal = Healing.Healing.newHeal()

def newGame():
    global user, towerFloor, recordDays, heal
    towerFloor = 1
    user = Character.newCharacter()
    user.newDays()
    user.stats = [10, 10, 10, 10, 10, 10] 
    heal = Healing.Healing.newHeal()
    game()

def savedGame():
    global user, towerFloor, recordDays, heal
    recordDays = [253, 257, 265, 279, 306]
    gameFile = open('Character_Data/GameData.txt')
    gameDataText = gameFile.read()
    print(gameDataText)
    #do something here to parse data
    gameFile.close()
    game()

def game():
    global towerFloor

    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))

    fontsize = 60
    background = pygame.image.load('Assets\Floor.jpg')
    background = pygame.transform.scale(background, (width*3/4, height*3/4))
    gameTextSize = int(fontsize*1/3)

    screen.blit(background, (width/8, height/8))
    pygame.display.flip()

    titleElement = UIElement.UITextElement(
            center_position=(width*1 / 12, height*11/ 12),
            font_size=int(fontsize*2/3),
            bg_rgb=None,
            text_rgb=WHITE,
            text="Back",
            highlight_true = True,
            action=GameState.GameStates.TITLE,
    )
    gameElement = UIElement.UITextElement(
        center_position=(width*1 / 10, height* 1 / 10),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Level: " + str(user.getLevel()),
        highlight_true = False,
        action=None,
    )
    expElement = UIElement.UITextElement(
        center_position=(width*1 / 10, (height* 1 / 10) + gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Experience: " + str(user.getExperience()) + " / " + str(user.expToNextLevel()),
        highlight_true = False,
        action=None,
    )
    getExpElement = UIElement.UITextElement(
        center_position=(width*1 / 6, height* 5 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Fight Enemy",
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
        center_position=(width*1 / 10, (height* 1 / 10) + 2*gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Health: " + str(int(user.getHitpoints())) + " / " + str(int(user.getMaxHitpoints())),
        highlight_true = False,
        action=None,
    )
    energyElement = UIElement.UITextElement(
        center_position=(width*1 / 10, (height* 1 / 10) + 3*gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Energy: " + str('%.1f'%(user.getEnergy())) + " / " + str('%.1f'%(user.getMaxEnergy())),
        highlight_true = False,
        action=None,
    )
    floorElement = UIElement.UITextElement(
        center_position=(width*5 / 10, (height* 1 / 10)),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Current Floor: " + str(towerFloor),
        highlight_true = False,
        action=None,
    )
    getBossElement = UIElement.UITextElement(
        center_position=(width*3 / 6, height* 5 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Fight Boss",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )
    healElement = UIElement.UITextElement(
        center_position=(width*1 / 10, (height* 1 / 10) + 4*gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Lifedrain: " + str(int(heal.getHeal())),
        highlight_true = False,
        action=GameState.GameStates.GAME,
    )
    healingElement = UIElement.UITextElement(
        center_position=(width*5 / 6, height* 5 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Heal",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )
    allElements = [gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, healElement]
    for i in range(len(allElements)):
            allElements[i].draw(screen)

    while towerFloor <= 100:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        getExp_action = getExpElement.update(pygame.mouse.get_pos(), mouse_up)
        boss_action = getBossElement.update(pygame.mouse.get_pos(), mouse_up)
        healing_action = healingElement.update(pygame.mouse.get_pos(), mouse_up)

        titleElement.draw(screen)
        getExpElement.draw(screen)
        getBossElement.draw(screen)
        healingElement.draw(screen)
        
        #find use of energy that doesn't affect stats, is needed throughout bosses and affects all floors
        #AFFECT DAYS!

        if title_action is not None:
            return Main.main()
        if getExp_action is not None: 
            defeatedEnemy = EnemyScreen.run(towerFloor)
            if defeatedEnemy == True:
                user.addDays(1/3, user.getEnergy())
            else: 
                user.zeroHealth()
            while(user.getStatPoints() > 0):
                screen.fill(BLACK)
                pygame.display.flip()
                StatsScreen.run()
            screen.fill(BLACK)
            pygame.display.flip()

            background = pygame.image.load('Assets\Floor.jpg')
            background = pygame.transform.scale(background, (width*3/4, height*3/4))
            screen.blit(background, (width/8, height/8))
        

            gameElement = UIElement.UITextElement(
                center_position=(width*1 / 10, height* 1 / 10),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Level: " + str(user.getLevel()),
                highlight_true = False,
                action=None,
            )
            expElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Experience: " + str(user.getExperience()) + " / " + str(user.expToNextLevel()),
                highlight_true = False,
                action=None,
            )
            healthElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 2*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Health: " + str(int(user.getHitpoints())) + " / " + str(int(user.getMaxHitpoints())),
                highlight_true = False,
                action=None,
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
            energyElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 3*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Energy: " + str('%.1f'%(user.getEnergy())) + " / " + str('%.1f'%(user.getMaxEnergy())),
                highlight_true = False,
                action=None,
            )
            floorElement = UIElement.UITextElement(
                center_position=(width*5 / 10, (height* 1 / 10)),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Current Floor: " + str(towerFloor),
                highlight_true = False,
                action=None,
            )
            healElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 4*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Lifedrain: " + str(int(heal.getHeal())),
                highlight_true = False,
                action=GameState.GameStates.GAME,
            )
            healingElement = UIElement.UITextElement(
                center_position=(width*5 / 6, height* 5 / 6),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Heal",
                highlight_true = True,
                action=GameState.GameStates.GAME,
            )
            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement, healingElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)

        if boss_action is not None:
            defeatedEnemy = BossScreen.run(towerFloor)
            if defeatedEnemy == True:
                user.addDays(1, user.getEnergy())
                towerFloor = towerFloor + 1
            else: 
                user.zeroHealth()
            if(towerFloor <= 100):
                while(user.getStatPoints() > 0):
                    screen.fill(BLACK)
                    pygame.display.flip()
                    StatsScreen.run()
            screen.fill(BLACK)
            pygame.display.flip()

            background = pygame.image.load('Assets\Floor.jpg')
            background = pygame.transform.scale(background, (width*3/4, height*3/4))
            screen.blit(background, (width/8, height/8))
        

            gameElement = UIElement.UITextElement(
                center_position=(width*1 / 10, height* 1 / 10),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Level: " + str(user.getLevel()),
                highlight_true = False,
                action=None,
            )
            expElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Experience: " + str(user.getExperience()) + " / " + str(user.expToNextLevel()),
                highlight_true = False,
                action=None,
            )
            healthElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 2*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Health: " + str(int(user.getHitpoints())) + " / " + str(int(user.getMaxHitpoints())),
                highlight_true = False,
                action=None,
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
            energyElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 3*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Energy: " + str('%.1f'%(user.getEnergy())) + " / " + str('%.1f'%(user.getMaxEnergy())),
                highlight_true = False,
                action=None,
            )
            floorElement = UIElement.UITextElement(
                center_position=(width*5 / 10, (height* 1 / 10)),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Current Floor: " + str(towerFloor),
                highlight_true = False,
                action=None,
            )
            healElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 4*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Lifedrain: " + str(int(heal.getHeal())),
                highlight_true = False,
                action=GameState.GameStates.GAME,
            )
            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)
        
        if healing_action is not None:
            user.hitpoints = heal.autoHeal(user.hitpoints, user.maxHitpoints, 100)
            screen.fill(BLACK)
            pygame.display.flip()

            background = pygame.image.load('Assets\Floor.jpg')
            background = pygame.transform.scale(background, (width*3/4, height*3/4))
            screen.blit(background, (width/8, height/8))
        

            healElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 4*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Lifedrain: " + str(int(heal.getHeal())),
                highlight_true = False,
                action=GameState.GameStates.GAME,
            )
            healthElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + 2*gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Health: " + str(int(user.getHitpoints())) + " / " + str(int(user.getMaxHitpoints())),
                highlight_true = False,
                action=None,
            )

            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)

        pygame.display.flip()
    return EndScreen.EndScreen()