from interface.python.audio.SoundCreation import SoundCreation

from interface.python.ResourceManager import ResourceManager

                
if __name__ == "__main__":
    print("Start")
    mainSoundPath = "interface/python/audio/sound/retro.wav"
    mainSoundData, samplerate = ResourceManager().getAudio(mainSoundPath)

    sound_creation = SoundCreation(samplerate, len(mainSoundData))

    sound_creation.readProject("configs/project1.json")

    sound_creation.create()

    for i in range(10):
        print("Generate sound for speaker " + str(i))
        ResourceManager().exportWavFromChannels("out/speaker" + str(i) + ".wav", 
                                                sound_creation.audio_result.data[i * 2], 
                                                sound_creation.audio_result.data[i * 2 + 1], 
                                                44100)