from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectMute(ModelAudioEffect):
    def __init__(self):
        super().__init__()

    def preprocess(self):
        super().preprocess()

        self.numberSecond = float(self.info["length"])
        self.length = int(self.numberSecond * self.sampleRate)
    
    def setAudioStreamId(self, streamsInId, streamOutId):
        assert streamsInId == None or len(streamsInId) == 0
        assert streamOutId != None and len(streamOutId) != 0

    def computeValue(self, startTime, tick, audioStreams):
        now = tick - startTime

        assert now >= 0 or now < self.getLength()

        return 0

    @staticmethod
    def Instanciate():
        return EffectMute()

    @staticmethod
    def GetEffectName():
        return "mute"