from interface.python.audio.effects.ModelAudioEffect import ModelAudioEffect
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
        self._soundData = self.resourceManager.get_audio(self.info["file"], self._sampleRate)[ResourceConstants.AUDIO_DATA] 
        self._length = len(self._soundData) * self._loop_time
        self._amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1

    def set_audio_stream_id(self, streams_in_id, stream_out_id):
        assert streams_in_id == None or len(streams_in_id) == 0
        assert stream_out_id != None and len(stream_out_id) != 0

    def compute_value(self, start_time: int, tick: int, audio_streams: list):
        now = tick - start_time

        assert now >= 0 or now < self.length()

        return self._soundData[now % len(self._soundData)] * self._amplitude

    @staticmethod
    def Instanciate():
        return EffectPlay()

    @staticmethod
    def Get_effect_name():
        return "play"