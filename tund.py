

class Tund:

    tunnid = []#Koosneb kõigist tundidest.
    
    def __init__(self, lessonName, location, weekday, time, color):
        self.lessonName = lessonName
        self.location = location
        self.weekday = weekday
        self.time = time
        self.color = color
        Tund.tunnid.append(self)


    def getWeekday(self):
        return self.weekday

    def getTime(self):
        return self.time
    
    def getColor(self):
        return self.color
