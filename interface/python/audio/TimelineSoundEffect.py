class TimelineSoundEffect:
    def __init__(self, ref_audio_model_effect, priority, start, sample_rate):
        self._ref_audio_model_effect = ref_audio_model_effect
        self._priority = priority
        self._start = start
        self._sample_rate = sample_rate

        self._audio_streams_in: list = []
        self._audio_streams_out: list = []

    def preprocess(self):
        self._ref_audio_model_effect.preprocess()

    def set_audio_streams_id(self, streams_in_id, streams_out_id):
        self._audio_streams_in = streams_in_id
        self._audio_streams_out = streams_out_id

        self._ref_audio_model_effect.set_audio_stream_id(streams_in_id, streams_out_id)

    """ 
    Mutiples return values are possible :
        - Return a single value, will be associated to all stream for left and right ear
        - Return a single double value, will be associated to all stream 
        - Return a list of double value, will be associated to all stream element to each element (as listed in project file)
        - Return a dict with this form : {
            "ids" : [[0], [1, 3], [2]]
            "values" : [[0.1518, 0.7787], 0.1, 0.2]
          }

          Note that element in values can be single or double element to assign to both or left then right ear
    """
    def compute_value(self, time, audioStreams):
        return self._ref_audio_model_effect.compute_value(int(self._start * self._sample_rate), time, audioStreams)

    def length(self):
        return self._ref_audio_model_effect.length()

    def start(self):
        return self._start

    def priority(self):
        return self._priority

    def get_audio_streams_in(self):
        return self._audio_streams_in

    def get_audio_streams_out(self):
        return self._audio_streams_out