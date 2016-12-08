import tund
from random import randint

class Task:

    tasks = []
    
    def __init__(self, name, ajakulu, finishTime, timeSteps, priority, color):
        self.ajakulu = ajakulu #minutites int
        self.finishTime = finishTime
        self.timeSteps = timeSteps #15,30,45,60 int
        self.priority = priority
        self.color = color
        self.timesList = otsiVabadAjad()#Formaat list[] HH:mm
        Task.tasks(self)
    
    def getAjakulu(self):
        return self.ajakulu
    
    def getName(self):
        return self.name
    
    def getFinishTime(Self):
        return self.finishTime
    
    def otsiVabadAjad(self):
        steps = []
        a = self.ajakulu / self.timeSteps
        if self.ajakulu % self.timeSteps == 0:
            for i in range(int(a)):
                rand = randint(10, 23)
                ...
        else:
            a = int(a)
            for i in range(a):
                rand = randint(10,18)
                time = str(rand) + ":" + str(self.timeSteps)
                ...
    def checkIfTimeConflicts(self, time):        
        for t in tund.Tund.tunnid:
                h,s = t.getTime().split(":")
                for i in range(3):#15 minutit * 6 = 1h 30min tund
                    if (h + ":" + str(int(s) + 15*i)) == time:
                        return True
                if str(int(h)+1) + ":00" == time:
                    return True
                for i in range(3):
                    if (str(int(h)+1) + ":" + str(int(s) + 15*i)) == time:
                        return True
        return False
        
        
        
            
            

        
        
