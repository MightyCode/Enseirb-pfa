import soundfile as sf
import numpy as np
import json
import scipy.signal as signal
import os

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
        self._audios: dict = {}
        self._jsons: dict = {}
        self._file_content: dict = {} 

    def get_audio(self, path: str, sampleRate: int = 44100) -> list:
        if path in self._audios.keys():
            return self._audios[path]

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

        self._audios[path] = file

        return file


    def export_wav_from_channels(self, path, leftChannel, rightChannel, samplerate):
        reformed = np.zeros((len(leftChannel), 2), dtype=float)

        for i in range(len(leftChannel)):
            reformed[i][0] = leftChannel[i]
            reformed[i][1] = rightChannel[i]

        sf.write(path, reformed, samplerate)


    def get_file_content(self, path: str) -> str:
        if path in self._file_content.keys():
            return self._file_content[path]

        file = open(path, 'r')
        self._file_content[path] = file.read()
        file.close()

        return self._file_content[path]

    def write_text_content(self, path : str, content: str) -> None:
        file = open(path, 'w')
        file.write(content)
        file.close()


    def get_json(self, path: str) -> dict:
        if path in self._jsons.keys():
            return self._jsons[path]
        
        with open(path, encoding="utf8") as json_file:
            self._jsons[path] = json.load(json_file)

        return self._jsons[path]


    def is_file_existing(self, path: str) -> bool:
        return os.path.exists(path)

if __name__ == "__main__":
    ResourceManager().get_audio("interface/python/audio/sound/vache.wav")