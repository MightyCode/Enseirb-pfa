from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectPlay(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.samplerate = 0
        self.soundFile = None
        self.amplitude = 1

    def preprocess(self):
        self.soundData = self.resourceManager.getAudio(self.info["file"])[ResourceConstants.AUDIO_DATA] 
        self.samplerate = self.resourceManager.getAudio(self.info["file"])[ResourceConstants.AUDIO_SAMPLE_RATE] 
        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1
        
    
    def computeValue(self, startTime, tick, value, speakerId, speakerGroup, isLeft):
        now = tick - startTime

        channel = 0 if isLeft else 1

        if now < 0 or now > self.getLength():
            return value

        return self.soundData[now][channel] * self.amplitude

    def getLength(self):
        return len(self.soundData)