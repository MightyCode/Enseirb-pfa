from interface.python.audio.SpeakerGroup import SpeakerGroup
from interface.python.audio.AudioResult import AudioResult

class SoundCreation:
    def __init__(self, samplerate):
        # Todo
        self.effects = []
        self.speakers_groups = []
        self.samplerate = samplerate

    def temporaryLoad(self):
        self.speakers_groups.append(
            SpeakerGroup()
        )

        for i in range(10):
            self.speakers_groups[0].add(i)

        self.audio_result = AudioResult(10, self.samplerate, 15)


    def readProject(self, path):
        # Todo
        self.temporaryLoad()

        for effect in self.effects:
            effect.preprocess()

    def create(self):
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

                        value = effect.computeValue(tick, self.audio_result.getAudioValue(speaker, tick))
                            
                        self.audio_result.setAudioValue(speaker, tick, value)

                    print(tick, value)
