#!/usr/bin/env python3

"""Play a sound file.

This only reads a certain number of blocks at a time into memory,
therefore it can handle very long files and also files with many
channels.

NumPy and the soundfile module (http://PySoundFile.rtfd.io/) must be
installed for this to work.

"""
import argparse
try:
    import queue  # Python 3.x
except ImportError:
    import Queue as queue  # Python 2.x
import sys
import os
import threading

buffersize = 20
event = threading.Event()

def print_error(*args):
    print(*args, file=sys.stderr)


def xrun(delay):
    print_error("An xrun occured, increase JACK's period size?")


def shutdown(status, reason):
    print_error('JACK shutdown!')
    print_error('status:', status)
    print_error('reason:', reason)
    event.set()


def stop_callback(msg=''):
    if msg:
        print_error(msg)
    for port in client.outports:
        port.get_array().fill(0)
    event.set()
    raise jack.CallbackExit


def process(frames):
    side = 0
    for i in range(len(client.outports)):
        if frames != blocksize:
            stop_callback('blocksize must not be changed, I quit!')
        try:
            if(i%2 == 0):
                data = queues[int(i//2)].get_nowait()
            #print(f'queue {i} : {len(data)}')
        except queue.Empty:
            stop_callback('Buffer is empty: increase buffersize?')
            stop_callback()  # Playback is finished
        if(i==0):
            print(f'queue {i} : {queues[int(i//2)].qsize()}')
        client.outports[i].get_array()[:] = data.T[side] 
        side = (len(data.T) - 1) - side
        
import jack
import soundfile as sf

client = jack.Client('test')

blocksize = client.blocksize
samplerate = client.samplerate
client.set_xrun_callback(xrun)
client.set_shutdown_callback(shutdown)
client.set_process_callback(process)

print(f'blocksize : {blocksize}, samplerate : {samplerate}')

filenames = os.listdir('out')
filenames.sort()

block_generators = []
queues = []

for filename in filenames:
    f = sf.SoundFile('out/'+filename)
    block_generators.append(f.blocks(blocksize=blocksize, dtype='float32', always_2d=True, fill_value=0))
    queues.append(queue.Queue(maxsize=blocksize))
    for data in block_generators[-1]:
        queues[-1].put_nowait(data)  # Pre-fill queue

print("All generators created and queues prefilled")

with client:
    target_ports = client.get_ports(
        is_physical=True, is_input=True, is_audio=True)
    for i in range(len(target_ports)):
        client.outports.register(f'out_{i}')
        client.outports[i].connect(target_ports[i])

    print("Target connected to source")
    
    for q in queues:
        q.put_nowait(None)
        

