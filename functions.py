from dmx import Colour, DMXInterface, DMXUniverse, DMXLight4Slot
from dmx.colour import WHITE
from dmx.light import ligh_map

import time

LIGHT_NUMBER = 54
LINE_NUMBER = 9
ROW_NUMBER = 6

def light_test(universe, interface):
    light = DMXLight4Slot(address=ligh_map[12])
    light.set_colour(WHITE)
    universe.add_light(light)
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

def rainbow(universe, interface):
    lights = []
    rainbow_9_colors = [Colour(255, 0, 0), Colour(255, 127, 0), Colour(255, 255, 0), Colour(0, 255, 0), Colour(0, 0, 255), Colour(75, 0, 130), Colour(143, 0, 255), Colour(255, 0, 255), Colour(255, 0, 127)]
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=ligh_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    for i in range(LINE_NUMBER):
        # Change the color of the lights line by line
        for j in range(ROW_NUMBER):
            lights[i * ROW_NUMBER + j].set_colour(rainbow_9_colors[i])

        # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

        # Send an update to the DMX network
        interface.send_update()

        time.sleep(0.5 - (15.0 / 1000.0))



def light_up_by_line(universe, interface):
    lights = []
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=ligh_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    for i in range(LINE_NUMBER):
        # Change the color of the lights line by line
        for j in range(ROW_NUMBER):
            lights[i * ROW_NUMBER + j].set_colour(WHITE)

        # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

        # Send an update to the DMX network
        interface.send_update()

        time.sleep(0.5 - (15.0 / 1000.0))


