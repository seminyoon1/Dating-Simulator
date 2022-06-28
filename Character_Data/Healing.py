class Healing():

    def __init__(self, heal):
        self.heal = heal
    
    def addHeal(self, num):
        self.heal = self.heal + int(num /3)

    def getHeal(self):
        return self.heal
    
    def autoHeal(self, hitpoints, maxHitpoints, percent):
        percent = percent/100
        if (hitpoints <= maxHitpoints * percent):
            totalHeal = maxHitpoints - hitpoints
            if totalHeal > self.heal:
                hitpoints = hitpoints + self.heal
                self.heal = 0
            else:
                hitpoints = maxHitpoints
                self.heal = self.heal - totalHeal
        return hitpoints

    def newHeal():
        return Healing(0)