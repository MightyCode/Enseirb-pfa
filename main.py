# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dmx import DMXInterface, DMXUniverse, Colour
from functions import *
from sys import *


if __name__ == '__main__':
    with DMXInterface("FT232R") as interface:
        # Create a universe
        print("Doing Magic...")
        universe = DMXUniverse()
        if argv[1] == "tamise":
            tamise(universe, interface)
        elif argv[1] == "strobe":
            strobe(universe, interface)
        elif argv[1] == "light_test":
            light_test(universe, interface)
        elif argv[1] == "loop":
            RGB_fade_loop(universe, interface)
        elif argv[1] == "wave":
            rainbow_wave(universe, interface)
        print("Magic Done")

