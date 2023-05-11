from dmx import *
from dmx.LightEffects import NUMBER_OF_LIGHTS, light_map

universe = DMXUniverse()
interface = DMXInterface("FT232R")

for i in range(NUMBER_OF_LIGHTS):
    universe.add_light(DMXLight4Slot(address=light_map[i]))

effect = LightEffects(universe, interface)

#effect.rainbow_wave_effect(3)
#effect.execute_light_effect()
effect.soft_white_effect()
effect.execute_light_effect()