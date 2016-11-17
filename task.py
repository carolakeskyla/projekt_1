

class Task:

    staticVar = 5

    def __init__(self, ajakulu, finishTime, priority, color):
        self.ajakulu = ajakulu
        self.finishTime = finishTime
        self.priority = priority
        self.color = color

    def otsiVabadAjad(self):
        listOfFreeTimes = []

        
        
