import ../ModelEffect as ModelEffect

class ModelAudioEffect(ModelEffect.ModelEffect):
    def __init__(self):
        super().__init__(ModelEffect.EffectPlay.SOUND)