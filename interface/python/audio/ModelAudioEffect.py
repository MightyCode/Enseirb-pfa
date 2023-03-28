from interface.python.ModelEffect import ModelEffect, EEffectType

class ModelAudioEffect(ModelEffect):
    def __init__(self, speakerGroup: list):
        super().__init__(EEffectType.SOUND)
        self.speakerGroup = speakerGroup

    @staticmethod
    def Instanciate(soundCreation, speakerGroup, modelEffectInfo, projectInfo):
        return ModelAudioEffect(speakerGroup)

    @staticmethod
    def GetEffectName():
        return "empty"