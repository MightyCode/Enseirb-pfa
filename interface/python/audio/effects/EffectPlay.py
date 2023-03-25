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
        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1
        
    
    def computeValue(self, startTime, tick, value, speakerId, speakerGroup, isLeft):
        now = tick - startTime

        channel = 0 if isLeft else 1

        if now < 0 or now > self.getLength():
            return value
            
        return self.soundFile[ResourceConstants.AUDIO_DATA][now][channel] * self.amplitude

    def getLength(self):
        return len(self.soundFile[ResourceConstants.AUDIO_DATA])