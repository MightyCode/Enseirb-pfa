from functions import *
from sys import *


if __name__ == '__main__':
    with DMXInterface("FT232R") as interface:

        # Create a universe
        print("Doing Magic...")
        universe = DMXUniverse()
        for i in range(NUMBER_OF_LIGHTS):
            universe.add_light(DMXLight4Slot(address=light_map[i]))
            
        if argv[1] == "tamise":
            dim_effect(universe, interface)
        elif argv[1] == "strobe":
            strobe_effect(universe, interface)
        elif argv[1] == "test":
            light_test(universe, interface)
        elif argv[1] == "wave":
            rainbow_wave_effect(universe, interface)
        elif argv[1] == "pulse":
            pulse_effect(universe, interface)
        elif argv[1] == "dust":
            pulse_bpm(universe, interface, 110)
        elif argv[1] == "nico":
            trans_flag(universe, interface)
        elif argv[1] == "fireball":
            fireball_circle_effect(universe, interface)
        print("Magic Done")

