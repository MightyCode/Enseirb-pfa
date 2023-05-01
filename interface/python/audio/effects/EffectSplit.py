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

    def set_audio_stream_id(self, streamsInId, streamOutId):
        assert streamsInId != None
        assert len(streamsInId) == 1

        assert streamOutId != None
        assert len(streamOutId) >= 2

        self.result = []
        for i in range(len(streamOutId)):
            self.result.append([0, 0])
        
    
    def compute_value(self, startTime, tick, audioStreams):
        now = tick - startTime

        assert now >= 0 or now < self._length()  

        for i in range(len(self.result)):
            self.result[i][0] = audioStreams[0].left_value() * self.amplitude 
            self.result[i][1] = audioStreams[0].right_value() * self.amplitude 

        return self.result

    @staticmethod
    def Instanciate():
        return EffectSplit()

    @staticmethod
    def GetEffectName():
        return "split"