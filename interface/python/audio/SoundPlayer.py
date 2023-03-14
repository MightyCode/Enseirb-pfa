from SpeakerGroup import SpeakerGroup
from TimelineEffect import TimelineEffect

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



if __name__ == "__main__":
    speakersGroup = SpeakerGroup()
    for i in range(10):
        speakersGroup.add(i)

    soundPlayer = SoundPlayer()
    soundPlayer.effects.append(
        TimelineEffect(

            #Create a reference model effect
        )
    )

    soundPlayer.effects[0].groupSpeakerId = 0

    soundPlayer.play()