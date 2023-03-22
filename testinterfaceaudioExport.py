from interface.python.audio.TimelineSoundEffect import TimelineSoundEffect
from interface.python.audio.SoundCreation import SoundCreation

from interface.python.audio.effects.EffectPlay import EffectPlay
from interface.python.ResourceManager import ResourceManager

                
if __name__ == "__main__":
    print("Start")
    mainSoundPath = "interface/python/audio/sound/vache.wav"
    mainSoundData, samplerate = ResourceManager().getAudio(mainSoundPath)

    sound_creation = SoundCreation(samplerate, len(mainSoundData))

    effect_play = EffectPlay()
    effect_play.setInfo("file", mainSoundPath)
    effect_play.setInfo("samplerate", str(samplerate))

    #Create a reference model effect
    sound_creation.effects.append(
        TimelineSoundEffect(effect_play, 0, 0)
    )

    sound_creation.readProject("")

    sound_creation.effects[0].setGroupSpeaker(0)

    sound_creation.create()

    for i in range(10):
        print(sound_creation.audio_result.data[i * 2])
        ResourceManager().exportWavFromChannels("out/speaker" + str(i) + ".wav", 
                                                sound_creation.audio_result.data[i * 2], 
                                                sound_creation.audio_result.data[i * 2 + 1], 
                                                44100)