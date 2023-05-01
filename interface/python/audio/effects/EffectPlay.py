from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectPlay(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self._soundData = None
        self._amplitude = 1
        self._loop_time = 1 

    def preprocess(self):
        super().preprocess()

        self._loop_time = self.info["loopTime"] if "loopTime" in self.info.keys() else 1
        self._soundData = self.resourceManager.getAudio(self.info["file"], self._sampleRate)[ResourceConstants.AUDIO_DATA] 
        self._length = len(self._soundData) * self._loop_time
        self._amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1

    def set_audio_stream_id(self, streamsInId, streamOutId):
        assert streamOutId != None and len(streamOutId) != 0
        assert streamsInId == None or len(streamsInId) == 0

    
    def compute_value(self, startTime, tick, audioStreams):
        now = tick - startTime

        assert now >= 0 or now < self._length()

        return self._soundData[now % len(self._soundData)] * self._amplitude

    @staticmethod
    def Instanciate():
        return EffectPlay()

    @staticmethod
    def GetEffectName():
        return "play"