from ics import Calendar, Event
from urllib.request import urlopen
import tund

def createEventList(url):
    timeFormat = "HH:mm" #Default time format
    timeFormat2 = "DD/MM/YYYY"
    c = Calendar(urlopen(url).read().decode('iso-8859-1'))

    '''if len(c.events) <= 0:
        view.printSomeError(error) #TODO Kui calender tuhi voi muu error.
        ...'''
    
    for event in c.events:
        print(event.name + " " + event.begin.format(timeFormat) + " " +event.begin.format(timeFormat2) + " WEEKDAY:" + str(event.begin.weekday()))
        tund.Tund(event.name, event.location, event.begin.weekday(), event.begin.format(timeFormat), event.description, event.begin.format(timeFormat2), 'red')
