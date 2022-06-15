""" 
        stats:
        defense = stats[0]
        evasiveness = stats[1]
        intelligence = stats[2]
        attack = stats[3]
        power = stats[4]
        critical = stats[5]  
        """

#This is for a new game, base stats
baseStats = [10, 10, 10, 10, 10, 10]
expPoints = 0

def addDefense(maxHitpoints, maxEnergy, stats):
        stats[0] = stats[0] + 1
        stats[2] = stats[2] + 0.2
        maxHitpoints = maxHitpoints + 5
        maxEnergy = maxEnergy - 0.4
        return maxHitpoints, maxEnergy, stats

def addEvasiveness(maxEnergy, stats):
        stats[1] = stats[1] + 1
        stats[0] = stats[0] + 0.2
        maxEnergy = maxEnergy - 0.4
        return maxEnergy, stats

def addIntelligence(maxEnergy, expPoints, stats):
        stats[2] = stats[2] + 1
        stats[1] = stats[1] + 0.2
        stats[5] = stats[5] + 0.2
        maxEnergy = maxEnergy + 0.4
        expPoints = expPoints + 1
        return maxEnergy, stats

def addAttack(maxEnergy, stats):
        stats[3] = stats[3] + 1
        stats[4] = stats[4] + 0.2
        stats[5] = stats[5] + 0.2
        maxEnergy = maxEnergy - 0.4
        return maxEnergy, stats

def addPower(maxEnergy, stats):
        stats[4] = stats[4] + 1
        stats[3] = stats[3] + 0.2
        stats[1] = stats[1] - 0.2
        maxEnergy = maxEnergy + 0.4
        return maxEnergy, stats

def addCritical(maxEnergy, stats):
        stats[5] = stats[5] + 1
        stats[3] = stats[3] + 0.2
        stats[4] = stats[4] + 0.2
        maxEnergy = maxEnergy + 0.4
        return maxEnergy, stats
