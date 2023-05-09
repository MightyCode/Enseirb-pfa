import sys
import os

# Add the root folder to the module search path
root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from interface.python.audio.players.RealPlayer import RealPlayer

if __name__ == '__main__':
    r = RealPlayer('test', 0)
    start_time : int = 5
    r.play([],start_time,48000)