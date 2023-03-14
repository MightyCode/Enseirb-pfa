import soundfile as sf


class ResourceManager:
    _resourcemanager = ResourceManager()

    def getResourceManager():
        return _resourcemanager

    def __init__(self):
        self.audios = {}


    def getAudio(path):
        if path in self.audios.keys():
            return self.audios[path]

        file = sf.SoundFile(path)

        self.audios[path] = file
        

        return file