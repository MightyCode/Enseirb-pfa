from interface.python.Tweenings.Tweening import Tweening
from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
from interface.python.Tweenings.ETweeningType import ETweeningType as ETT

from interface.python.audio.ModelAudioEffect import ModelAudioEffect

class EffectAmplitudeTweening(ModelAudioEffect):
    def __init__(self, speakerGroup):
        super().__init__(speakerGroup)

        self.tweeningType = -1
        self.tweeningBehaviour = -1

        self.startValue = 0
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

        self.startValue = float(self.info["startValue"]) if "startValue" in self.info.keys() else 0
        self.endValue = float(self.info["endValue"]) if "endValue" in self.info.keys() else 1

        self.delta = self.endValue - self.startValue

        if "arg1" in self.info.keys():
           self.arg1 = float(self.info["arg1"])
    
        if "arg2" in self.info.keys():
           self.arg2 = float(self.info["arg2"])

        self.numberSeconds = int(self.info["length"])
        self.length = int(self.numberSeconds * self.samplerate)

    def computeValue(self, startTime, tick, value, speakerId, isLeft):
        now: int = tick - startTime

        if now < 0 or now > self.getLength():
            return value

        return value * Tweening.evaluate(self.tweeningType, self.tweeningBehaviour, now, self.startValue, self.delta, self.length, self.arg1, self.arg2)

    def getLength(self):
        return self.length

    @staticmethod
    def Instanciate(soundCreation, speakerGroup, modelEffectInfo, projectInfo):
        return EffectAmplitudeTweening(speakerGroup)

    @staticmethod
    def GetEffectName():
        return "amplitudeTweening"