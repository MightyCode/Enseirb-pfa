from dmx.effect import *

with DMXInterface("FT232R") as interface:
    universe = DMXUniverse()
    for i in range(LIGHT_NUMBER):
            universe.add_light(DMXLight4Slot(address=light_map[i]))

    tamise(universe, interface)
    white(universe, interface)