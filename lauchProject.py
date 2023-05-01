from code import interact
import threading
import sys
from interface.python.Interface import Interface
from interface.python.audio.SoundCreation import SoundCreation

initialized = []

def run_interface(id: int, interface: Interface, path: str):
    # create interface object

    # read project and load custom effects
    interface.read_project(path)

    # precompute
    interface.pre_compute()

    initialized[id] = True
    can_go: bool = False
    while not can_go:
        can_go = True
        for i in range(len(initialized)):
            if not initialized[i]:
                can_go = False

    # run scenario
    interface.do_scenarii()

# main thread
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python lauchProject.py path/to/project")
        sys.exit()

    # get project path
    path = sys.argv[1]

    # create two threads for the workers
    threads = []

    soundInterface: Interface = SoundCreation()
    soundInterfaceThread = threading.Thread(target=run_interface, args=(0, soundInterface, path,))
    threads.append(soundInterfaceThread)
    initialized.append(False)

    """
    Do the same for audio
    """

    for t in threads:
        t.start()

    # join the threads
    for t in threads:
        t.join()