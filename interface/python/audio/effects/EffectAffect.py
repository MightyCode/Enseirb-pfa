from interface.python.Tweenings.Tweening import Tweening
from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
from interface.python.Tweenings.ETweeningType import ETweeningType as ETT

from interface.python.audio.ModelAudioEffect import ModelAudioEffect

class AffectFunction:
    def add(a, b) : return a + b
    def sub(a, b) : return a - b
    def rsub(a, b) : return b - a
    def mul(a, b) : return a * b
    def div (a, b) : return a / b
    def rdiv(a, b) : return b / a

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

        if now < 0 or now > self.getLength():
            return value

        return self.func(value, self.subModel.computeValue(startTime, tick, value, speakerId, isLeft))

    def getLength(self):
        return self.length