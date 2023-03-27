from interface.python.Tweenings.Tweening import Tweening
from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
from interface.python.Tweenings.ETweeningType import ETweeningType as ETT

from interface.python.audio.ModelAudioEffect import ModelAudioEffect

class EffectAmplitudeTweening(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.tweeningType = -1
        self.tweeningBehaviour = -1

        self.minValue = 0
        self.maxValue = 0

        self.delta = 0

        # Optionnal, depend of tweening type
        self.arg1 = None
        self.arg2 = None

        self.length = 0

    def preprocess(self):
        self.samplerate = int(self.info["sampleRate"])
        self.tweeningType = ETT.from_str(self.info["tweeningType"])
        self.tweeningBehaviour = ETB.from_str(self.info["tweeningBehaviour"])

        self.minValue = float(self.info["minValue"]) if "minValue" in self.info.keys() else 0
        self.maxValue = float(self.info["maxValue"]) if "maxValue" in self.info.keys() else 1

        self.delta = self.maxValue - self.minValue

        if "arg1" in self.info.keys():
           self.arg1 = float(self.info["arg1"])
    
        if "arg2" in self.info.keys():
           self.arg2 = float(self.info["arg2"])

        self.numberSeconds = int(self.info["length"])
        self.length = int(self.numberSeconds * self.samplerate)

    def computeValue(self, startTime, tick, value, speakerId, speakerGroup, isLeft):
        now: int = tick - startTime

        #print(now, Tweening.evaluate(self.tweeningType, self.tweeningBehaviour, now, self.minValue, self.delta, self.length, self.arg1, self.arg2))
        return value * Tweening.evaluate(self.tweeningType, self.tweeningBehaviour, now, self.minValue, self.delta, self.length, self.arg1, self.arg2)

    def getLength(self):
        return self.length