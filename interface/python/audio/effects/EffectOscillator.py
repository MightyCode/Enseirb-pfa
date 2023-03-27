from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

import numpy as np

class EffectOscillator(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.freq = 440.0  # frequency in Hz
        self.amp = 0.5  # amplitude between 0 and 1

        self.length = 0
        self.amplitude = 0.5

    def preprocess(self):
        self.samplerate = int(self.info["sampleRate"])
        self.freq = float(self.info["frequency"])

        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1
        self.numberSecond = float(self.info["length"])
        self.length = int(self.numberSecond * self.samplerate)

        t = np.linspace(0, self.numberSecond, int(self.length), endpoint=False)

        # create the oscillator waveform
        self.osc = self.amplitude * np.sin(2 * np.pi * self.freq * t)
        
    def computeValue(self, startTime, tick, value, speakerId, speakerGroup, isLeft):
        now = tick - startTime

        if now < 0 or now > self.getLength():
            return value

        return self.osc[now]

    def getLength(self):
        return self.length