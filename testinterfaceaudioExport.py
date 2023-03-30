from interface.python.audio.SoundCreation import SoundCreation

from interface.python.ResourceManager import ResourceManager

import os
                
if __name__ == "__main__":
    print("Start")
    projectPath = "projects/testMergeAudio.json"
    sound_creation = SoundCreation()
    sound_creation.readProject(projectPath)

    sound_creation.create()

    for i in range(10):
        export_path = "out"
        if not os.path.exists(export_path):
            os.makedirs(export_path)

        print("Export sound file for speaker " + str(i))
        ResourceManager().exportWavFromChannels("out/speaker" + str(i) + ".wav", 
                                                sound_creation.audio_result.data[i * 2], 
                                                sound_creation.audio_result.data[i * 2 + 1], 
                                                44100)