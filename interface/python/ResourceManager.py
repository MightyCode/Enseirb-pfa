import soundfile as sf
import numpy as np
import json
import scipy.signal as signal


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
        self.jsons: dict = {}

    def getAudio(self, path, sampleRate=44100):
        if path in self.audios.keys():
            return self.audios[path]

        file = sf.read(path)

        if file[ResourceConstants.AUDIO_SAMPLE_RATE] != sampleRate:
            file = [signal.resample(file[ResourceConstants.AUDIO_DATA], 
                    int(len(file[ResourceConstants.AUDIO_DATA]) * float(sampleRate) / file[ResourceConstants.AUDIO_SAMPLE_RATE])),
                    sampleRate]
            
        # If mono sound
        if len(file[ResourceConstants.AUDIO_DATA].shape) == 1:
            reformed = np.zeros((file[ResourceConstants.AUDIO_DATA].shape[0], 2), dtype=float)

            for i in range(file[ResourceConstants.AUDIO_DATA].shape[0]):
                reformed[i][0] = file[ResourceConstants.AUDIO_DATA][i]
                reformed[i][1] = file[ResourceConstants.AUDIO_DATA][i]

            file = [reformed, file[ResourceConstants.AUDIO_SAMPLE_RATE]]

        self.audios[path] = file

        return file
    
    def exportWavFromChannels(self, path, leftChannel, rightChannel, samplerate):
        reformed = np.zeros((len(leftChannel), 2), dtype=float)

        for i in range(len(leftChannel)):
            reformed[i][0] = leftChannel[i]
            reformed[i][1] = rightChannel[i]

        sf.write(path, reformed, samplerate)
    
    def getJson(self, path):
        if path in self.jsons.keys():
            return self.jsons[path]
        
        with open(path, encoding="utf8") as json_file:
            self.jsons[path] = json.load(json_file)

        return self.jsons[path]

if __name__ == "__main__":
    ResourceManager().getAudio("interface/python/audio/sound/vache.wav")