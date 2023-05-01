from interface.python.Tweenings.Tweening import Tweening
from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
from interface.python.Tweenings.ETweeningType import ETweeningType as ETT

from interface.python.audio.ModelAudioEffect import ModelAudioEffect

class EffectAmplitudeTweening(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self._tweening_type: int = -1
        self._tweening_behaviour: int = -1

        self._start_value: int = 0
        self._max_value: int = 0

        self._delta: int = 0

        # Optionnal, depend of tweening type
        self._optional_arg_1: int = None
        self._optional_arg_2: int = None

        self._result: list = []

    def preprocess(self):
        super().preprocess()

        self._tweening_type = ETT.from_str(self.info["tweeningType"])
        self._tweening_behaviour = ETB.from_str(self.info["tweeningBehaviour"])

        self._start_value = float(self.info["startValue"]) if "startValue" in self.info.keys() else 0
        self.endValue = float(self.info["endValue"]) if "endValue" in self.info.keys() else 1

        self._delta = self.endValue - self._start_value

        if "arg1" in self.info.keys():
           self._optional_arg_1 = float(self.info["arg1"])
    
        if "arg2" in self.info.keys():
           self._optional_arg_2 = float(self.info["arg2"])

        numberSeconds: float = float(self.info["length"])
        self._length = round(numberSeconds * self._sampleRate)

    def set_audio_stream_id(self, streamsInId, streamOutId):
        assert len(streamsInId) == len(streamOutId) and len(streamOutId) != 0

        self._result = []
        for i in range(len(streamOutId)):
            self._result.append([0, 0])

    def compute_value(self, startTime, tick, audioStreams):
        now: int = tick - startTime

        assert now >= 0 or now < self._length()

        for audioStream, i in zip(audioStreams, range(len(audioStreams))):
            amplitude = Tweening.evaluate(self._tweening_type, self._tweening_behaviour, now, self._start_value, self._delta, self._length, self._optional_arg_1, self._optional_arg_2)
            self._result[i][0] = audioStream.left_value() * amplitude 
            self._result[i][1] = audioStream.right_value() * amplitude 
    
        return self._result

    @staticmethod
    def Instanciate():
        return EffectAmplitudeTweening()

    @staticmethod
    def GetEffectName():
        return "amplitudeTweening"