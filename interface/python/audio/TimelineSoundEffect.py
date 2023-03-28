class TimelineSoundEffect:
    def __init__(self, refAudioModelEffect, priority, start):
        self.refAudioModelEffect = refAudioModelEffect
        self.priority = priority
        self.start = start

        self.groupSpeakerId = -1

    def preprocess(self):
        self.refAudioModelEffect.preprocess()

    def setGroupSpeaker(self, id):
        self.groupSpeakerId = id

    def computeValue(self, time, value, speakerId, isLeft):
        return self.refAudioModelEffect.computeValue(self.start, time, value, speakerId, isLeft)

    def getLength(self):
        return self.refAudioModelEffect.getLength()