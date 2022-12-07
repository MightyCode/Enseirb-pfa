from dmx import Colour, DMXInterface, DMXUniverse, DMXLight4Slot
from dmx.colour import *
from dmx.light import *

import time

LIGHT_NUMBER = 54
LINE_NUMBER = 9
ROW_NUMBER = 6

def strobe(universe, interface):
    lights = []
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=ligh_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)
    i = 0
    while True:
        i+=1
        if i%2 == 0:
            for l in lights:
                l.set_colour(Colour(255, 255, 255, 100))
        else:
            for l in lights:
                l.set_colour(Colour(0, 0, 0, 0))

        # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

        # Send an update to the DMX network
        interface.send_update()


def tamise(universe, interface):
    lights = []
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=ligh_map[i])
        light.set_colour(Colour(200, 50, 0, 100))
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

        # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

        # Send an update to the DMX network
    interface.send_update()
    light_test(universe, interface)
    
def light_test(universe, interface):
    
    if universe.has_light_at_address(light_coord(0, 1)):
        universe.get_light_at_address(light_coord(0, 1)).set_colour(WHITE)
    else:
        universe.add_light(DMXLight4Slot(address=light_coord(0, 1)).set_colour(WHITE))


    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

def RGB_fade_loop(universe, interface):
    lights = []
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=ligh_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    red = 0
    green = 0
    blue = 0
    while True:
        for i in range(LIGHT_NUMBER):
            lights[i].set_colour(Colour(red, green, blue, 50))
        interface.set_frame(universe.serialise())
        interface.send_update()

        if green == 0 and red < 255:
            red += 5
        if red == 255 and green < 255:
            green += 5
        if green == 255 and blue == 0:
            red -= 5
        if red == 0 and blue < 255:
            blue += 5
        if blue == 255 and green > 0:
            green -= 5
        if green == 0 and blue == 255:
            red += 5
        if red == 255 and blue > 0:
            blue -= 5
        
        time.sleep(0.001)

        

def rainbow_wave(universe, interface):
    lights = []
    rainbow_9_colors = [Colour(255, 0, 0), Colour(255, 127, 0), Colour(255, 255, 0), Colour(0, 255, 0), Colour(0, 0, 255), Colour(75, 0, 130), Colour(143, 0, 255), Colour(255, 0, 255), Colour(255, 0, 127)]
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=ligh_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    cycle = 0
    while True:
        for i in range(LINE_NUMBER):
            # Change the color of the lights line by line
            for j in range(ROW_NUMBER):
                lights[i * ROW_NUMBER + j].set_colour(rainbow_9_colors[(i - cycle) % LINE_NUMBER])

            # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

            # Send an update to the DMX network
        interface.send_update()

        time.sleep(0.2)
        cycle+= 1

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


