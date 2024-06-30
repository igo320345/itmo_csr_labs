import requests
from models.event import Event

class EventService():
    def __init__(self):
        self.__responce = requests.get('https://date.nager.at/api/v2/publicholidays/2023/RU').json()
    
    def getEvents(self):
        events = []
        for value in  self.__responce:
            event = Event(value['localName'], value['date'])
            events.append(event)
        return events
