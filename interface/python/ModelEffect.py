from interface.python.ResourceManager import ResourceManager
from enum import Enum

class EEffectType(Enum):
    NONE = -1
    SOUND = 0
    LIGHT = 1


class ModelEffect:
    _id = 0

    def __init__(self, effect_type):
        self._id = ModelEffect._id
        ModelEffect._id += 1

        self.type = effect_type
        self.resourceManager = ResourceManager()
        self.info = {}

    def set_info(self, key, value):
        self.info[key] = value

    def id(self):
        return self._id

    def length(self):
        return 0

    def preprocess(self):
        pass