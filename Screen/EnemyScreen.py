import pyautogui
import pygame
from pygame.locals import *

import UIElement
import Game
import GameState
import Enemy_Data.Enemy as Enemy
import Character_Data.Healing as Healing

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def run(towerFloor):
    heal = Game.heal
    user = Game.user
    towerFloor = Game.towerFloor
    gameEnemy, enemyName = Enemy.Enemy.getNewEnemy(towerFloor)
    maxHealth = gameEnemy.getHitpoints()
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())

    fontsize = 60
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1:
        mouse_up = False

        nameElement = UIElement.UITextElement(
            center_position=(width/6, height/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text= "Floor " + str(towerFloor) + " " + enemyName + " Enemy",
            highlight_true = False,
            action=None,
        )
        HP = gameEnemy.getHitpoints()
        if HP < 1:
            HP = 1
        hitpointElement = UIElement.UITextElement(
            center_position=(width/6, height/8 + fontsize/2),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Health: " + str(int(HP)) + " / " + str(gameEnemy.getMaxHitpoints()),
            highlight_true = False,
            action= GameState.GameStates.ENEMY,
        )
        hitEnemyElement = UIElement.UITextElement(
            center_position=(width/6, height*7/8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Fight",
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        userHP = user.getHitpoints()
        if userHP <= 1 and userHP > 0:
            userHP = 1
        healthElement = UIElement.UITextElement(
            center_position=(width*5 / 6, (height* 7 / 8) - fontsize/2 ),
            font_size= fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text= "Health: " + str(int(userHP)) + " / " + str(int(user.getMaxHitpoints())),
            highlight_true = False,
            action=None,
        )
        energyElement = UIElement.UITextElement(
            center_position=(width*5 / 6, (height* 7 / 8)),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text= "Energy: " + str('%.1f'%(user.getEnergy())) + " / " + str('%.1f'%(user.getMaxEnergy())),
            highlight_true = False,
            action=None,
        )
        gameElement = UIElement.UITextElement(
            center_position=(width*5 / 6, (height* 7 / 8) - fontsize),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text= "Level: " + str(user.getLevel()),
            highlight_true = False,
            action=None,
        )

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        hitEnemy_action = hitEnemyElement.update(pygame.mouse.get_pos(), mouse_up)
        if hitEnemy_action is not None:
            damage = user.sendAttack()
            user.changeEnergy(-0.5)
            user.checkEnergy()
            gameEnemy.getHit(damage)
            if(gameEnemy.getHitpoints() <= 0):
                user.addExperience(gameEnemy.sendExperience() * (0.9 + towerFloor/10))
                heal.addHeal(maxHealth, towerFloor)
                return True
            pygame.time.wait(200)
            enemyDamage = gameEnemy.sendAttack()
            user.getHit(enemyDamage)
            if(user.getHitpoints() <= 0):
                return False

        screen.fill(BLACK)

        allElements = [nameElement, hitpointElement, hitEnemyElement, healthElement, energyElement, gameElement]
        for i in range(len(allElements)):
                allElements[i].draw(screen)
                
        pygame.display.flip()

    return True