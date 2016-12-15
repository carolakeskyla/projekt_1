import tund
from random import randint

class Task:

    tasks = []
    currentTask = None #Really bad....
    
    def __init__(self, name, ajakulu, finishTime, timeSteps):
        self.name = name
        self.ajakulu = ajakulu #minutites int
        self.finishTime = finishTime
        self.timeSteps = timeSteps #30,60,90,120 int
        #self.priority = priority
        self.timesList = self.otsiVabadAjad()#Formaat list[] D:HH:mm
        Task.tasks.append(self)
        print(self.timesList)

    def getTimeSteps(self):
        return self.timeSteps

    def getAjakulu(self):
        return self.ajakulu
    
    def getName(self):
        return self.name
    
    def getFinishTime(self):
        return self.finishTime

    def getTimesList(self):
        return self.timesList

    def otsiVabadAjad(self):
        steps = []
        a = self.ajakulu / self.timeSteps
        print(a)
        if self.ajakulu % self.timeSteps == 0:
            for i in range(int(10)):
                rand = randint(10, 23)
                rand2 = randint(1, 2)
                randDay = randint(1, 7)
                if rand2 == 1:
                    rand2 = 15
                else:
                    rand2 = 45
                time1 = str(rand) + ":" + str(rand2)
                if(self.checkIfTimeConflicts(str(rand) + ":" + str(rand2), randDay)):
                    print(time1 + "-CONFLICTS")
                    i -= 1
                    continue
                if(self.checkIfTimeConflicts(self.addMinutesToTime(time1, self.ajakulu), randDay)):
                    print(time1 + "-CONFLICTS AT " + str(self.ajakulu) + " at " + self.addMinutesToTime(time1, self.ajakulu))
                    i -= 1
                    continue
                steps.append([randDay,time1])
        else:
            pass
            #a = int(a)
            #for i in range(a):
                #rand = randint(10,18)
                #time = str(rand) + ":" + str(self.timeSteps)
                #...
        return steps
    
    def checkIfTimeConflicts(self, time, day):
        for t in tund.Tund.tunnid:
            if t.getWeekday() == day:
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

    def addMinutesToTime(self, time, minutes):
        h,m = time.split(":")
        time1 = int(h)*60 + int(m)
        time2 = time1 + minutes
        h = int(time2/60)
        m = time2 - (h*60)
        return str(h) + ":" + str(m)  
