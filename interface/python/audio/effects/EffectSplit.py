from interface.python.audio.ModelAudioEffect import ModelAudioEffect

class EffectSplit(ModelAudioEffect):
    def __init__(self):
        super().__init__()

        self.soundFile = None
        self.amplitude = 1

        self.result: list = []

    def preprocess(self):
        super().preprocess()

        self.numberSecond = float(self.info["length"])
        self._length = round(self.numberSecond * self._sampleRate)

        self.amplitude = self.info["amplitude"] if "amplitude" in self.info.keys() else 1

    def set_audio_stream_id(self, streams_in_id, stream_out_id):
        assert streams_in_id != None and len(streams_in_id) == 1
        assert stream_out_id != None and len(stream_out_id) >= 2

        self.result = []
        for i in range(len(stream_out_id)):
            self.result.append([0, 0])
        
    
    def compute_value(self, start_time: int, tick: int, audio_streams: list):
        now = tick - start_time

        assert now >= 0 or now < self.length()  

        for i in range(len(self.result)):
            self.result[i][0] = audio_streams[0].left_value() * self.amplitude 
            self.result[i][1] = audio_streams[0].right_value() * self.amplitude 

        return self.result

    @staticmethod
    def Instanciate():
        return EffectSplit()

    @staticmethod
    def Get_effect_name():
        return "split"