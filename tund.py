

class Tund:

    tunnid = []#Koosneb kõigist tundidest.
    
    def __init__(self, lessonName, location, beginDateTime, endDateTime, color):
        self.lessonName = lessonName
        self.location = location
        self.beginDateTime = beginDateTime #Formaat YYYY-MM-dd HH:mm:ss
        self.endDateTime = endDateTime
        self.color = color

        Tund.tunnid.append(self)


    def getBeginDate(self):
        return self.beginDateTime.split()[0] #Formaat YYYY-MM-dd

    def getBeginTime(self):
        return self.beginDateTime.split()[1] #Formaat HH:mm:ss

    def getEndDate(self):
        return self.endDateTime.split()[0] #Formaat YYYY-MM-dd

    def getEndTime(self):
        return self.endDateTime.split()[1] #Formaat HH:mm:ss
    
