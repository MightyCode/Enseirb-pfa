import sys
import os

# Add the root folder to the module search path
root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from aubio import source, onset
from os import path
from os import system
from pydub import AudioSegment
import threading
import time
from pygame import mixer
import subprocess
import librosa
from functions import *



frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second

def nothing():
    while True:
        print()
        time.sleep(0.05)
    
        

def convert_to_wav(file_path):
    # files                                                                         
    src = file_path+".mp3"
    dst = file_path+".wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

def tempo(file_name):
    # load the audio file
    y, sr = librosa.load(file_name)

    # compute the beat times
    tempo, beat_times = librosa.beat.beat_track(y=y, sr=sr)

    return tempo

def get_onset_times(file_path, file_name):
    window_size = 1024 # FFT size
    hop_size = window_size // 4
    beat = tempo(file_path)
    sample_rate = 0
    src_func = source(file_path, sample_rate, hop_size)
    sample_rate = src_func.samplerate
    #onset_func = onset('hfc', window_size, hop_size, t)
    #onset_func = system("aubioonset -i "+file_name+".mp3 -B 1024 -H 256 -M 0.3 > "+file_name+".txt")
    onset_func = str(subprocess.check_output("aubioonset -i "+file_name+".mp3 -B 1024 -H 256 -t 0.7 -M "+str(60/beat/1.3), shell=True)).split("\\n")
    onset_func.pop(0)
    onset_func.pop(-1)
    #print(onset_func)
    onset_func = [float(numeric_string) for numeric_string in onset_func]
    print(onset_func)

    """ onset_times = [] # seconds
    while True: # read frames
        samples, num_frames_read = src_func()
        if onset_func(samples):
            onset_time = onset_func.get_last_s()
            if onset_time < duration:
                onset_times.append(onset_time)
            else:
                break
        if num_frames_read < hop_size:
            break """
    
    #return onset_times
    return onset_func


def main():
    threading.Thread(target=nothing).start()
    file_path = 'Queen.mp3'
    # remove extension, .mp3, .wav etc.
    file_name_no_extension, extension = path.splitext(file_path)
    print(file_name_no_extension, extension)
    if extension != '.wav':
        convert_to_wav(file_name_no_extension)
        file_path = file_name_no_extension + '.wav'
    onset_times = get_onset_times(file_path, file_name_no_extension)
    #Instantiate mixer
    mixer.init()

    #Load audio file
    mixer.music.load(file_path)

    print("music started playing....")

    #Set preferred volume
    mixer.music.set_volume(1)

    #Play the music
    mixer.music.play()
    cursor = 0
    while True:
        if round(mixer.music.get_pos()/1000, 2) == round(onset_times[cursor], 2):
            print("beat")
            lights_up(universe, interface, WHITE.serialise())
            time.sleep(0.01)
            lights_down(universe, interface, WHITE.serialise())
            cursor += 1
            if cursor == len(onset_times):
                break


interface = DMXInterface("FT232R")
universe2 = DMXUniverse()
universe = DMXUniverse()
for i in range(NUMBER_OF_LIGHTS):
    universe2.add_light(DMXLight4Slot(address=light_map[i]))
soft_white_effect(universe2, interface)
universe.add_light(DMXLight4Slot(address=light_coord_to_id(3, 8)))

main()