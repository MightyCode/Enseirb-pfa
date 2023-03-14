class SpeakerGroup:
    _id = 0

    def __init__(self):
        self.group_id = SpeakerGroup._id
        SpeakerGroup._id += 1

        self.speakers = []
    
    def add(self, id):
        self.speakers.append(id)

    def remove(self, id):
        self.speakers.remove(id)

    def id(self):
        return self.group_id