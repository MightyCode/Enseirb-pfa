from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectPlay(ModelAudioEffect):
    def __init__(self, speakerGroup):
        super().__init__(speakerGroup)

        self.soundFile = None
        self.amplitude = 1

    def preprocess(self):
        self.samplerate = int(self.info["sampleRate"])
        self.soundData = self.resourceManager.getAudio(self.info["file"], self.samplerate)[ResourceConstants.AUDIO_DATA] 
        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1
    
    def computeValue(self, startTime, tick, value, speakerId, isLeft):
        now = tick - startTime

        channel = 0 if isLeft else 1

        if now < 0 or now > self.getLength():
            return value

        return self.soundData[now][channel] * self.amplitude

    def getLength(self):
        return len(self.soundData)

    @staticmethod
    def Instanciate(soundCreation, speakerGroup, modelEffectInfo, projectInfo):
        return EffectPlay(speakerGroup)

    @staticmethod
    def GetEffectName():
        return "play"