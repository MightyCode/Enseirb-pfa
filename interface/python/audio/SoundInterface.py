from operator import concat
from interface.python.ResourceManager import ResourceManager, ResourceConstants
from interface.python.audio.AudioSteam import AudioStream
from interface.python.audio.SpeakerGroup import SpeakerGroup
from interface.python.audio.AudioResult import AudioResult
from interface.python.audio.effects.TimelineSoundEffect import TimelineSoundEffect

from interface.python.Interface import Interface

import importlib.util
import hashlib
import os, math

import hashlib
import json

"""
Interface to load projet and create audios source (several .wav) to play it
"""
class SoundInterface (Interface):
    # Size (in second) of segments to play timeline effects
    SEGMENT_SIZE = 2
    
    PATH_AUDIO_FILE = "out/"
    PATH_SAVED_HASH = PATH_AUDIO_FILE + "hash.text"

    def __init__(self, stop_flag, verbose: bool = False):
        super().__init__(stop_flag, verbose)

        self._timeline_effects: list = []
        self._segment_effects: list = [] # Optimization purpose
        self._speakers_groups: list = []

        self._project_hash = None
        self._should_compute = False

        # Can have number of audioStreams > nb of groups of speaker, but at the end audioStreams[i] => groupSpeaker[i]
        self._audio_streams: list = []
        self._audio_stream_id_mapping: dict = {}

        self._audio_result: AudioResult = None

        self._reference_effects: list = []

        self._sample_rate: int = 0

        self._player = None

        self._resource_manager: ResourceManager = ResourceManager()

    def attach_player(self, player) -> None:
        self._player = player


    def compute_hash(dictionnary: dict) -> str:
        json_string = json.dumps(dictionnary, sort_keys=True)

        sha256_hash = hashlib.sha256(json_string.encode()).hexdigest()

        return sha256_hash

    """
    Will read a projet given a path, if the audio source has already been computed, it will load it
    If not if will load all components need to create the audio source and save it
    """
    def read_project(self, path: str) -> str:
        project: dict = self._resource_manager.get_json(path)

        # Compute the hash from project to kno
        self._project_hash = SoundInterface.compute_hash(project)

        if self._resource_manager.is_file_existing(SoundInterface.PATH_SAVED_HASH) \
            and self._resource_manager.get_file_content(SoundInterface.PATH_SAVED_HASH) == self._project_hash:
            return

        print("Not corresponding hash, create audio sources")

        self._should_compute = True
        self._sample_rate: int = project["project"]["sampleRate"]

        audio_timeline: list = project["audioTimeline"]
        main_sound_data = self._resource_manager.get_audio(project["project"]["mainSound"], self._sample_rate)[ResourceConstants.AUDIO_DATA]

        # Load Effects
        self._reference_effects = []
        self.load_effect_from("interface/python/audio/effects")
        
        if ("externScripts" in project["project"].keys()):
            self.load_effect_from(project["project"]["externScripts"])

        self._audio_result = AudioResult(10, self._sample_rate, len(main_sound_data))

        # Create as segment effects needed, number of segment is given by SEGMENT SIZE and sound result length
        self._segment_effects = [None] * math.ceil(self._audio_result.get_number_tick() / (SoundInterface.SEGMENT_SIZE * self._sample_rate))
        for i in range(len(self._segment_effects)):
            self._segment_effects[i] = []

        # Create speakers group
        self._audio_stream_id_mapping.clear()
        for speakers_group, group_index in zip(project["project"]["speakersGroups"], range(len(project["project"]["speakersGroups"]))):
            self.add_group()
            self._audio_stream_id_mapping[group_index] = group_index

            for i in speakers_group:
                self.add_to_group(group_index, i)

        # Create all effect
        for effect_raw_data in audio_timeline:
            effect = self.create_effect_from_name(effect_raw_data["modelEffect"], project["project"])
            timeline_effect = TimelineSoundEffect(effect, effect_raw_data["priority"], effect_raw_data["start"], self._sample_rate)

            stream_in_id = None

            if "audioStreamIn" in effect_raw_data.keys():
                stream_in_id = [effect_raw_data["audioStreamIn"]] if isinstance(effect_raw_data["audioStreamIn"], int) else effect_raw_data["audioStreamIn"]
            stream_out_id = [effect_raw_data["audioStreamOut"]] if isinstance(effect_raw_data["audioStreamOut"], int) else effect_raw_data["audioStreamOut"]

            timeline_effect.set_audio_streams_id(stream_in_id, stream_out_id)
            self._timeline_effects.append(timeline_effect)

            # Append potentially new audio stream

            for audio_stream_id in stream_out_id if stream_in_id == None else concat(stream_in_id, stream_out_id):
                if audio_stream_id not in self._audio_stream_id_mapping.keys():
                    self._audio_stream_id_mapping[audio_stream_id] = len(self._audio_stream_id_mapping.keys())

        for effect in self._timeline_effects:
            effect.preprocess()

        # Append timeline effect in segment
        for effect in self._timeline_effects:
            segment_start: int = int(effect.start() // SoundInterface.SEGMENT_SIZE)
            segment_end: int = int((effect.length() / self._sample_rate + effect.start()) // SoundInterface.SEGMENT_SIZE)

            for i in range(max(segment_start, 0), min(segment_end + 1, len(self._segment_effects))):
                self._segment_effects[i].append(effect)

        # Create audio Streams
        self._audio_streams = [None] * len(self._audio_stream_id_mapping.keys())
        for i in self._audio_stream_id_mapping.keys():
            self._audio_streams[self._audio_stream_id_mapping[i]] = AudioStream(i)

    def load_effect_from(self, path):
        if not os.path.exists(path):
            return 

        for file_name in os.listdir(path):
            if not file_name.endswith(".py"):
                continue 
            
            effect_module_name = os.path.splitext(file_name)[0]
            effect_module_path = os.path.join(path, file_name)

            # Load the module and find the effect class
            spec = importlib.util.spec_from_file_location(effect_module_name, effect_module_path)
            effect_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(effect_module)
            for attr_name in dir(effect_module):
                attr = getattr(effect_module, attr_name)
                if hasattr(attr, "Get_effect_name") and hasattr(attr, "Instanciate"):
                    self._reference_effects.append(attr)

    
    def create_effect_from_name(self, model_effect_info, project_info):
        effect = None

        for tested in self._reference_effects:
            if model_effect_info["name"] in tested.Get_effect_name():
                effect = tested.Instanciate()

        for key in model_effect_info.keys():
            if key != "name":
                effect.set_info(key, model_effect_info[key])

        effect.set_info("sampleRate", self._sample_rate)
        effect.set_info("audio", self._sample_rate)

        return effect

    def add_group(self):
        self._speakers_groups.append(
            SpeakerGroup()
        )

    def add_to_group(self, group_id, speaker_id):
        if 0 > group_id or group_id >= len(self._speakers_groups):
            return

        if self._speakers_groups[group_id].contains(speaker_id):
            return

        self._speakers_groups[group_id].add(speaker_id)


    def compute_result_for_audio(self, effect_priority, result, audio_streams):
        if isinstance(result, dict):
            pass # Todo
        elif isinstance(result, float) or isinstance(result, int):
            for audioStream in audio_streams:
                audioStream.set_value_both(effect_priority, result)
        elif isinstance(result[0], float) or isinstance(result[0], int):
            for audioStream in audio_streams:
                audioStream.set_both_value(effect_priority, result[0], result[1])
        else:
            assert len(result) == len(audio_streams)

            for value, audioStream in zip(result, audio_streams):
                if isinstance(value, float) or isinstance(value, int):
                    audioStream.set_value_both(effect_priority, result)
                else :
                    audioStream.set_both_value(effect_priority, value[0], value[1])

    def get_audio_streams(self, ids):
        if ids == None : return None

        result = []
        for id in ids:
            result.append(self._audio_streams[self._audio_stream_id_mapping[id]])

        return result
    
    def compute_tick(self, tick):
        # Alter audio stream with effects
        for effect in self._segment_effects[tick // (SoundInterface.SEGMENT_SIZE * self._sample_rate)]:
            start = effect.start() * self._sample_rate

            if tick >= start and tick < start + effect.length():
                audioStreamsIn = self.get_audio_streams(effect.get_audio_streams_in())
                audioStreamsOut = self.get_audio_streams(effect.get_audio_streams_out())

                result = effect.compute_value(tick, audioStreamsIn)

                self.compute_result_for_audio(effect.priority(), result, audioStreamsOut)

    """
    If hash is corresponding _should_compute be false, so only load sound from files
    If other case, will compute each tick of the sound
    """
    def pre_compute(self):
        if not self._should_compute:
            for i in range(len(self._audio_streams)):
                audio_stream.load_data_from_resources(i)

            return


        display_pourcent = 0.1

        for tick in range(self._audio_result.get_number_tick()):
            # Threading purpose, should stop the computing
            if self._stop_flag.is_set():
                break
            
            # Set all value to zero
            for audio_stream in self._audio_streams:
                audio_stream.reset()

            self.compute_tick(tick)

            # Apply audio stream to audio result using group of speakers
            for i in range(self._audio_result._nb_speakers):
                priority: int = -1
                values = [0, 0]

                for group in self._speakers_groups:
                    if i not in group.speakers:
                        continue
                    
                    audio_stream = self._audio_streams[group.id()]
                    if audio_stream.priority() >= priority:
                        values = audio_stream.both_value()
                        priority = audio_stream.priority()

                        if values[0] != 0: # Left
                            self._audio_result.set_audio_value(i, tick, values[0], 0)
                        if values[1] != 0: # Right
                            self._audio_result.set_audio_value(i , tick, values[1], 1)

            if tick > display_pourcent * self._audio_result.get_number_tick() and self._verbose:
                print("Done " + str(round(display_pourcent * 100)), "%, "  \
                    + str(round(display_pourcent * self._audio_result.get_number_tick())) + "/"  \
                    + str(self._audio_result.get_number_tick()))

                display_pourcent += 0.1

        self._resource_manager.write_text_content(SoundInterface.PATH_SAVED_HASH, self._project_hash)

    def do_scenarii(self, start_time):
        if (self._player == None):
            print("Please attach player to sound interface")

        self._player.play(self._audio_result, start_time, self._sample_rate)
        print("Do scenarii sound")

    def stop(self):
        self._should_play = False