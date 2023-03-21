import soundfile as sf
import numpy as np

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

class ResourceConstants:
    AUDIO_DATA: int = 0
    AUDIO_SAMPLE_RATE: int = 1

@singleton
class ResourceManager:

    def __init__(self):
        self.audios: dict = {}

    def getAudio(self, path):
        if path in self.audios.keys():
            return self.audios[path]

        file = sf.read(path)

        # If mono sound
        if len(file[ResourceConstants.AUDIO_DATA].shape) == 1:
            reformed = np.zeros((file[ResourceConstants.AUDIO_DATA].shape[0], 2), dtype=float)

            for i in range(file[ResourceConstants.AUDIO_DATA].shape[0]):
                reformed[i][0] = file[ResourceConstants.AUDIO_DATA][i]
                reformed[i][1] = file[ResourceConstants.AUDIO_DATA][i]

            file = [reformed, file[ResourceConstants.AUDIO_SAMPLE_RATE]]

        self.audios[path] = file

        return file

if __name__ == "__main__":
    ResourceManager().getAudio("interface/python/audio/sound/vache.wav")