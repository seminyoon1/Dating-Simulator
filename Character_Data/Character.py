from pstats import Stats


class Character():

    def __init__(self, level, hitpoints, energy, experience, stats, statPoints):
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
        self.energy = energy
        self.experience = experience
        self.stats = stats
        self.statPoints = statPoints

    def expToNextLevel(self):
        return int(self.level * self.level/2 * 100)

    def levelUp(self):
        while(self.experience >= Character.expToNextLevel(self)):
            self.level = self.level + 1
            self.experience = self.experience - Character.expToNextLevel(self)
            self.statPoints = self.statPoints + 2
            for i in range(len(self.stats)):
                self.stats[i] = self.stats[i] + 1
        return self.level, self.experience
    
me = Character(1,1,1,1000,[1,1,1,1,1,1],1)
print(me.levelUp())
print(me.expToNextLevel())
