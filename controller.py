from ics import Calendar, Event
from urllib.request import urlopen
import tund

#def getDate(time):
    #return time.strptime(time, '%Y-%m-%dT%H:%M:%S')

url = "http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=2003546243"

c = Calendar(urlopen(url).read().decode('iso-8859-1'))
timeFormat = "YYYY-MM-DD HH:mm:ss" 

for event in c.events:
    print(event.name + " " + event.begin.format(timeFormat))
    

'''
class Controller:

    def __init__(self, view):
        self.view = view
    
    def createEvents(self):
        url = view.getUrl()
        
        timeFormat = "YYYY-MM-DD HH:mm:ss" #Default time format
        
        if len(c.events) <= 0:
            view.printSomeError(error)
            ...
        

        
        for event in c.events:
            tund.Tund(event.name, event.location, event.begin.format(timeFormat), event.end.format(timeFormat), 0) #Creating objects.
            




events = getEventsList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=1228100092")
if(events == False):
    handle error...'''

