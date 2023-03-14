import soundfile as sf

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class ResourceManager:
    def __init__(self):
        self.audios = {}


    def getAudio(self, path):
        if path in self.audios.keys():
            return self.audios[path]

        file = sf.read(path)

        self.audios[path] = file

        return file

if __name__ == "__main__":
    ResourceManager().getAudio("interface/python/audio/sound/vache.wav")