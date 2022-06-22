import random

class Enemy():

    def __init__(self, hitpoints, maxHitpoints, stats):
        """ For viewing purposes only
        stats:
        defense = stats[0]
        evasiveness = stats[1]
        intelligence = stats[2]
        attack = stats[3]
        critical = stats[4]
        power = stats[5]  
        """
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.stats = stats

    #All things related to self.hitpoints
    def getHitpoints(self):
        return self.hitpoints
    
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
        #if self.hitpoints <= 0:
        #    return Enemy.zeroHealth(self)

    #All things related to maxHitpoints
    def getMaxHitpoints(self):
        return self.maxHitpoints

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

    #def newCharacter():
    #    return Enemy(1,100,100,10,10,0,Character_Data.CharacterStats.baseStats,0,0)