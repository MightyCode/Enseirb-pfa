from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectPlay(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.samplerate = 0
        self.length = 0

    def preprocess(self):
        self.samplerate = int(self.info["sampleRate"])
        self.length = int(self.numberSecond * self.samplerate)
    
    def computeValue(self, startTime, tick, value, speakerId, speakerGroup, isLeft):
        now = tick - startTime

        if now < 0 or now > self.getLength():
            return value

        return 0

    def getLength(self):
        return self.length