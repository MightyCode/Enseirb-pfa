import numpy as np
import librosa
import playsound
import sounddevice as sd
from functions import *
import scipy.signal as signal
import os
import threading

interface = DMXInterface("FT232R")

def low_pass_filter(data, samplerate, cutoff_freq):
    aplha = 1/samplerate * cutoff_freq / (1+(1/samplerate)*cutoff_freq)
    y = [aplha*data[0][0]]
    for i in range(1, len(data)):
        y.append(aplha*data[i][0] + (1-aplha)*y[i-1])
    return y

def high_pass_filter(data, samplerate, cutoff_freq):
    pass


def tempo(file_name):
    # load the audio file
    y, sr = librosa.load(file_name)

    # compute the beat times
    tempo, beat_times = librosa.beat.beat_track(y=y, sr=sr)

    print("tempo: ", tempo)
    playsound.playsound(file_name, False)
    # playsound with os.system("mpg123 " + file_name) in background
    # os.system("mpg123 " + file_name + " &")
    # Create a universe
    print("Doing Magic...")
    universe = DMXUniverse()
    pulse_bpm(universe, interface, tempo)


def live_process():
    """
    process microphone input in real time and make a pulse when a peak is detected
    """
    samplerate = 44100
    cutoff_freq = 25
    sample_timpe = 20
    mic = sd.InputStream(samplerate=samplerate, channels=1)

    universe2 = DMXUniverse()
    universe = DMXUniverse()
    for i in range(LIGHT_NUMBER):
        universe2.add_light(DMXLight4Slot(address=light_map[i]))
    white(universe2, interface)
    universe.add_light(DMXLight4Slot(address=light_coord(2, 4)))

    with mic:
        print("Listening...")
        # create fifo of sample_timpe elements
        fifo = [0]*sample_timpe
        l = 0
        lights_on = False
        while True:
            data = mic.read(1024)[0]

            y = low_pass_filter(data, samplerate, cutoff_freq)

            # add new value to fifo
            fifo[l % sample_timpe] = 20*np.log10(np.sqrt(np.mean(np.square(y))))
            print(fifo[l % sample_timpe], np.mean(fifo)/1.3)

            # if last value is superior to the average of the 100 last values, then a beat is detected
            if fifo[l % sample_timpe] > np.mean(fifo)/1.3 and not lights_on:
                print("On")
                lights_up(universe, interface, WHITE.serialise())
                lights_on = True
            elif fifo[l % sample_timpe] < np.mean(fifo)/1.3 and lights_on:
                print("Off", l)
                lights_down(universe, interface, WHITE.serialise())
                lights_on = False
            l += 1


#tempo('/home/juliench/Téléchargements/Michael Jackson - Billie Jean.mp3')
live_process()
