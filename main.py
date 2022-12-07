# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dmx import DMXInterface, DMXLight3Slot, DMXUniverse, Colour
from functions import *


if __name__ == '__main__':
    with DMXInterface("FT232R") as interface:
        # Create a universe
        universe = DMXUniverse()
        #light_test(universe, interface)
        #light_up_by_line(universe, interface)
        rainbow(universe, interface)


