from interface.python.audio.AudioSteam import AudioStream


class TimelineSoundEffect:
    def __init__(self, refAudioModelEffect, priority, start, sampleRate):
        self.refAudioModelEffect = refAudioModelEffect
        self.priority = priority
        self.start = start
        self.sampleRate = sampleRate

        self.audioStreamsIn: list = []
        self.audioStreamsOut: list = []

    def preprocess(self):
        self.refAudioModelEffect.preprocess()

    def setAudioStreamsId(self, streamsInId, streamsOutId):
        self.audioStreamsIn = streamsInId
        self.audioStreamsOut = streamsOutId

        self.refAudioModelEffect.setAudioStreamId(streamsInId, streamsOutId)

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
    def computeValue(self, time, audioStreams):
        return self.refAudioModelEffect.computeValue(int(self.start * self.sampleRate), time, audioStreams)

    def getLength(self):
        return self.refAudioModelEffect.getLength()