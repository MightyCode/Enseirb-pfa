from operator import concat
from interface.python.ResourceManager import ResourceManager, ResourceConstants
from interface.python.audio.AudioSteam import AudioStream
from interface.python.audio.SpeakerGroup import SpeakerGroup
from interface.python.audio.AudioResult import AudioResult
from interface.python.audio.TimelineSoundEffect import TimelineSoundEffect

from interface.python.Interface import Interface

import importlib.util
import hashlib
import os, math

class SoundCreation (Interface):
    SEGMENT_SIZE = 2

    def __init__(self):
        super().__init__()

        self.timelineEffects: list = []
        self.segmentEffects: list = [] # Optimization purpose

        self.speakers_groups: list = []

        # Can have number of audioStreams > nb of groups of speaker, but at the end audioStreams[i] => groupSpeaker[i]
        self.audioStreams: list = []
        self.audioStreamIdMapping: dict = {}

        self.audio_result: AudioResult = None


    def read_project(self, path):
        project = ResourceManager().getJson(path)
        audioTimeline = project["audioTimeline"]

        self.samplerate = project["project"]["sampleRate"]

        mainSoundData = ResourceManager().getAudio(project["project"]["mainSound"], self.samplerate)[ResourceConstants.AUDIO_DATA]

        # Load Effects
        self.referenceEffects = []
        self.load_effect_from("interface/python/audio/effects")
        
        if ("externScripts" in project["project"].keys()):
            self.load_effect_from(project["project"]["externScripts"])

        self.audio_result = AudioResult(10, self.samplerate, len(mainSoundData))

        # Create as segment effects needed, number of segment is given by SEGMENT SIZE and sound result length
        self.segmentEffects = [None] * math.ceil(self.audio_result.getNumberTick() / (SoundCreation.SEGMENT_SIZE * self.samplerate))
        for i in range(len(self.segmentEffects)):
            self.segmentEffects[i] = []

        # Create speakers group
        self.audioStreamIdMapping.clear()
        for speakersGroup, groupIndex in zip(project["project"]["speakersGroups"], range(len(project["project"]["speakersGroups"]))):
            self.addGroup()
            self.audioStreamIdMapping[groupIndex] = groupIndex

            for i in speakersGroup:
                self.addToGroup(groupIndex, i)

        # Create all effect
        for effectRawData in audioTimeline:
            effect = self.createEffectFromName(effectRawData["modelEffect"], project["project"])
            timelineEffect = TimelineSoundEffect(effect, effectRawData["priority"], effectRawData["start"], self.samplerate)
            streamInId = None
            if "audioStreamIn" in effectRawData.keys():
                streamInId = [effectRawData["audioStreamIn"]] if isinstance(effectRawData["audioStreamIn"], int) else effectRawData["audioStreamIn"]
            streamOutId = [effectRawData["audioStreamOut"]] if isinstance(effectRawData["audioStreamOut"], int) else effectRawData["audioStreamOut"]

            timelineEffect.setAudioStreamsId(streamInId, streamOutId)
            self.timelineEffects.append(timelineEffect)

            # Append potentially new audio stream

            for audioStreamId in streamOutId if streamInId == None else concat(streamInId, streamOutId):
                if audioStreamId not in self.audioStreamIdMapping.keys():
                    self.audioStreamIdMapping[audioStreamId] = len(self.audioStreamIdMapping.keys())

        for effect in self.timelineEffects:
            effect.preprocess()

        # Append timeline effect in segment
        for effect in self.timelineEffects:
            segmentStart: int = int(effect.start // SoundCreation.SEGMENT_SIZE)
            segmentEnd: int = int((effect.getLength() / self.samplerate + effect.start) // SoundCreation.SEGMENT_SIZE)

            for i in range(max(segmentStart, 0), min(segmentEnd + 1, len(self.segmentEffects))):
                self.segmentEffects[i].append(effect)

        # Create audio Streams
        self.audioStreams = [None] * len(self.audioStreamIdMapping.keys())
        for i in self.audioStreamIdMapping.keys():
            self.audioStreams[self.audioStreamIdMapping[i]] = AudioStream(i)

    def load_effect_from(self, path):
        if not os.path.exists(path):
            return 

        for filename in os.listdir(path):
            if not filename.endswith(".py"):
                continue 
            
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

    
    def createEffectFromName(self, modelEffectInfo, projectInfo):
        effect = None

        for tested in self.referenceEffects:
            if modelEffectInfo["name"] in tested.GetEffectName():
                effect = tested.Instanciate()

        for key in modelEffectInfo.keys():
            if key != "name":
                effect.setInfo(key, modelEffectInfo[key])

        effect.setInfo("sampleRate", self.samplerate)
        effect.setInfo("audio", self.samplerate)

        return effect

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


    def computeResultForAudio(self, effectPriority, result, audioStreams):
        if isinstance(result, dict):
            pass # Todo
        elif isinstance(result, float) or isinstance(result, int):
            for audioStream in audioStreams:
                audioStream.setValueBoth(effectPriority, result)
        elif isinstance(result[0], float) or isinstance(result[0], int):
            for audioStream in audioStreams:
                audioStream.setBothValue(effectPriority, result[0], result[1])
        else:
            assert len(result) == len(audioStreams)

            for value, audioStream in zip(result, audioStreams):
                if isinstance(value, float) or isinstance(value, int):
                    audioStream.setValueBoth(effectPriority, result)
                else :
                    audioStream.setBothValue(effectPriority, value[0], value[1])

    def getAudioStreams(self, ids):
        if ids == None : return None

        result = []
        for id in ids:
            result.append(self.audioStreams[self.audioStreamIdMapping[id]])

        return result
    
    def compute_tick(self, tick):
        # Alter audio stream with effects
        for effect in self.segmentEffects[tick // (SoundCreation.SEGMENT_SIZE * self.samplerate)]:
            start = effect.start * self.samplerate

            if tick >= start and tick < start + effect.getLength():
                audioStreamsIn = self.getAudioStreams(effect.audioStreamsIn)
                audioStreamsOut = self.getAudioStreams(effect.audioStreamsOut)

                result = effect.computeValue(tick, audioStreamsIn)

                self.computeResultForAudio(effect.priority, result, audioStreamsOut)

    def pre_compute(self):
        display_pourcent = 0.1

        for tick in range(self.audio_result.getNumberTick()):
            for audioStream in self.audioStreams:
                audioStream.reset()

            self.compute_tick(tick)

            # Apply audio stream to audio result
            for i in range(self.audio_result.nb_speakers):
                priority: int = -1
                values = [0, 0]

                for group in self.speakers_groups:
                    if i not in group.speakers:
                        continue
                    
                    audioStream = self.audioStreams[group.id()]
                    if audioStream.priority() >= priority:
                        values = audioStream.bothValue()
                        priority = audioStream.priority()

                        if values[0] != 0: # Left
                            self.audio_result.setAudioValue(i, tick, values[0], 0)
                        if values[1] != 0: # Right
                            self.audio_result.setAudioValue(i , tick, values[1], 1)

            if tick > display_pourcent * self.audio_result.getNumberTick():
                print("Done " + str(round(display_pourcent * 100)), "%, "  \
                    + str(round(display_pourcent * self.audio_result.getNumberTick())) + "/"  \
                    + str(self.audio_result.getNumberTick()))

                display_pourcent += 0.1


    def do_scenarii(self):
        print("Do scenarii sound")