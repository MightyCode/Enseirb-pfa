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

    def str_to_affect_function(func_name: str):
        if hasattr(AffectFunction, func_name):
            return getattr(AffectFunction, func_name)
        else:
            raise ValueError(f"Function {func_name} not found in AffectFunction")

class Effect2Merge(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self._func: function = AffectFunction.add

    def preprocess(self):
        super().preprocess()

        number_second = float(self.info["length"])
        self._length = round(number_second * self._sampleRate)
        self._func =  AffectFunction.str_to_affect_function(self.info["func"])

    def set_audio_stream_id(self, streamsInId, streamOutId):
        assert len(streamsInId) == 2
        assert streamOutId != None and len(streamOutId) != 0

    def compute_value(self, startTime, tick, audioStreams):
        now: int = tick - startTime

        assert now >= 0 or now < self._length()

        return [
            self._func(audioStreams[0].left_value(), audioStreams[1].right_value()),
            self._func(audioStreams[0].left_value(), audioStreams[1].right_value())
        ]

    @staticmethod
    def Instanciate():
        return Effect2Merge()

    @staticmethod
    def GetEffectName():
        return "2merge"