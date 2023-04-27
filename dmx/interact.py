from dmx.color import *
from dmx.light import *
from dmx.universe import *
from dmx.interface import *
import threading
import time
import numpy as np
import random

NUMBER_OF_LIGHTS = 54
NUMBER_OF_ROWS = 9
NUMBER_OF_COLUMNS = 6


def set_lights_color(lights, color):
    for l in lights:
        l.set_colour(color)

def set_universe_color(universe, color):
    lights = universe.get_lights()
    set_lights_color(lights, color)
        
def interpolate(frames, times):
    new_frames = []
    for i in range(len(frames) - 1):
        for j in np.linspace(frames[i], frames[i + 1], times, dtype=int).tolist():
            new_frames.append(j)
    return new_frames


def lights_transition(universe, interface, target_color, interpolation_rate):
    """
    Transitions the lights in the universe to the target color over interpolation_rate frames.

    Args:
        universe (DMXUniverse): lights to transition
        interface (DMXInterface): interface to send the updates
        target_color (list[int]): RGBW color to transition to
        interpolation_rate (int): number of frames appearing during the transition
    """
    lights = universe.get_lights()
    current_color = (lights[0].get_colour()).serialise()
    frames = interpolate([current_color, target_color], interpolation_rate)
    for frame in frames:
        set_universe_color(universe, Color(*frame))
        interface.set_frame(universe.serialise())
        interface.send_update()

