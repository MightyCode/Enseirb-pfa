from interface.python.ResourceManager import ResourceManager
from openal import *

import time
import wave


def main():
    device = alcOpenDevice(None)
    if not device:
        error = alcGetError()
        # do something with the error, which is a ctypes value
        return -1
    
    # Omit error checking
    context = alcCreateContext(device, None)
    alcMakeContextCurrent(context)

    config = ResourceManager.getJson("configs/eirlab")
    sources = []

    for i in range(10):
        data = wave.open("out/speaker" + str(i) + ".wav")

        source = ALuint(0)
        sources.append(source)

        # Do more things
        alGenSources(1, source)
        alSourcef(source, AL_PITCH, 1)
        alSourcef(source, AL_GAIN, 1)
        alSource3f(source, AL_POSITION, 10, 0, 0)
        alSource3f(source, AL_VELOCITY, 0, 0, 0)
        alSourcei(source, AL_LOOPING, 1)

    alSourcePlay(source)

    alDeleteSources(1, source)
    alcDestroyContext(context)
    alcCloseDevice(device)
    return 0

main()
"""
# Load the WAV file using SoundFile
data, samplerate = sf.read('interface/python/audio/sound/vache.wav')

# Create an OpenAL context and listener
device = openal.Device()
context = device.create_context()
listener = openal.Listener()

# Create an OpenAL buffer and source
buffer = openal.Buffer(data)
source = openal.Source()

# Set the position of the source
source.position = (0, 0, 0)  # Replace with your desired position

# Queue the buffer to the source
source.queue(buffer)

# Play the source
source.play()

# Wait for the sound to finish playing
while source.get_state() == openal.AL_PLAYING:
    pass

# Cleanup
source.delete()
buffer.delete()
context.delete()
device.close()"""