from interface.python.audio.ModelAudioEffect import ModelAudioEffect

class EffectPlay(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.samplerate = 0
        self.soundFile = None

    def preprocess(self):
        self.samplerate = int(self.info["samplerate"])

        self.soundFile = self.resourceManager.getAudio(self.info["file"])
        print(self.soundFile)
    
    def computeValue(self, startTime, tick, value):
        now = tick - startTime

        if now > len(self.soundFile[0]):
            return value
            
        return self.soundFile[0][now]

    def getLength(self):
        return 15