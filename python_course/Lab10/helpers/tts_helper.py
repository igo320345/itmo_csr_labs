import pyttsx3

class TTSHelper():
    def __init__(self):
        #Works only on MacOS, change driver for another OS
        self.__engine = pyttsx3.init('nsss')
        self.__engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yuri')

    def say(self, text):
        self.__engine.say(text)
        self.__engine.runAndWait()