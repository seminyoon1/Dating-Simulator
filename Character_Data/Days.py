class Days():
    def __init__(self, days):
        self.days = days
    
    def addDays(self, num, energy):
        self.days = self.days + (num * (200 - energy) / 200)
    
    def getDays(self):
        return self.days
    
    def setDays(self, num):
        self.days = num
    
    def resetDays(self):
        self.days = 0

    def newDays():
        return Days(0)
