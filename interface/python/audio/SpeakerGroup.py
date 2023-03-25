class SpeakerGroup:
    _id = 0

    def __init__(self):
        self.group_id = SpeakerGroup._id
        SpeakerGroup._id += 1

        self.speakers = []
    
    def add(self, speakerId):
        self.speakers.append(speakerId)
        self.speakers.sort()

    def remove(self, speakerId):
        self.speakers.remove(speakerId)

    def contains(self, speakerId):
        return speakerId in self.speakers

    def id(self):
        return self.group_id