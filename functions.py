from dmx import Colour, DMXInterface, DMXUniverse, DMXLight4Slot
from dmx.colour import *
from dmx.light import *

import time
import numpy as np
import random

LIGHT_NUMBER = 54
LINE_NUMBER = 9
ROW_NUMBER = 6

def lights_up(universe, interface, color):
    lights = universe.get_lights()
    updates = []
    for i in np.around(np.arange(0.2, 1.2, 0.2)):
        for l in lights:
            l.set_colour(Colour(int(i*color[0]), int(i*color[1]), int(i*color[2]), int(i*color[3])))
        updates.append(universe.serialise())
    
    for u in updates:
        interface.set_frame(u)
        interface.send_update()

def lights_down(universe, interface, color):
    lights = universe.get_lights()
    updates = []
    for i in np.around(np.arange(0.8, -0.2, -0.2), 1):
        for l in lights:
            l.set_colour(Colour(int(i*color[0]), int(i*color[1]), int(i*color[2]), int(i*color[3])))
        updates.append(universe.serialise())
    
    for u in updates:
        interface.set_frame(u)
        interface.send_update()



def pulse_bpm(universe, interface, bpm):
    # send a pulse of light every bpm
    while True:
        a = time.time()
        pulse(universe, interface, bpm)
        b = time.time()

        time.sleep(60 / bpm - (b - a))


def pulse(universe, interface, duration):
    lights_up(universe, interface, WHITE.serialise())
    lights_down(universe, interface, WHITE.serialise())


def strobe(universe, interface):
    lights = universe.get_lights()
    i = 0
    while True:
        i += 1
        if i % 2 == 0:
            for l in lights:
                l.set_colour(WHITE)
        else:
            for l in lights:
                l.set_colour(BLACK)

        # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

        # Send an update to the DMX network
        interface.send_update()


def tamise(universe, interface):
    lights = universe.get_lights()
    for l in lights:
        l.set_colour(Colour(200, 50, 0, 100))

        # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()
    #light_test(universe, interface)

def white(universe, interface):
    lights = universe.get_lights()
    for l in lights:
        l.set_colour(Colour(150, 150, 100, 255))

        # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()
    #light_test(universe, interface)
    
def light_test(universe, interface):
    
    if universe.has_light_at_address(light_coord(1, 4)):
        universe.get_light_at_address(light_coord(1, 4)).set_colour(WHITE)
    else:
        universe.add_light(DMXLight4Slot(address=light_coord(2, 4)).set_colour(WHITE))

    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()


def rainbow_wave(universe, interface):
    lights = []
    rainbow_9_colors = [Colour(255, 0, 0), Colour(255, 127, 0), Colour(255, 255, 0), Colour(0, 255, 0),
                        Colour(0, 0, 255), Colour(75, 0, 130), Colour(143, 0, 255), Colour(255, 0, 255),
                        Colour(255, 0, 127)]
    states = []
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=light_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    for cycle in range(LINE_NUMBER):
        for i in range(LINE_NUMBER):
            # Change the color of the lights line by line
            for j in range(ROW_NUMBER):
                lights[i * ROW_NUMBER + j].set_colour(rainbow_9_colors[(i - cycle) % LINE_NUMBER])

            # Update the interface's frame to be the universe's current state
        states.append(universe.serialise())

    states.append(states[0])
    new_states = interpolate(states, 20)

    # print(new_states)
    while True:
        for s in new_states:
            interface.set_frame(s)
            interface.send_update()
        
def trans_flag(universe, interface):
    lights = []
    trans_color = [Colour(91, 206, 250, 0), Colour(91, 206, 250, 0), Colour(150, 20, 110, 50), Colour(150, 20, 110, 50), Colour(255, 255, 255, 100), Colour(150, 20, 110, 50), Colour(150, 20, 110, 50),Colour(91, 206, 250, 0),Colour(91, 206, 250, 0)]
    states = []
    for i in range(LIGHT_NUMBER):
        light = DMXLight4Slot(address=light_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    states = []
    for cycle in range(LINE_NUMBER):
        for i in range(LINE_NUMBER):
            # Change the color of the lights line by line
            for j in range(ROW_NUMBER):
                lights[i * ROW_NUMBER + j].set_colour(trans_color[(i - cycle) % LINE_NUMBER])

            # Update the interface's frame to be the universe's current state
        states.append(universe.serialise())

    states.append(states[0])
    new_states = interpolate(states, 20)
    while True:
        for s in new_states:
            interface.set_frame(s)
            interface.send_update()


def interpolate(tab, times):
    new_tab = []
    for i in range(len(tab) - 1):
        for j in np.linspace(tab[i], tab[i + 1], times, dtype=int).tolist():
            new_tab.append(j)
    return new_tab


def fireball_circle(universe, interface):
    path = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
        (8, 4), (8, 3), (8, 2), (8, 1), (8, 0),
        (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)
    ]

    coords = lambda x, y: light_map[x * ROW_NUMBER + y]
    lights = [DMXLight4Slot(address=coords(x, y)) for x, y in path]

    for l in lights:
        universe.add_light(l)

    current_light = 0

    # Turn off all lights
    for l in lights:
        l.set_colour(Colour(0, 0, 0, 0))
    interface.set_frame(universe.serialise())
    interface.send_update()

    while True:
        # For each light, make one of them red at a time
        for i in range(len(lights)):
            if i == current_light:
                # Turn on the current light
                lights[i].set_colour(RED)
            else:
                # If i is at a distance > 3 from the current light, turn it off
                # else, interpolate the color between red and black
                if (current_light - i) > 3:
                    lights[i].set_colour(Colour(0, 0, 0, 0))
                elif current_light - i > 0:
                    # The less i is from current_light, the more red it is
                    red = 255 // (current_light - i + 2)
                    lights[i].set_colour(Colour(red, 0, 0, 0))

        interface.set_frame(universe.serialise())
        interface.send_update()
        time.sleep(.05)

        current_light += 1
        current_light %= len(lights)
