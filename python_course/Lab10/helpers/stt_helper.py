from vosk import Model, KaldiRecognizer
import json
import pyaudio

class STTHelper():
    def __init__(self):
        model = Model('vosk-model-small-ru-0.4')
        p = pyaudio.PyAudio()
        self.__stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=16000
        )
        self.__stream.start_stream()
        self.__rec = KaldiRecognizer(model, 16000)

    def recognize(self):
        while True:
            data = self.__stream.read(4000, exception_on_overflow=False)
            if (self.__rec.AcceptWaveform(data)) and (len(data) > 0):
                command = json.loads(self.__rec.Result())
                if command['text']:
                    yield command['text']
    