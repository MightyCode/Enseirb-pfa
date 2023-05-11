import numpy as np
import librosa
import sounddevice as sd
import scipy.signal as signal
import os
import threading
from dmx import *
from dmx.LightEffects import NUMBER_OF_LIGHTS, light_map, light_coord_to_id, WHITE, BLACK

interface = DMXInterface("FT232R")

def low_pass_filter(data, samplerate, cutoff_freq):
    aplha = 1/samplerate * cutoff_freq / (1+(1/samplerate)*cutoff_freq)
    y = [aplha*data[0][0]]
    for i in range(1, len(data)):
        y.append(aplha*data[i][0] + (1-aplha)*y[i-1])
    return y

def high_pass_filter(data, samplerate, cutoff_freq):
    pass



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
    universe.add_light(DMXLight4Slot(address=light_coord_to_id(4, 2)))
    effect = LightEffects(universe, interface)
    for i in range(NUMBER_OF_LIGHTS):
        universe2.add_light(DMXLight4Slot(address=light_map[i]))

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
                effect.lights_up((255, 255, 255, 255), 4)
                effect.execute_light_effect()
                lights_on = True
            elif fifo[l % sample_timpe] < np.mean(fifo)/1.3 and lights_on:
                print("Off", l)
                effect.lights_down((0, 0, 0, 0), 4)
                effect.execute_light_effect()
                lights_on = False
            l += 1


live_process()
