from interface.python.Tweenings.Tweening import Tweening
from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
from interface.python.Tweenings.ETweeningType import ETweeningType as ETT

from interface.python.audio.ModelAudioEffect import ModelAudioEffect

import copy

class EffectAmplitudeTweening(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.tweeningType = -1
        self.tweeningBehaviour = -1

        self.startValue = 0
        self.maxValue = 0

        self.delta = 0

        # Optionnal, depend of tweening type
        self.arg1 = None
        self.arg2 = None

        self.length = 0

        self.result: list = []

    def preprocess(self):
        super().preprocess()

        self.tweeningType = ETT.from_str(self.info["tweeningType"])
        self.tweeningBehaviour = ETB.from_str(self.info["tweeningBehaviour"])

        self.startValue = float(self.info["startValue"]) if "startValue" in self.info.keys() else 0
        self.endValue = float(self.info["endValue"]) if "endValue" in self.info.keys() else 1

        self.delta = self.endValue - self.startValue

        if "arg1" in self.info.keys():
           self.arg1 = float(self.info["arg1"])
    
        if "arg2" in self.info.keys():
           self.arg2 = float(self.info["arg2"])

        self.numberSeconds = float(self.info["length"])
        self.length = round(self.numberSeconds * self.sampleRate)

    def setAudioStreamId(self, streamsInId, streamOutId):
        assert len(streamsInId) == len(streamOutId) and len(streamOutId) != 0

        for i in range(len(streamOutId)):
            self.result.append([0, 0])

    def computeValue(self, startTime, tick, audioStreams):
        now: int = tick - startTime

        assert now >= 0 or now < self.getLength()

        for audioStream, i in zip(audioStreams, range(len(audioStreams))):
            amplitude = Tweening.evaluate(self.tweeningType, self.tweeningBehaviour, now, self.startValue, self.delta, self.length, self.arg1, self.arg2)
            self.result[i][0] = audioStream.leftValue() * amplitude 
            self.result[i][1] = audioStream.rightValue() * amplitude 
    
        return copy.deepcopy(self.result) 

    @staticmethod
    def Instanciate():
        return EffectAmplitudeTweening()

    @staticmethod
    def GetEffectName():
        return "amplitudeTweening"