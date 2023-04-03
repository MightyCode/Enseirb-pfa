from interface.python.ModelEffect import ModelEffect, EEffectType

class ModelAudioEffect(ModelEffect):
    def __init__(self):
        super().__init__(EEffectType.SOUND)

        self.sampleRate: int = 0
        self.audioStreamOut: list = [] 
        self.length: int = 0

    def preprocess(self):
        self.sampleRate = int(self.info["sampleRate"])

    def setAudioStreamId(self, streamsInId, streamOutId):
        pass

    def computeValue(self, startTime, tick, speakerId):
        pass

    def getLength(self):
        return self.length

    @staticmethod
    def Instanciate():
        return ModelAudioEffect()

    @staticmethod
    def GetEffectName():
        return "empty"