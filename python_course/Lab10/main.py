from helpers.stt_helper import STTHelper
from helpers.tts_helper import TTSHelper
from usecases.event_usecase import EventUsecase

stt = STTHelper()
tts = TTSHelper()
usecase = EventUsecase()

for text in stt.recognize():
    if text == 'перечисли названия праздников':
        events = usecase.getEventNames()
        for event in events:
            tts.say(event)
    elif text == 'сохрани названия праздников в файл':
        usecase.saveEventFile()
        tts.say('сохранил названия праздников в файл')
    elif text == 'назови ближайший праздник':
        tts.say(usecase.nearestEvent())
    elif text == 'назови количество праздников':
        tts.say(usecase.countEvents())
    else:
        tts.say('не понимаю, что вы говорите')
