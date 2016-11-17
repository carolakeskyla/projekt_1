from ics import Calendar, Event
from urllib.request import urlopen
import tund

    
class Controller:

    def __init__(self, view):
        self.view = view
    
    #V
    def getEventsFromUrl(self):
        url = view.getUrl()
        timeFormat = "YYYY-MM-DD HH:mm:ss" #Default time format
        c = Calendar(urlopen(url).read().decode('iso-8859-1'))
        
        if len(c.events) <= 0:
            view.printSomeError(error)
            ...
            
        for event in c.events:
            tund.Tund(event.name, event.location, event.begin.format(timeFormat), event.end.format(timeFormat), 0) #Creating objects.
            
      
        


events = getEventsList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=1228100092")
if(events == False):
    handle error...

