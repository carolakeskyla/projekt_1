

class Tund:

    tunnid = []#Koosneb kõigist tundidest.
    
    def __init__(self, lessonName, location, weekday, time, description, date, color):
        
        lName = lessonName.split()
        lessonName = ""
        for s in lName:
            if s.count(".") == 2:
                break
            lessonName += s + " "
        self.lessonName = lessonName

        self.date = date
        self.location = location
        self.weekday = weekday
        self.time = time
        self.color = color
        
        self.description = description
        Tund.tunnid.append(self)

    def getLessonName(self):
        return self.lessonName

    def getLocation(self):
        return self.location

    def getDescription(self):
        return self.description

    def getDate(self):
        return self.date
    
    def getWeekday(self):
        return self.weekday

    def getTime(self):
        return self.time
    
    def getColor(self):
        return self.color

