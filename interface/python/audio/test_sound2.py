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
import threading

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('filename', help='audio file to be played back')
parser.add_argument(
    '-b', '--buffersize', type=int, default=20,
    help='number of blocks used for buffering (default: %(default)s)')
parser.add_argument('-c', '--clientname', default='file player',
                    help='JACK client name')
parser.add_argument('-m', '--manual', action='store_true',
                    help="don't connect to output ports automatically")
args = parser.parse_args()
if args.buffersize < 1:
    parser.error('buffersize must be at least 1')

q = queue.Queue(maxsize=args.buffersize)
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
    if frames != blocksize:
        stop_callback('blocksize must not be changed, I quit!')
    try:
        data = q.get_nowait()
    except queue.Empty:
        stop_callback('Buffer is empty: increase buffersize?')
    if data is None:
        stop_callback()  # Playback is finished
    

    side = 0
    for i in range(len(client.outports)):
        #print(data.T, len(data.T[0]), data.T[0])

        client.outports[i].get_array()[:] = data.T[side] 
        side = (len(data.T) - 1) - side
        
try:
    import jack
    import soundfile as sf

    print("Create jack client")
    client = jack.Client(args.clientname)
    print("Jack client created")

    print(client)
    print(client.outports)
    print(len(client.outports))

    print(f'buff:{args.buffersize}')

    blocksize = client.blocksize
    samplerate = client.samplerate
    client.set_xrun_callback(xrun)
    client.set_shutdown_callback(shutdown)
    client.set_process_callback(process)

    print(blocksize, samplerate)

    with sf.SoundFile(args.filename) as f:
        block_generator = f.blocks(blocksize=blocksize, dtype='float32', always_2d=True, fill_value=0)
        print("generator created")
        for _, data in zip(range(args.buffersize), block_generator):
            q.put_nowait(data)  # Pre-fill queue
        print("Pre-filled queue")

        with client:
            if not args.manual:
                target_ports = client.get_ports(
                    is_physical=True, is_input=True, is_audio=True)
                print(target_ports)
                for i in range(len(target_ports)):
                    client.outports.register(f'out_{i}')
                    client.outports[i].connect(target_ports[i])

            print("Target connected to source")
            timeout = blocksize * args.buffersize / samplerate
            #for data in block_generator:
                #q.put(data, timeout=timeout)
                
            q.put(None, timeout=timeout)  # Signal end of file
            event.wait()  # Wait until playback is finished
except KeyboardInterrupt:
    parser.exit('\nInterrupted by user')
except (queue.Full):
    # A timeout occured, i.e. there was an error in the callback
    parser.exit(1)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))