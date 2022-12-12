
import numpy as np
import librosa
import playsound
import sounddevice as sd
from functions import *
import scipy.signal as signal

def tempo(file_name):
    # load the audio file
    y, sr = librosa.load(file_name)

    # compute the beat times
    tempo, beat_times = librosa.beat.beat_track(y=y, sr=sr)

    print("tempo: ", tempo )
    playsound.playsound(file_name, False)
    with DMXInterface("FT232R") as interface:
        # Create a universe
        print("Doing Magic...")
        universe = DMXUniverse()
        pulse_bpm(universe, interface, tempo)

def live_process():
    """
    process microphone input in real time and call function "pulse" when a beat is detected
    """
    samplerate = 44100
    cutoff_freq = 500
    mic = sd.InputStream(samplerate=samplerate, channels=1)
    with mic:
        print("Listening...")
        while True:
            aplha = 1/samplerate * cutoff_freq / (1+(1/samplerate)*cutoff_freq)
            data = mic.read(1024)[0]
            y = [aplha*data[0][0]]
            for i in range(1, len(data)):
                y.append(aplha*data[i][0] + (1-aplha)*y[i-1])
        
        # print decibel value
            print(20*np.log10(np.sqrt(np.mean(np.square(y)))))
            if 20*np.log10(np.sqrt(np.mean(np.square(y)))) > -10:
                print("beat detected")
                with DMXInterface("FT232R") as interface:
                    # Create a universe
                    print("Doing Magic...")
                    universe = DMXUniverse()
                    pulse(universe, interface, 0.5)






tempo('/home/juliench/Téléchargements/Michael Jackson - Billie Jean.mp3')
#live_process()

