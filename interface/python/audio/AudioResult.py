class AudioResult:
    def __init__(self, nb_speakers, samplerate, length):
        self.nb_speakers = nb_speakers
        self.samplerate = samplerate
        self.length = length

        self.data = [0] * nb_speakers

        for i in range(nb_speakers):
            self.data[i] = [0] * samplerate * length

        self.blocks_generator = [0] * nb_speakers

    def process(main_sound):
        pass

    def generate_block():
        for i in range(self.nb_speakers):
            self.blocks_generator[i] = 0