

class Tund:

    tunnid = []#Koosneb kõigist tundidest.
    
    def __init__(self, lessonName, location, weekday, time, color):
        
        lastTwoLetters = [lessonName[0], lessonName[1]]
        breakPoint = None
        for i in range(2, len(lessonName)):
            if lessonName[i].isupper():
                if lastTwoLetters[0].isupper() and lastTwoLetters[1].isupper():
                    breakPoint = i-2
        
        if breakPoint == None:
            self.lessonName = lessonName
        else:
            self.lessonName = lessonName[:breakPoint]

        self.location = location
        self.weekday = weekday
        self.time = time
        self.color = color
        Tund.tunnid.append(self)

    def getLessonName(self):
        return self.lessonName
    
    def getWeekday(self):
        return self.weekday

    def getTime(self):
        return self.time
    
    def getColor(self):
        return self.color

