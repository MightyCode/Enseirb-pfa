import sys
import os

# Add the root folder to the module search path
root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from interface.python.ResourceManager import ResourceManager
from openal import *

import time
import wave

def checkError(text = ""):
    error = alGetError()
    if (error != 0):
        print(text + " : Openal error n°" + str(error))

class Listener:
    def __init__(self):
        self.device = alcOpenDevice(None)

        if self.device == None:
            checkError(None)

        self.context = alcCreateContext(self.device, None)

        alcMakeContextCurrent(self.context)
        checkError("Init openAl")

        self._position = [0, 0, 0]
        self.setPosition(self._position)

    def setPosition(self, pos):
            self._position = pos
            x, y, z = pos
            alListener3f(AL_POSITION, x, y, z)
            checkError("Listener check position")

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
        checkError("Gen buffer")

        alBufferData(self.bufferId, alformat, wavbuf, len(wavbuf), samplerate)
        checkError("Fill buffer")

    def id(self):
        return self.bufferId

    def delete(self):
        alDeleteBuffers(1, self.bufferId)
        checkError("Delete buffer")

class SoundSource:
    def __init__(self, position) -> None:
        self.position = position
        
        self.source = ALuint(0)
        
        alGenSources(1, self.source)
        checkError("Gen source")

        alSourcef(self.source, AL_PITCH, 0.5)
        checkError("Set pitch")

        alSourcef(self.source, AL_GAIN, 1)
        checkError("Set gain")

        alSourcef(self.source, AL_ROLLOFF_FACTOR, 1)
        checkError("Set rolloff factor")

        alSourcef(self.source, AL_REFERENCE_DISTANCE, 50.0)
        checkError("Set reference distance")

        alSourcef(self.source, AL_MAX_DISTANCE, 100.0)
        checkError("Set max distance")

        alSource3f(self.source, AL_VELOCITY, 0, 0, 0)
        checkError("Set velocity")

        alSourcei(self.source, AL_LOOPING, AL_FALSE)
        checkError("Set looping")

        alSourcei(self.source, AL_SOURCE_RELATIVE, AL_FALSE)
        checkError("Set source relative")

    def setPosition(self, position):
        alSource3f(self.source, AL_POSITION, position[0], position[1], position[2])
        checkError("Set position")

    def play(self):
        alSourcePlay(self.source)
        checkError("Play source")

    def addSound(self, soundData):
        alSourceQueueBuffers(self.source, 1, soundData.id())
        checkError("Add sound to source")

    def isPlaying(self):
        state = ALint(0)

        alGetSourcei(self.source, AL_SOURCE_STATE, state)
        checkError("Check playing")

        return state.value == al.AL_PLAYING

    def delete(self):
        alDeleteSources(1, self.source)
        checkError("Delete sound")


def main():
    config = ResourceManager().get_json("configs/eirlab.json")
    
    listener = Listener()

    buffers = []
    sources = []
    for i in range(10):
        soundData = SoundData("out/speaker" + str(i) + ".wav")
        buffers.append(soundData)

        soundSource = SoundSource(config["speakerPosition"][i])
        soundSource.setPosition([10, 0, 0])

        sources.append(soundSource)
        soundSource.addSound(soundData)

        soundSource.play()

    listener.setPosition([0, 1, 0])

    for i in range(10):
        while sources[i].isPlaying():
            time.sleep(0.1)
        
    for i in range(10):
        sources[i].delete()
        buffers[i].delete()
    
    listener.delete()

main()