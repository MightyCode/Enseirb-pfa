from interface.python.Tweenings.Tweening import Tweening
from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
from interface.python.Tweenings.ETweeningType import ETweeningType as ETT

from interface.python.audio.ModelAudioEffect import ModelAudioEffect

import math

class AffectFunction:
    @staticmethod
    def add(a, b) : return a + b
    @staticmethod
    def sub(a, b) : return a - b
    @staticmethod
    def rsub(a, b) : return b - a
    @staticmethod
    def mul(a, b) : return a * b
    @staticmethod
    def div (a, b) : return a / b
    @staticmethod
    def rdiv(a, b) : return b / a
    @staticmethod
    def max(a, b) : return max(a, b)
    @staticmethod
    def min(a, b) : return min(a, b)
    @staticmethod
    def mean(a, b) : return (a + b) / 2
    @staticmethod
    def dist(a, b) : return math.sqrt(a * a + b * b)

    def str_to_affect_function(funcName: str):
        if hasattr(AffectFunction, funcName):
            return getattr(AffectFunction, funcName)
        else:
            raise ValueError(f"Function {funcName} not found in AffectFunction")

class EffectAffect(ModelAudioEffect):
    def __init__(self, speakerGroup, subModelAudioEffect: ModelAudioEffect):
        super().__init__(speakerGroup)

        self.func: function = AffectFunction.add
        self.subModel: ModelAudioEffect = subModelAudioEffect
        self.length: int = 0

    def preprocess(self):
        self.subModel.preprocess()
        self.length = self.subModel.getLength()
        self.func =  AffectFunction.str_to_affect_function(self.info["affect"])

    def computeValue(self, startTime, tick, value, speakerId, isLeft):
        now: int = tick - startTime

        if now < 0 or now >= self.getLength():
            return value

        return self.func(value, self.subModel.computeValue(startTime, tick, value, speakerId, isLeft))

    def getLength(self):
        return self.length

    @staticmethod
    def Instanciate(soundCreation, speakerGroup, modelEffectInfo, projectInfo):
        subEffect = soundCreation.createEffectFromName(speakerGroup, modelEffectInfo["subModel"], projectInfo)
        return EffectAffect(speakerGroup, subEffect)

    @staticmethod
    def GetEffectName():
        return "affect"