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
        elif argv[1] == "test":
            light_test(universe, interface)
        elif argv[1] == "wave":
            rainbow_wave(universe, interface)
        elif argv[1] == "pulse":
            pulse(universe, interface)
        elif argv[1] == "dust":
            pulse_bpm(universe, interface, 110)
        elif argv[1] == "nico":
            trans_flag(universe, interface)
        print("Magic Done")

