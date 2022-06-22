from ast import Num
import Character_Data.CharacterStats
from Character_Data.Days import Days
import random

numOfDays = Days.newDays()

class Character():

    def __init__(self, level, hitpoints, maxHitpoints, energy, maxEnergy, experience, stats, statPoints, expPoints):
        """ 
        stats:
        defense = stats[0]
        evasiveness = stats[1]
        intelligence = stats[2]
        attack = stats[3]
        critical = stats[4]
        power = stats[5]  
        """
        self.level = level
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.energy = energy
        self.maxEnergy = maxEnergy
        self.experience = experience
        self.stats = stats
        self.statPoints = statPoints
        self.expPoints = expPoints

    #All things relating to self.level
    def getLevel(self):
        return self.level
    
    def levelUp(self):
        while(self.experience >= Character.expToNextLevel(self) and self.level < 100):
            self.experience = self.experience - Character.expToNextLevel(self)
            self.level = self.level + 1
            if(self.level > 99):
                self.experience = 0
            self.energy = self.energy + 2
            self.maxEnergy = self.maxEnergy + 2
            self.hitpoints = self.hitpoints + 10
            self.maxHitpoints = self.maxHitpoints + 10
            self.statPoints = self.statPoints + 2
            for i in range(len(self.stats)):
                self.stats[i] = self.stats[i] + 0.5
    
    #All things related to self.hitpoints
    def getHitpoints(self):
        return self.hitpoints
    
    def updateHitpoints(self):
        if self.hitpoints > self.maxHitpoints:
            self.hitpoints = self.maxHitpoints
    
    #def poisioned or damage over time?
    
    def getHit(self, damage): #certain floors, some aspect gets doubled for that floor
        num = random.random() * 650
        #defense
        blockMultiplier = self.stats[0] / 650
        damage = damage * (1 - blockMultiplier)
        #evasiveness
        if self.stats[1] >= num:
            damage = 0
        self.hitpoints = self.hitpoints - damage


    def zeroHealth(self):
        self.experience = 0
        self.hitpoints = self.maxHitpoints
        self.energy = self.maxEnergy
        numOfDays.addDays(3)
    
    def changeHitpoints(self, num):
        self.hitpoints = self.hitpoints + num
        return Character.updateHitpoints(self)

    #All things related to maxHitpoints
    def getMaxHitpoints(self):
        return self.maxHitpoints

    def changeMaxHitPoints(self, num):
        self.maxHitpoints = self.maxHitpoints + num
    
    #All things related to energy
    def getEnergy(self):
        return self.energy

    def changeEnergy(self, num):
        self.energy = self.energy + num
    
    def checkEnergy(self):
        if self.energy <= 0:
            self.energy = self.maxEnergy
            damage = Character.getMaxHitpoints() / 2
            Character.getHit(damage)
            if self.hitpoints <= 0:
                self.hitpoints = 1

    #All things related to maxEnergy
    def getMaxEnergy(self):
        return self.maxEnergy
        
    def changeMaxEnergy(self, num):
        self.maxEnergy = self.maxEnergy + num

    #All things related to experience
    def getExperience(self):
        return self.experience
    
    def expToNextLevel(self):
        return int(self.level * self.level/2 * 100 * (1 + self.expPoints/100))

    def addExperience(self):
        #idunno, 500 per thingy???
        self.experience = int(self.experience + 50 * self.level * self.level/2)
        if(self.level > 99):
            self.experience = 0
        return Character.levelUp(self)

    #All things related to Stats
    def getStats(self):
        return self.stats
    
    def sendAttack(self):
        num = random.random() * 289
        damage = self.stats[3]
        critMultiplier = 1.5 + (self.stats[5] / 260)
        if(self.stats[4] >= num):
            damage = damage * critMultiplier
        damage = damage + (self.stats[5] / 5)
        return damage

    #All things related to Statpoints
    def getStatPoints(self):
        return self.statPoints

    def changeStatPoints(self, num):
        self.statPoints = self.statPoints + num
    
    #All things related to Days
    def getDays(self):
        return numOfDays.getDays()
    
    def addDays(self, num):
        return numOfDays.addDays(num)
    
    def newCharacter():
        return Character(1,100,100,10,10,0,Character_Data.CharacterStats.baseStats,0,0)