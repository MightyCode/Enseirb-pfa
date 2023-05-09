from interface.python.Interface import Interface
from interface.python.audio.SoundInterface import SoundInterface
from interface.python.audio.players.PlayerInterface import PlayerInterface
from interface.python.audio.players.RealPlayer import RealPlayer

import threading, sys, time
import argparse

initialized: list = []
ended: list = []
joined: list = []
parser = argparse.ArgumentParser(description='My Python Script')
parser.add_argument('path', type=str, help='path of the project')
parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose mode')
parser.add_argument('-l', '--light', action='store_true', help='use only light interface')
parser.add_argument('-s', '--sound', action='store_true', help='use only sound interface')
parser.add_argument('-p', '--precompute', action='store_true', help='do precompute only')
parser.add_argument('-b', '--begin', type=float, help='begin time (in seconds)')
args = parser.parse_args()


stop_flag = threading.Event()

def run_interface(id: int, interface: Interface, path: str, start_time: str):
    # create interface object

    # read project and load custom effects
    interface.read_project(path)

    # precompute
    interface.pre_compute()
    initialized[id] = True

    if args.precompute:
        ended[id] = True
        return


    can_go: bool = False
    while not can_go:
        can_go = True
        for i in range(len(initialized)):
            if not initialized[i]:
                can_go = False

    # run scenario
    interface.do_scenarii(start_time)
    ended[id] = True

# main thread
if __name__ == '__main__':
    # get project path
    path = sys.argv[1]

    # create two threads for the workers 
    threads = []

    start: float = args.begin if args.begin else 0
    print("Start simulation at " + str(start))

    if args.sound or not args.light:
        sound_interface: Interface = SoundInterface(stop_flag, verbose=args.verbose)
        real_player: PlayerInterface = RealPlayer('test',stop_flag)
        sound_interface.attach_player(real_player)
        soundInterfaceThread = threading.Thread(target=run_interface, args=(0, sound_interface, path, start, ))
        threads.append(soundInterfaceThread)

    if args.light or not args.sound:
        pass 

    """
    Do the same for audio
    """

    for t in threads:
        initialized.append(False)
        ended.append(False)
        joined.append(False)

    for t in threads:
        t.start()

    num_joined: int = 0

    try:
        while num_joined != len(joined):
            for i in range(len(initialized)):
                if ended[i] and not joined[i]:
                    threads[i].join()
                    joined[i] = True
                    num_joined += 1

            time.sleep(0.1)
    except KeyboardInterrupt:
        stop_flag.set()
        print("Exiting...")

