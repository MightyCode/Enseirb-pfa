from interface.python.ModelEffect import ModelEffect, EEffectType

class ModelAudioEffect(ModelEffect):
    def __init__(self, speakerGroup):
        super().__init__(EEffectType.SOUND)
        self.speakerGroup = speakerGroup