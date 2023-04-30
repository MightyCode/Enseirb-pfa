from dmx.LightEffects import *

with DMXInterface("FT232R") as interface:
    universe = DMXUniverse()
    for i in range(NUMBER_OF_LIGHTS):
            universe.add_light(DMXLight4Slot(address=light_map[i]))

    