from dmx.colour import *
from dmx.light import *
from dmx.universe import *
from dmx.interface import *
import threading
import time
import numpy as np
import random

LIGHT_NUMBER = 54
LINE_NUMBER = 9
ROW_NUMBER = 6

def set_universe_color(universe, color):
    lights = universe.get_lights()
    for l in lights:
        l.set_colour(color)

def set_lights_color(lights, color):
    for l in lights:
        l.set_colour(color)

def interpolate(frames, times):
    new_frames = []
    for i in range(len(frames) - 1):
        for j in np.linspace(frames[i], frames[i + 1], times, dtype=int).tolist():
            new_frames.append(j)
    return new_frames

def lights_up(universe, interface, color, times):
    
    lights = universe.get_lights()
    updates = []
    for i in range(2):
        set_universe_color(universe, Colour(int(i*color[0]), int(i*color[1]), int(i*color[2]), int(i*color[3])))
        updates.append(universe.serialise())
    
    updates = interpolate(updates, times)
    
    for u in updates:
        interface.set_frame(u)
        interface.send_update()

def lights_down(universe, interface, color, times):
    lights = universe.get_lights()
    updates = []
    
    for i in range(1, -1, -1):
        set_universe_color(universe, Colour(int(i*color[0]), int(i*color[1]), int(i*color[2]), int(i*color[3])))
        updates.append(universe.serialise())
    
    updates = interpolate(updates, times)
    
    for u in updates:
        interface.set_frame(u)
        interface.send_update()
