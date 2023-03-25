from sympy import im
from interface.python.ResourceManager import ResourceManager
from openal import *

import time
import wave

class Listener:
    def __init__(self):
        self.device = alcOpenDevice(None)

        if not self.device:
            error = alcGetError()
            print("Open al init error : " + error)

        self.context = alcCreateContext(self.device, None)
        alcMakeContextCurrent(self.context)

        self._position = [0, 0, 0]
        self.setPosition(self._position)

    def setPosition(self, pos):
            self._position = pos
            x, y, z = pos
            alListener3f(AL_POSITION, x, y, z)

    def delete(self):
        alcDestroyContext(self.context)
        alcCloseDevice(self.device)

class SoundData:
    def __init__(self, path) -> None:
        data = wave.open(path)
        channels = data.getnchannels()
        bitrate = data.getsampwidth() * 8
        samplerate = data.getframerate()
        wavbuf = data.readframes(data.getnframes())

        self.duration = (len(wavbuf) / float(samplerate))/2
        self.length = len(wavbuf)
        
        formatmap = {
            (1, 8) : AL_FORMAT_MONO8,
            (2, 8) : AL_FORMAT_STEREO8,
            (1, 16): AL_FORMAT_MONO16,
            (2, 16) : AL_FORMAT_STEREO16,
        }

        alformat = formatmap[(channels, bitrate)]

        self.bufferId = ALuint(0)

        alGenBuffers(1, self.bufferId)
        alBufferData(self.bufferId, alformat, wavbuf, len(wavbuf), samplerate)

    def id(self):
        return self.bufferId

    def delete(self):
        alDeleteBuffers(1, self.bufferId)

class SoundSource:
    def __init__(self, position) -> None:
        self.position = position
        
        self.source = ALuint(0)
        
        alGenSources(1, self.source)

        alSourcef(self.source, AL_PITCH, 1)
        alSourcef(self.source, AL_GAIN, 1)
        alSourcef(self.source, AL_ROLLOFF_FACTOR, 0.5)
        alSource3f(self.source, AL_VELOCITY, 0, 0, 0)
        alSourcei(self.source, AL_LOOPING, AL_FALSE)

        self.setPosition(self.position)

    def setPosition(self, position):
        alSource3f(self.source, AL_POSITION, position[0], position[1], position[2])

    def play(self):
        alSourcePlay(self.source)

    def addSound(self, soundData):
        alSourceQueueBuffers(self.source, 1, soundData.id())

    def isPlaying(self):
        state = ALint(0)

        alGetSourcei(self.source, AL_SOURCE_STATE, state)
        return state.value == al.AL_PLAYING

    def delete(self):
        alDeleteSources(1, self.source)


def main():
    config = ResourceManager().getJson("configs/eirlab.json")
    
    listener = Listener()

    buffers = []
    sources = []
    for i in range(10):
        soundData = SoundData("out/speaker" + str(i) + ".wav")
        buffers.append(soundData)

        soundSource = SoundSource(config["speakerPosition"][i])
        sources.append(soundSource)
        soundSource.addSound(soundData)

        soundSource.play()

    for a in range(0,704,64):
        listener.setPosition([a, 240, 0])
        time.sleep(0.1)

    for i in range(10):
        while sources[i].isPlaying():
            time.sleep(0.1)
        
    for i in range(10):
        sources[i].delete()
        buffers[i].delete()
    
    listener.delete()

main()