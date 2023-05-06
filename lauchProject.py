import threading, sys, time
from interface.python.Interface import Interface
from interface.python.audio.SoundInterface import SoundInterface

initialized: list = []
ended: list = []
joined: list = []

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
    ended[id] = True

# main thread
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python lauchProject.py path/to/project")
        sys.exit()

    # get project path
    path = sys.argv[1]

    # create two threads for the workers
    threads = []

    soundInterface: Interface = SoundInterface()
    soundInterfaceThread = threading.Thread(target=run_interface, args=(0, soundInterface, path,))
    threads.append(soundInterfaceThread)

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

    while num_joined != len(joined):
        for i in range(len(initialized)):
            if ended[i] and not joined[i]:
                threads[i].join()
                joined[i] = True
                num_joined += 1

        time.sleep(0.1)