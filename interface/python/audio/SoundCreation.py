from interface.python.audio.SpeakerGroup import SpeakerGroup
from interface.python.audio.AudioResult import AudioResult


class SoundCreation:
    def __init__(self, samplerate, length):
        # Todo
        self.effects = []
        self.speakers_groups = []
        self.samplerate = samplerate
        self.length = length
        self.audio_result = None
    
    def addGroup(self):
        self.speakers_groups.append(
            SpeakerGroup()
        )

    def addToGroup(self, groupId, speakerId):
        if 0 > groupId or groupId >= len(self.speakers_groups):
            return

        if self.speakers_groups[groupId].contains(speakerId):
            return

        self.speakers_groups[groupId].add(speakerId)


    def temporaryLoad(self):
        self.addGroup()

        for i in range(10):
            self.addToGroup(0, i)

        self.addGroup()
        for i in range(1):
            self.addToGroup(1, i)
  
        self.audio_result = AudioResult(10, self.samplerate, self.length)


    def readProject(self, path):
        # Todo
        self.temporaryLoad()

        for effect in self.effects:
            effect.preprocess()


    def computeForSpeaker(self, effect, tick, speaker, isLeft):
        value = effect.computeValue(tick, 
            self.audio_result.getAudioValue(speaker, tick, isLeft),
            speaker, self.speakers_groups[effect.groupSpeakerId], isLeft)
        
        self.audio_result.setAudioValue(speaker, tick, value, isLeft)

    def create(self):
        display_pourcent = 0.1

        priorities: list = [0] * self.audio_result.nb_speakers

        for tick in range(self.audio_result.getNumberTick()):
            for i in range(self.audio_result.nb_speakers):
                priorities[0] = -1

            for effect in self.effects:
                start = effect.start * self.audio_result.samplerate
                end = start + effect.getLength() * self.audio_result.samplerate

                if tick >= start and tick <= end:
                    priority = effect.priority

                    for speaker in self.speakers_groups[effect.groupSpeakerId].speakers:
                        if priorities[speaker] > priority:
                            continue

                        self.computeForSpeaker(effect, tick, speaker, False)
                        self.computeForSpeaker(effect, tick, speaker, True)

            if tick > display_pourcent * self.audio_result.getNumberTick():
                print("Done " + str(round(display_pourcent * 100)), "%, "  \
                    + str(round(display_pourcent * self.audio_result.getNumberTick())) + "/"  \
                    + str(self.audio_result.getNumberTick()))

                display_pourcent += 0.1
