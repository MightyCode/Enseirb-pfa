from time import sleep
import random
from dmx.color import *
from dmx.light import *
from dmx.universe import *
from dmx.interface import *
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



def pulse_effect(universe, interface, color, interpolation_rate):
    """Pulses the lights in the universe once to the given color and interpolation rate.

    Args:
        universe (DMXUniverse): lights to transition
        interface (DMXInterface): interface to send the updates
        color (Color): RGBW color to pulse to
        interpolation_rate (int): number of frames appearing during the transition
    """
    lights_transition(universe, interface, color.serialise(), interpolation_rate)
    lights_transition(universe, interface, BLACK.serialise(), interpolation_rate)
    
def pulse_in_rythm(beat, universe, interface, color):
    lights_transition(universe, interface, color.serialise(), 1)
    sleep(beat)
    lights_transition(universe, interface, BLACK.serialise(), 1)

def pulse_rainbow_effect(universe, interface, interpolation_rate, number_of_pulses):
    """Pulses a rainbow effect on the lights in the universe.

    Args:
        universe (DMXUniverse): lights to transition
        interface (DMXInterface): interface to send the updates
        interpolation_rate (int): number of frames appearing during the transition
        time_length (int): time length of the effect in seconds
    """
    rainbow_colors = [Color(255, 0, 0), Color(255, 127, 0), Color(255, 255, 0),
                      Color(0, 255, 0), Color(0, 0, 255), Color(75, 0, 130),
                      Color(143, 0, 255), Color(255, 0, 255), Color(255, 0, 127)]


    for _ in range(number_of_pulses):
        for color in rainbow_colors:
            lights_transition(universe, interface, color.serialise(), interpolation_rate)
            lights_transition(universe, interface, BLACK.serialise(), interpolation_rate)
        

def fading_rainbow_effect(universe, interface, fade_speed, number_of_fades):
    """Creates a fading rainbow effect on the lights in the universe.

    Args:
        universe (DMXUniverse): lights to transition
        interface (DMXInterface): interface to send the updates
        fade_speed (float): speed of the fading effect (higher values for faster fading)
    """
    rainbow_colors = [Color(255, 0, 0), Color(255, 127, 0), Color(255, 255, 0),
                      Color(0, 255, 0), Color(0, 0, 255), Color(75, 0, 130),
                      Color(143, 0, 255), Color(255, 0, 255), Color(255, 0, 127)]

    fade_interval = int(fade_speed * 10)

    for _ in range(number_of_fades):
        for color in rainbow_colors:
            lights_transition(universe, interface, color.serialise(), fade_interval)

        for color in reversed(rainbow_colors):
            lights_transition(universe, interface, color.serialise(), fade_interval)


import random

def color_flicker_effect(universe, interface, flicker_speed, flicker_intensity, number_of_flickers):
    """Creates a color flicker effect on the lights in the universe.

    Args:
        universe (DMXUniverse): lights to transition
        interface (DMXInterface): interface to send the updates
        flicker_speed (float): speed of the flickering effect (higher values for faster flickering)
        flicker_intensity (float): intensity of the flickering effect (values between 0 and 1)
    """
    fade_interval = int(flicker_speed * 10)

    for _ in range(number_of_flickers):
        random_color = Color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        flicker_color = random_color * flicker_intensity

        lights_transition(universe, interface, flicker_color.serialise(), fade_interval)


def strobe_effect(universe, interface, number_of_strobes):
    i = 0
    while i < number_of_strobes:
        i += 1
        if i % 2 == 0:
            set_universe_color(universe, WHITE)
        else:
            set_universe_color(universe, BLACK)

        interface.set_frame(universe.serialise())
        interface.send_update()


def dim_effect(universe, interface):
    lights_transition(universe, interface, Color(200, 50, 0, 100).serialise(), 10)


def soft_white_effect(universe, interface):
    lights_transition(universe, interface, Color(150, 150, 100, 255).serialise(), 10)
    

def light_test(universe, interface):
    
    if universe.has_light_at_address(light_coord_to_id(1, 4)):
        universe.get_light_at_address(light_coord_to_id(1, 4)).set_colour(WHITE)
    else:
        universe.add_light(DMXLight4Slot(address=light_coord_to_id(2, 4)).set_colour(WHITE))

    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()
    

def random_color_change_effect(universe, interface, change_interval, number_of_changes):
    """Applies random color changes to each individual light in the universe.

    Args:
        universe (DMXUniverse): lights to transition
        interface (DMXInterface): interface to send the updates
        change_interval (float): interval between color changes (in seconds)
    """
    for _ in range(number_of_changes):
        for light in universe.lights:
            random_color = Color(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            light.set_colour(random_color)
        
        interface.set_frame(universe.serialise())
        interface.send_update()
        
        time.sleep(change_interval)



def rainbow_wave_effect(universe, interface, number_of_waves):
    lights = []
    rainbow_9_colors = [Color(255, 0, 0), Color(255, 127, 0), Color(255, 255, 0), Color(0, 255, 0),
                        Color(0, 0, 255), Color(75, 0, 130), Color(143, 0, 255), Color(255, 0, 255),
                        Color(255, 0, 127)]
    states = []
    for i in range(NUMBER_OF_LIGHTS):
        light = DMXLight4Slot(address=light_map[i])
        # Add the light to a universe
        universe.add_light(light)
        lights.append(light)

    for cycle in range(NUMBER_OF_ROWS):
        for i in range(NUMBER_OF_ROWS):
            # Change the color of the lights line by line
            for j in range(NUMBER_OF_COLUMNS):
                lights[i * NUMBER_OF_COLUMNS + j].set_colour(rainbow_9_colors[(i - cycle) % NUMBER_OF_ROWS])

            # Update the interface's frame to be the universe's current state
        states.append(universe.serialise())

    states.append(states[0])
    new_states = interpolate(states, 20)

    # print(new_states)
    for _ in range(number_of_waves):
        for s in new_states:
            interface.set_frame(s)
            interface.send_update()


def fireball_circle_effect(universe, interface, number_of_fades):
    path = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
        (8, 4), (8, 3), (8, 2), (8, 1), (8, 0),
        (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)
    ]

    coords = lambda x, y: light_map[x * NUMBER_OF_COLUMNS + y]
    lights = [DMXLight4Slot(address=coords(x, y)) for x, y in path]

    for l in lights:
        universe.add_light(l)

    current_light = 0

    # Turn off all lights
    for l in lights:
        l.set_colour(Color(0, 0, 0, 0))
    interface.set_frame(universe.serialise())
    interface.send_update()

    for _ in range(number_of_fades):
        # For each light, make one of them red at a time
        for i in range(len(lights)):
            if i == current_light:
                # Turn on the current light
                lights[i].set_colour(RED)
            else:
                # If i is at a distance > 3 from the current light, turn it off
                # else, interpolate the color between red and black
                if (current_light - i) > 3:
                    lights[i].set_colour(Color(0, 0, 0, 0))
                elif current_light - i > 0:
                    # The less i is from current_light, the more red it is
                    red = 255 // (current_light - i + 2)
                    lights[i].set_colour(Color(red, 0, 0, 0))

        interface.set_frame(universe.serialise())
        interface.send_update()
        time.sleep(.05)

        current_light += 1
        current_light %= len(lights)
        
        
