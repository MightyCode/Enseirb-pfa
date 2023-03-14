from enum import Enum

class EEffectType(Enum):
    NONE = -1
    SOUND = 0
    LIGHT = 1


class ModelEffect:
    _id = 0
    def __init__(self, effectType):
        self.id = _id
        _id += 1
        self.type = effectType

    def id(self):
        return self.id