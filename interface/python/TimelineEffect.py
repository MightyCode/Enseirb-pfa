class TimelineEffect:
    def __init__(self, refModelEffect, priority, start):
        self.refModelEffect = refModelEffect
        self.priority = priority
        self.start = start


        self.groupSpeakerId = -1
        self.groupSoundId = -1