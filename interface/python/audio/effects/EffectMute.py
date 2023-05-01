from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectMute(ModelAudioEffect):
    def __init__(self):
        super().__init__()

    def preprocess(self):
        super().preprocess()

        self.numberSecond = float(self.info["length"])
        self._length = int(self.numberSecond * self._sampleRate)
    
    def set_audio_stream_id(self, streamsInId, streamOutId):
        assert streamsInId == None or len(streamsInId) == 0
        assert streamOutId != None and len(streamOutId) != 0

    def compute_value(self, startTime, tick, audioStreams):
        now = tick - startTime

        assert now >= 0 or now < self._length()

        return 0

    @staticmethod
    def Instanciate():
        return EffectMute()

    @staticmethod
    def GetEffectName():
        return "mute"