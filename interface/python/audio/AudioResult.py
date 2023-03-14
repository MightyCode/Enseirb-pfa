class AudioResult:
    def __init__(self, nb_speakers, samplerate, length):
        self.nb_speakers = nb_speakers
        self.samplerate = samplerate
        self.length = length

        self.data = [0] * nb_speakers

        for i in range(nb_speakers):
            self.data[i] = [0] * samplerate * length

        self.blocks_generator = [0] * nb_speakers

        self.blockAdvancement = 0

    def getNumberTick(self):
        return int(self.samplerate * self.length)

    def generate_block(self):
        for i in range(self.nb_speakers):
            self.blocks_generator[i] = 0

    def getAudioValue(self, id_speaker, tick):
        return self.data[id_speaker][tick]


    def setAudioValue(self, id_speaker, tick, value):
        self.data[id_speaker][tick] = value