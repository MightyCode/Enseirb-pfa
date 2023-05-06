from interface.python.audio.SoundInterface import SoundInterface

from interface.python.ResourceManager import ResourceManager

import os
                
if __name__ == "__main__":
    print("Start")
    projectPath = "projects/testSplitAudio.json"
    sound_creation = SoundInterface()
    sound_creation.read_project(projectPath)

    sound_creation.pre_compute()

    for i in range(10):
        export_path = "out"
        if not os.path.exists(export_path):
            os.makedirs(export_path)

        print("Export sound file for speaker " + str(i))
        ResourceManager().export_wav_from_channels("out/speaker" + str(i) + ".wav", 
                                                sound_creation._audio_result.data[i * 2], 
                                                sound_creation._audio_result.data[i * 2 + 1], 
                                                44100)