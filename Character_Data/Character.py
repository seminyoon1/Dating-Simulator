
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

    def getLevel(self):
        return self.level
    
    def expToNextLevel(self):
        return int(self.level * self.level/2 * 100)

    def levelUp(self):
        while(self.experience >= Character.expToNextLevel(self) and self.level < 100):
            self.experience = self.experience - Character.expToNextLevel(self)
            self.level = self.level + 1
            self.energy = self.energy + 3
            self.maxEnergy = self.maxEnergy + 3
            self.hitpoints = self.hitpoints + 5
            self.maxHitpoints = self.maxHitpoints + 5
            self.statPoints = self.statPoints + 2
            for i in range(len(self.stats)):
                self.stats[i] = self.stats[i] + 1
    
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
    
    def getExperience(self):
        #idunno, 500 per thingy???
        self.experience = self.experience + 50
        return Character.levelUp(self)
    
    def newCharacter():
        return Character(1,100,100,10,10,0,[10,10,10,10,10,10],0)

