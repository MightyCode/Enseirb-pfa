import numpy as np

from interface.python.ResourceManager import ResourceManager

class AudioResult:
    PATH_AUDIO_FILE = "out/speaker"

    def __init__(self, nb_speakers, sample_rate, length):
        self._nb_speakers = nb_speakers
        self._sample_rate = sample_rate
        self._length = length

        #Stereo
        self.data = [0] * nb_speakers * 2

        for i in range(nb_speakers * 2):
            self.data[i] = [0] * length

        self.data = np.asarray(self.data, dtype=float)

    def get_number_tick(self):
        return int(self._length)

    def generate_block(self):
        for i in range(self._nb_speakers):
            self.blocks_generator[i] = 0

    def get_audio_value(self, id_speaker, tick, isLeft=False):
        index = id_speaker * 2 if isLeft else id_speaker * 2 + 1

        return self.data[index][tick]

    def set_audio_value(self, id_speaker, tick, value, isLeft=False):
        index = (id_speaker * 2) if isLeft else (id_speaker * 2 + 1) 

        self.data[index][tick] = value

    
    def load_data_from_resources(self, index):
        self.data = ResourceManager().get_audio(AudioResult.PATH_AUDIO_FILE + index + ".wav", self._sample_rate)