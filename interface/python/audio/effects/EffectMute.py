from interface.python.audio.ModelAudioEffect import ModelAudioEffect
from interface.python.ResourceManager import ResourceConstants

class EffectMute(ModelAudioEffect):
    def __init__(self):
        super().__init__()

    def preprocess(self):
        super().preprocess()

        self.numberSecond = float(self.info["length"])
        self._length = int(self.numberSecond * self._sampleRate)
    
    def set_audio_stream_id(self, streams_in_id, stream_out_id):
        assert streams_in_id == None or len(streams_in_id) == 0
        assert stream_out_id != None and len(stream_out_id) != 0

    def compute_value(self, start_time: int, tick: int, audio_streams: list):
        now = tick - start_time

        assert now >= 0 or now < self.length()

        return 0

    @staticmethod
    def Instanciate():
        return EffectMute()

    @staticmethod
    def Get_effect_name():
        return "mute"