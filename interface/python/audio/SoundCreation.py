from re import A
from interface.python.ResourceManager import ResourceManager
from interface.python.audio.SpeakerGroup import SpeakerGroup
from interface.python.audio.AudioResult import AudioResult

from interface.python.audio.TimelineSoundEffect import TimelineSoundEffect

from interface.python.audio.effects.EffectPlay import EffectPlay
from interface.python.audio.effects.EffectAmplitudeTweening import EffectAmplitudeTweening
from interface.python.audio.effects.EffectOscillator import EffectOscillator
from interface.python.audio.effects.EffectMute import EffectMute
from interface.python.audio.effects.EffectAffect import EffectAffect

import importlib.util
import os

class SoundCreation:
    def __init__(self):
        self.effects = []
        self.speakers_groups = []
        self.length = 0
        self.audio_result = None

        self.referenceEffects = []
    
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


    def computeForSpeaker(self, effect, tick, speaker, isLeft, audioValues):
        index = speaker * 2 + (1 if isLeft else 0)
        audioValues[index] = effect.computeValue(tick, audioValues[index],
            speaker, isLeft)

    def create(self):
        display_pourcent = 0.1

        priorities: list = [0] * self.audio_result.nb_speakers
        audioValue: list = [0] * self.audio_result.nb_speakers * 2

        for tick in range(self.audio_result.getNumberTick()):
            for i in range(self.audio_result.nb_speakers):
                priorities[i] = -1
                audioValue[i] = 0

            for effect in self.effects:
                start = effect.start * self.samplerate
                end = start + effect.getLength()

                if tick >= start and tick <= end:
                    priority = effect.priority

                    for speaker in self.speakers_groups[effect.groupSpeakerId].speakers:
                        if priorities[speaker] > priority:
                            continue
                            
                        self.computeForSpeaker(effect, tick, speaker, False, audioValue)
                        self.computeForSpeaker(effect, tick, speaker, True, audioValue)

            for i in range(self.audio_result.nb_speakers * 2):
                if audioValue[i] != 0:
                    self.audio_result.setAudioValue(i // 2, tick, audioValue[i], i % 2 == 0)

            if tick > display_pourcent * self.audio_result.getNumberTick():
                print("Done " + str(round(display_pourcent * 100)), "%, "  \
                    + str(round(display_pourcent * self.audio_result.getNumberTick())) + "/"  \
                    + str(self.audio_result.getNumberTick()))

                display_pourcent += 0.1


    def load_custom_effects(self, path):
        if os.path.exists(path):
            for filename in os.listdir(path):
                if filename.endswith(".py"):
                    effect_module_name = os.path.splitext(filename)[0]
                    effect_module_path = os.path.join(path, filename)

                    # Load the module and find the effect class
                    spec = importlib.util.spec_from_file_location(effect_module_name, effect_module_path)
                    effect_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(effect_module)
                    for attr_name in dir(effect_module):
                        attr = getattr(effect_module, attr_name)
                        if hasattr(attr, "GetEffectName") and hasattr(attr, "Instanciate"):
                            self.referenceEffects.append(attr)

    
    def createEffectFromName(self, speakerGroup, modelEffectInfo, projectInfo):
        effect = None

        for tested in self.referenceEffects:
            if modelEffectInfo["name"] in tested.GetEffectName():
                effect = tested.Instanciate(self, speakerGroup, modelEffectInfo, projectInfo)

        for key in modelEffectInfo.keys():
            if key == "name":
                continue
        
            effect.setInfo(key, modelEffectInfo[key])

        effect.setInfo("sampleRate", projectInfo["sampleRate"])

        return effect

    def readProject(self, path):
        project = ResourceManager().getJson(path)
        audioTimeline = project["audioTimeline"]

        mainSoundData, self.samplerate = ResourceManager().getAudio(project["project"]["mainSound"])

        self.load_custom_effects("interface/python/audio/effects")
        
        if ("externScripts" in project["project"].keys()):
            self.load_custom_effects(project["project"]["externScripts"])

        self.audio_result = AudioResult(10, self.samplerate, len(mainSoundData))

        groupIndex = 0
        for speakersGroup in project["project"]["speakersGroups"]:
            self.addGroup()

            for i in speakersGroup:
                self.addToGroup(groupIndex, i)
            
            groupIndex += 1

        for effectRawData in audioTimeline:
            effect = self.createEffectFromName(self.speakers_groups[effectRawData["speakersGroup"]].speakers, 
                                               effectRawData["modelEffect"], project["project"])
            timelineEffect = TimelineSoundEffect(effect, effectRawData["priority"], effectRawData["start"])
            timelineEffect.setGroupSpeaker(effectRawData["speakersGroup"])

            self.effects.append(timelineEffect)

        for effect in self.effects:
            effect.preprocess()
