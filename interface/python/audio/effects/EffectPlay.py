from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectPlay(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.soundFile = None
        self.amplitude = 1

    def preprocess(self):
        super().preprocess()

        self.loopTime = self.info["loopTime"] if "loopTime" in self.info.keys() else 1
        self.soundData = self.resourceManager.getAudio(self.info["file"], self.sampleRate)[ResourceConstants.AUDIO_DATA] 
        self.length = len(self.soundData) * self.loopTime
        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1

    def setAudioStreamId(self, streamsInId, streamOutId):
        assert streamOutId != None and len(streamOutId) != 0
    
    def computeValue(self, startTime, tick, audioStreams):
        now = tick - startTime

        assert now >= 0 or now < self.getLength()
        assert audioStreams == None or len(audioStreams) == 0

        return self.soundData[now % len(self.soundData)] * self.amplitude

    @staticmethod
    def Instanciate():
        return EffectPlay()

    @staticmethod
    def GetEffectName():
        return "play"