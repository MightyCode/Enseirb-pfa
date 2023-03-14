import SpeakerGroup

class SoundPlayer:
    def __init__(self):
        # Todo
        self.effects = []

        self.speakersGroups = []


    def temporaryLoad(self):
        self.speakersGroups.append(
            SpeakerGroup()
        )

        for i in range(10):
            self.speakersGroups[0].add(i)

    def readProject(self,path):
        # Todo
        self.temporaryLoad()


    