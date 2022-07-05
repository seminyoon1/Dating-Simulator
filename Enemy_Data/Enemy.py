import random

class Enemy():

    def __init__(self, hitpoints, maxHitpoints, stats, experience):
        self.hitpoints = hitpoints
        self.maxHitpoints = maxHitpoints
        self.stats = stats
        self.experience = experience

    #All things related to self.hitpoints
    def getHitpoints(self):
        return self.hitpoints
    
    #def poisioned or damage over time?
    
    def getHit(self, damage): 
        num = random.random() * 1000
        #defense
        blockMultiplier = self.stats[0] / 1000
        damage = damage * (1 - blockMultiplier)
        #evasiveness
        if self.stats[1] >= num:
            damage = 0
        self.hitpoints = self.hitpoints - damage
        if self.hitpoints <= 0:
            self.hitpoints = 0

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
    
    def sendExperience(self):
        return self.experience
    
    def getStatName(self, num):
        statDict = {
        0: "Defense",
        1: "Evasiveness",
        2: "Intelligence",
        3: "Attack",
        4: "Critical",
        5: "Power",
        }
        return statDict.get(num)

    def getNewEnemy(floor):
        #boss is 0% and 100%
        #4 types: normal: 75%, critical: 10%, tank: 10%, elite: 5%
        enemyType = random.random() * 100
        hitpoints = 40 + floor*5 + int(random.random() * (10 + floor))
        stats = []
        total = hitpoints
        for i in range(6):
            num = 5 + floor/3 + round((random.random() * floor/10), 1)
            stats.append(num)
            total = total + num
        if enemyType < 75:
            name = "Normal"
            experience = total
            return Enemy(hitpoints, hitpoints, stats, experience), name
        elif enemyType < 85:
            for i in range(len(stats)):
                stats[i] = round((stats[i] * 1.2) , 1)
            name = "Powered"
            experience = total * 1.25
            return Enemy(hitpoints, hitpoints, stats, experience), name
        elif enemyType < 95:
            hitpoints = int(hitpoints*1.5)
            name = "Tank"
            experience = total * 1.25
            return Enemy(hitpoints, hitpoints, stats, experience), name

        hitpoints = int(hitpoints*1.25)
        for i in range(len(stats)):
            stats[i] = round((stats[i] * 1.25), 1)
            name = "Elite"
        experience = total * 1.5
        return Enemy(hitpoints, hitpoints, stats, experience), name

    def getBoss(floor):
        hitpoints = 80 + floor*15 + int(random.random() * (10 + floor*2))
        stats = []
        total = hitpoints
        for i in range(6):
            num = 5 + round(floor/2 + (random.random() * floor/10), 1)
            stats.append(num)
            total = total + num
        experience = total * 1.875
        return Enemy(hitpoints, hitpoints, stats, experience)