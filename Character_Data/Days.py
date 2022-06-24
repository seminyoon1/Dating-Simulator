class Days():
    def __init__(self, days):
        self.days = days
    
    def addDays(self, num):
        self.days = self.days + num
    
    def getDays(self):
        return self.days
    
    def resetDays(self):
        self.days = 0

    def newDays():
        return Days(0)
