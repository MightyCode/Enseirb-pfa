from interface.python.audio.SoundCreation import SoundCreation

from interface.python.ResourceManager import ResourceManager

import os
import sys
                
if __name__ == "__main__":
    if(len(sys.argv)==1):
        print("Expected a json project, abroted")
        exit()
    if(sys.argv[1][-5:]!=".json"):
        print("Expected a json project, abroted")
        exit()
    projectPath = sys.argv[1]
    print("Start")
    sound_creation = SoundCreation()
    sound_creation.read_project(projectPath)

    sound_creation.pre_compute()

    for i in range(10):
        export_path = "out"
        if not os.path.exists(export_path):
            os.makedirs(export_path)

        print("Export sound file for speaker " + str(i))
        ResourceManager().exportWavFromChannels("out/speaker" + str(i) + ".wav", 
                                                sound_creation._audio_result.data[i * 2], 
                                                sound_creation._audio_result.data[i * 2 + 1], 
                                                44100)