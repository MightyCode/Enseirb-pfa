from interface.python.ModelEffect import ModelEffect, EEffectType

class ModelAudioEffect(ModelEffect):
    def __init__(self):
        super().__init__(EEffectType.SOUND)