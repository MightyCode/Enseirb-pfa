import numpy as np

class AudioResult:
    def __init__(self, nb_speakers, samplerate, length):
        self.nb_speakers = nb_speakers
        self.samplerate = samplerate
        self.length = length

        #Stereo
        self.data = [0] * nb_speakers * 2

        for i in range(nb_speakers * 2):
            self.data[i] = [0] * length

        self.data = np.asarray(self.data, dtype=float)

        self.blockAdvancement = 0

    def get_number_tick(self):
        return int(self.length)

    def generate_block(self):
        for i in range(self.nb_speakers):
            self.blocks_generator[i] = 0

    def get_audio_value(self, id_speaker, tick, isLeft=False):
        index = id_speaker * 2 if isLeft else id_speaker * 2 + 1

        return self.data[index][tick]


    def set_audio_value(self, id_speaker, tick, value, isLeft=False):
        index = (id_speaker * 2) if isLeft else (id_speaker * 2 + 1) 

        self.data[index][tick] = value