import pyautogui
import pygame
from pygame.locals import *
import Main
from Character_Data.Character import Character
import Character_Data.Healing as Healing
import Screen.StatsScreen as StatsScreen
import Screen.EnemyScreen as EnemyScreen
import Screen.BossScreen as BossScreen
import Screen.EndScreen as EndScreen
import Screen.SettingsScreen as SettingsScreen
import Screen.HelpScreen as HelpScreen

import GameState
import UIElement

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

user = Character.newCharacter()
towerFloor = 1
lines = open('Character_Data\GameData.txt', 'r').readlines()
lines[4] = lines[4].replace("'", "")
recordDays = list(map(str, lines[4][1:len(lines[4]) - 1].split(", ")))
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
    gameFile = open('Character_Data/GameData.txt')
    gameDataText = gameFile.read()
    gameData = gameDataText.split("\n")
    gameData[0] = tuple(map(float, gameData[0][1:len(gameData[0]) - 1].split(", ")))
    level, hp, maxHp, energy, maxEnergy, exp, statPoints, expPoints = gameData[0]
    gameData[1] = list(map(float, gameData[1][1:len(gameData[1]) - 1].split(", ")))
    charStats = gameData[1]
    user = Character(level, hp, maxHp, energy, maxEnergy, exp, statPoints, expPoints, charStats)
    heal = Healing.Healing(int(gameData[2]))
    towerFloor = int(gameData[3])
    gameData[4] = gameData[4].replace("'", "")
    recordDays = list(map(str, gameData[4][1:len(gameData[4]) - 1].split(", ")))
    user.setDays(float(gameData[5]))
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

    heartImage = pygame.image.load('Assets\GameImages\RedHeart.png')
    heartImage = pygame.transform.scale(heartImage, (60, 60))
    heart_center = ((width*4/5 - heartImage.get_width() / 2), (height*5/6 - 40 - heartImage.get_height() / 2))

    enemyImage = pygame.image.load('Assets\GameImages\enemy.png')
    enemyImage = pygame.transform.scale(enemyImage, (60, 60))
    enemy_center = ((width*2/5 - enemyImage.get_width() / 2), (height*5/6 - 40 - enemyImage.get_height() / 2))

    bossImage = pygame.image.load('Assets\GameImages\Boss.jpg')
    bossImage = pygame.transform.scale(bossImage, (60, 60))
    boss_center = ((width*3/5 - bossImage.get_width() / 2), (height*5/6 - 40 - bossImage.get_height() / 2))
    
    click = pygame.mixer.Sound('Assets\ClickSound.wav')

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
        text= "Level: " + str(int(user.getLevel())),
        highlight_true = False,
        action=None,
    )
    expElement = UIElement.UITextElement(
        center_position=(width*1 / 10, (height* 1 / 10) + gameTextSize),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Experience: " + str(int(user.getExperience())) + " / " + str(user.expToNextLevel()),
        highlight_true = False,
        action=None,
    )
    getExpElement = UIElement.UITextElement(
        center_position=(width*2/5, height* 5 / 6),
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
        font_size=gameTextSize*2,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Floor " + str(towerFloor),
        highlight_true = False,
        action=None,
    )
    getBossElement = UIElement.UITextElement(
        center_position=(width*3/5, height* 5 / 6),
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
        center_position=(width*4/5, height* 5 / 6),
        font_size=gameTextSize,
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Heal",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )
    settings = UIElement.UITextElement(
        center_position=(width*11 / 12, height* 11 / 12),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Settings",
        highlight_true = True,
        action=GameState.GameStates.SETTINGS,
    )
    saveElement = UIElement.UITextElement(
        center_position=(width*13 / 36, height* 11 / 12),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Save",
        highlight_true = True,
        action=GameState.GameStates.SETTINGS,
    )
    helpElement = UIElement.UITextElement(
        center_position=(width*23 / 36, height* 11 / 12),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text= "Help",
        highlight_true = True,
        action=GameState.GameStates.SETTINGS,
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
        settings_action = settings.update(pygame.mouse.get_pos(), mouse_up)
        save_action = saveElement.update(pygame.mouse.get_pos(), mouse_up)
        help_action = helpElement.update(pygame.mouse.get_pos(), mouse_up)

        titleElement.draw(screen)
        getExpElement.draw(screen)
        getBossElement.draw(screen)
        healingElement.draw(screen)
        settings.draw(screen)
        saveElement.draw(screen)
        helpElement.draw(screen)

        screen.blit(heartImage, heart_center)
        screen.blit(enemyImage, enemy_center)
        screen.blit(bossImage, boss_center)

        if title_action is not None:
            click.play()
            return Main.main()
        if getExp_action is not None: 
            click.play()
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

            screen.blit(background, (width/8, height/8))
            print(SettingsScreen.healOn)
            if SettingsScreen.healOn == True:
                user.hitpoints = heal.autoHeal(user.hitpoints, user.maxHitpoints, 100)
        
            gameElement = UIElement.UITextElement(
                center_position=(width*1 / 10, height* 1 / 10),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Level: " + str(int(user.getLevel())),
                highlight_true = False,
                action=None,
            )
            expElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Experience: " + str(int(user.getExperience())) + " / " + str(user.expToNextLevel()),
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
                font_size=gameTextSize*2,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Floor " + str(towerFloor),
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
            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement, healingElement, settings, saveElement, helpElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)

        if boss_action is not None:
            click.play()
            defeatedEnemy = BossScreen.run(towerFloor)
            if defeatedEnemy == True:
                user.addDays(1, user.getEnergy())
                towerFloor = towerFloor + 1
                user.energy = user.getMaxEnergy()
            else: 
                user.zeroHealth()
            if(towerFloor <= 100):
                while(user.getStatPoints() > 0):
                    screen.fill(BLACK)
                    pygame.display.flip()
                    StatsScreen.run()
            screen.fill(BLACK)
            pygame.display.flip()

            screen.blit(background, (width/8, height/8))

            gameElement = UIElement.UITextElement(
                center_position=(width*1 / 10, height* 1 / 10),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Level: " + str(int(user.getLevel())),
                highlight_true = False,
                action=None,
            )
            expElement = UIElement.UITextElement(
                center_position=(width*1 / 10, (height* 1 / 10) + gameTextSize),
                font_size=gameTextSize,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Experience: " + str(int(user.getExperience())) + " / " + str(user.expToNextLevel()),
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
                font_size=gameTextSize * 2,
                bg_rgb=None,
                text_rgb=WHITE,
                text= "Floor " + str(towerFloor),
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
            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement, settings, saveElement, helpElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)
        
        if healing_action is not None:
            click.play()
            user.hitpoints = heal.autoHeal(user.hitpoints, user.maxHitpoints, 100)
            screen.fill(BLACK)
            pygame.display.flip()

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

            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement, settings, saveElement, helpElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)
        if settings_action is not None:
            click.play()
            screen.fill(BLACK)
            pygame.display.flip()
            SettingsScreen.run()
            screen.fill(BLACK)
            pygame.display.flip()
            screen.blit(background, (width/8, height/8))
            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement, settings, saveElement, helpElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)

        if save_action is not None:
            click.play()
            gameFile = open('Character_Data/GameData.txt', 'w')
            gameFile.write(str(user.getCharacterInfo()) + "\n" + str(user.getCharacterStats()) + "\n")
            gameFile.write(str(heal.getHeal()) + "\n" + str(towerFloor) + "\n" + str(recordDays) + "\n" + str(user.getDays()) + "\n")
            gameFile.write("ID: ")
            gameFile.close()

        if help_action is not None:
            click.play()
            screen.fill(BLACK)
            pygame.display.flip()
            HelpScreen.run()
            screen.fill(BLACK)
            pygame.display.flip()

            screen.blit(background, (width/8, height/8))

            allElements = [titleElement, gameElement, expElement, getExpElement, daysElement, healthElement, energyElement, floorElement, getBossElement, healElement, settings, saveElement, helpElement]
            for i in range(len(allElements)):
                allElements[i].draw(screen)

        pygame.display.flip()
    return EndScreen.EndScreen()