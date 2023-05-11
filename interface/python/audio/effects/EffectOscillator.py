from interface.python.audio.effects.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

import numpy as np

class EffectOscillator(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self._freq: float = 440.0  # frequency in Hz
        self._amplitude = 0.5 # amplitude between 0 and 1
        self.oscillations: list = []

    def preprocess(self):
        super().preprocess()

        self._freq = float(self.info["frequency"])

        self._amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1

        number_second = float(self.info["length"])
        self._length = round(number_second * self._sampleRate)

        t = np.linspace(0, number_second, int(self._length), endpoint=False)

        # create the oscillator waveform
        self.oscillations = self._amplitude * np.sin(2 * np.pi * self._freq * t)
    
    def set_audio_stream_id(self, streams_in_id, stream_out_id):
        assert stream_out_id != None and len(stream_out_id) != 0

    def compute_value(self, start_time: int, tick: int, audio_streams: list):
        now = tick - start_time

        assert now >= 0 or now < self.length()

        return self.oscillations[now]

    @staticmethod
    def Instanciate():
        return EffectOscillator()

    @staticmethod
    def Get_effect_name():
        return "oscillator"