from interface.python.audio.TimelineSoundEffect import TimelineSoundEffect
from interface.python.audio.SoundCreation import SoundCreation

from interface.python.audio.effects.EffectPlay import EffectPlay

                
if __name__ == "__main__":
    print("Start")
    samplerate = 44100

    sound_creation = SoundCreation(samplerate)

    effect_play = EffectPlay()
    effect_play.setInfo("file", "interface/python/audio/sound/vache.wav")
    effect_play.setInfo("samplerate", str(samplerate))

    #Create a reference model effect
    sound_creation.effects.append(
        TimelineSoundEffect(
            effect_play,
            0, 
            0

        )
    )

    sound_creation.readProject("")

    sound_creation.effects[0].setGroupSpeaker(0)

    sound_creation.create()