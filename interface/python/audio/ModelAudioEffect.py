from interface.python.ModelEffect import ModelEffect, EEffectType

class ModelAudioEffect(ModelEffect):
    def __init__(self):
        super().__init__(EEffectType.SOUND)

        self._sampleRate: int = 0
        self._audio_stream_out: list = [] 
        self._length: int = 0

    def preprocess(self):
        self._sampleRate = int(self.info["sampleRate"])

    def set_audio_stream_id(self, streams_in_id: list, stream_out_id: list):
        pass

    def compute_value(self, start_time: int, tick: int, audio_streams: list):
        pass

    def length(self):
        return self._length

    @staticmethod
    def Instanciate():
        return ModelAudioEffect()

    @staticmethod
    def Get_effect_name():
        return "empty"