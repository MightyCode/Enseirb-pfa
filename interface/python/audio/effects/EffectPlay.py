from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectPlay(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.samplerate = 0
        self.soundFile = None

    def preprocess(self):
        self.samplerate = int(self.info["samplerate"])

        self.soundFile = self.resourceManager.getAudio(self.info["file"])
        self.soundFile = self.resourceManager.getAudio("interface/python/audio/sound/vache.wav")
        
    
    def computeValue(self, startTime, tick, value, speakerId, speakerGroup, isLeft):
        now = tick - startTime

        channel = 0 if isLeft else 1

        if now < 0 or now > len(self.soundFile[ResourceConstants.AUDIO_DATA]):
            return value
            
        return self.soundFile[ResourceConstants.AUDIO_DATA][now][channel]

    def getLength(self):
        return len(self.soundFile[ResourceConstants.AUDIO_DATA])