from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

import numpy as np

class EffectOscillator(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.freq = 440.0  # frequency in Hz
        self.amp = 0.5  # amplitude between 0 and 1

        self._length = 0
        self.amplitude = 0.5

    def preprocess(self):
        super().preprocess()

        self.freq = float(self.info["frequency"])

        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1
        self.numberSecond = float(self.info["length"])
        self._length = round(self.numberSecond * self._sampleRate)

        t = np.linspace(0, self.numberSecond, int(self._length), endpoint=False)

        # create the oscillator waveform
        self.osc = self.amplitude * np.sin(2 * np.pi * self.freq * t)
    
    def set_audio_stream_id(self, streamsInId, streamOutId):
        assert streamOutId != None and len(streamOutId) != 0

    def compute_value(self, startTime, tick, audioStreams):
        now = tick - startTime

        assert now >= 0 or now < self._length()

        return self.osc[now]

    @staticmethod
    def Instanciate():
        return EffectOscillator()

    @staticmethod
    def GetEffectName():
        return "oscillator"