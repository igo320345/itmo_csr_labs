from services.event_service import EventService
from datetime import datetime


class EventUsecase():
    def __init__(self):
        service = EventService()
        self.__events = service.getEvents()

    def getEventNames(self):
        return [event.localName for event in self.__events]
    
    def saveEventFile(self):
        file = open('event_names.txt', 'w')
        for event in self.__events:
            file.write(event.localName + '\n')
        file.close()

    def nearestEvent(self):
        userDate = datetime.now()
        min = 367
        nearest = 'Не обнаружено'
        for event in self.__events:
            eventDate = datetime.strptime(event.date, '%Y-%m-%d')
            distance = eventDate - userDate
            if distance.days > 0 and distance.days < min:
                min = distance.days
                nearest = event.localName
        return nearest

    def countEvents(self):
        return str(len(self.__events))