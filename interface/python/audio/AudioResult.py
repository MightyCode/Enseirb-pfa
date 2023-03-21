import numpy as np

class AudioResult:
    def __init__(self, nb_speakers, samplerate, length):
        self.nb_speakers = nb_speakers
        self.samplerate = samplerate
        self.length = length

        #Stereo
        self.data = [0] * nb_speakers * 2

        for i in range(nb_speakers * 2):
            self.data[i] = [0] * samplerate * length

        self.data = np.asarray(self.data)

        self.blockAdvancement = 0

    def getNumberTick(self):
        return int(self.samplerate * self.length)

    def generate_block(self):
        for i in range(self.nb_speakers):
            self.blocks_generator[i] = 0

    def getAudioValue(self, id_speaker, tick, isLeft=False):
        return self.data[id_speaker * 2][tick] if isLeft else self.data[id_speaker * 2 + 1][tick]


    def setAudioValue(self, id_speaker, tick, value, isLeft=False):
        self.data[(id_speaker * 2) if isLeft else (id_speaker * 2 + 1)][tick] = value