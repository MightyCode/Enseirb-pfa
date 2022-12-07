# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dmx import DMXInterface, DMXLight3Slot, DMXUniverse, Colour
import time
import random

light_number = 54

# Open an interface
with DMXInterface("FT232R") as interface:
    # Define DMX universe
    universe = DMXUniverse()

    # Define DMX lights
    lights = []
    for i in range(light_number):
        light = DMXLight3Slot(address=1)
        lights.append(light)
        universe.add_light(light)



    # Play lights randomly for a bit
    for _ in range(2000):
        for light in lights:
            random_colour = Colour(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            light.set_colour(random_colour)

        interface.set_frame(universe.serialise())
        interface.send_update()

        time.sleep(0.5 - (15.0 / 1000.0))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
