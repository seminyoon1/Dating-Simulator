import Character_Data.CharacterStats

class Character():

    def __init__(self, level, hitpoints, maxHitpoints, energy, maxEnergy, experience, stats, statPoints):
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

    #handling exp stat boosts for experience
    expPoints = Character_Data.CharacterStats.expPoints

    #All things relating to self.level
    def getLevel(self):
        return self.level
    
    def levelUp(self):
        while(self.experience >= Character.expToNextLevel(self) and self.level < 100):
            self.experience = self.experience - Character.expToNextLevel(self)
            self.level = self.level + 1
            if(self.level > 99):
                self.experience = 0
            self.energy = self.energy + 3
            self.maxEnergy = self.maxEnergy + 3
            self.hitpoints = self.hitpoints + 5
            self.maxHitpoints = self.maxHitpoints + 5
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
    
    def getHit(self, damage):
        #might need days here to run?
        if (self.hitpoints - damage) <= 0:
            return Character.zeroHealth(self)
        self.hitpoints = self.hitpoints - damage

    def zeroHealth(self): # include days in the function params?
        #insert screen here to show death and reset
        self.experience = 0
        self.hitpoints = self.maxHitpoints
        self.energy = self.maxEnergy
        #add 3 days, need some import thingy
    
    def addHitpoints(self, num):
        self.hitpoints = self.hitpoints + num
        return Character.updateHitpoints(self)

    #All things related to maxHitpoints
    def getMaxHitpoints(self):
        return self.maxHitpoints

    #All things related to experience
    def getExperience(self):
        return self.experience
    
    def expToNextLevel(self):
        return int(self.level * self.level/2 * 100)

    
    def addExperience(self):
        #idunno, 500 per thingy???
        self.experience = self.experience + 5000 * self.level
        if(self.level > 99):
            self.experience = 0
        return Character.levelUp(self)
    
    def newCharacter():
        return Character(1,100,100,10,10,0,Character_Data.CharacterStats.baseStats,0)

