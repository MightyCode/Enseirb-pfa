from time import sleep
import random
from dmx.color import *
from dmx.light import *
from dmx.DMXUniverse import *
from dmx.DMXInterface import *
import time
import numpy as np
import json

NUMBER_OF_LIGHTS = 54
NUMBER_OF_ROWS = 9
NUMBER_OF_COLUMNS = 6

class LightEffects:
    def __init__(self, universe: DMXUniverse, interface: DMXInterface):
        self.universe = universe
        self.interface = interface
        self.light_effects = []

    def save_light_effects(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.light_effects, file)
        

    def set_lights_color(self, lights, color):
        for l in lights:
            l.set_colour(color)

    def set_universe_color(self, color):
        lights = self.universe.get_lights()
        self.set_lights_color(lights, color)

    def interpolate(self, frames, times):
        new_frames = []
        for i in range(len(frames) - 1):
            for j in np.linspace(frames[i], frames[i + 1], times, dtype=int).tolist():
                new_frames.append(j)
        return new_frames

    def lights_transition(self, target_color, interpolation_rate):
        lights = self.universe.get_lights()
        current_color = (lights[0].get_colour()).serialise()
        frames = self.interpolate([current_color, target_color], interpolation_rate)
        for frame in frames:
            self.set_universe_color(Color(*frame))
            self.light_effects.append(self.universe.serialise())

    def pulse_effect(self, color, interpolation_rate):
        self.lights_transition(color.serialise(), interpolation_rate)
        self.lights_transition(BLACK.serialise(), interpolation_rate)

    def pulse_in_rhythm(self, beat, color):
        self.lights_transition(color.serialise(), 1)
        sleep(beat)
        self.lights_transition(BLACK.serialise(), 1)

    def pulse_rainbow_effect(self, interpolation_rate, number_of_pulses):
        rainbow_colors = [
            Color(255, 0, 0), Color(255, 127, 0), Color(255, 255, 0),
            Color(0, 255, 0), Color(0, 0, 255), Color(75, 0, 130),
            Color(143, 0, 255), Color(255, 0, 255), Color(255, 0, 127)
        ]

        for _ in range(number_of_pulses):
            for color in rainbow_colors:
                self.lights_transition(color.serialise(), interpolation_rate)
                self.lights_transition(BLACK.serialise(), interpolation_rate)

    def fading_rainbow_effect(self, fade_speed, number_of_fades):
        rainbow_colors = [
            Color(255, 0, 0), Color(255, 127, 0), Color(255, 255, 0),
            Color(0, 255, 0), Color(0, 0, 255), Color(75, 0, 130),
            Color(143, 0, 255), Color(255, 0, 255), Color(255, 0, 127)]
            
        fade_interval = int(fade_speed * 10)
        
        for _ in range(number_of_fades):
            for color in rainbow_colors:
                self.lights_transition(color.serialise(), fade_interval)
                self.lights_transition(BLACK.serialise(), fade_interval)

    def random_color_effect(self, duration):
        start_time = time.time()
        end_time = start_time + duration

        while time.time() < end_time:
            random_color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.set_universe_color(random_color)
            self.light_effects.append(self.universe.serialise())
            time.sleep(0.1)

    def lightning_effect(self, flash_duration, pause_duration, max_lightning_duration):
        start_time = time.time()
        while (time.time() - start_time) < max_lightning_duration:
            self.set_universe_color(WHITE)
            self.light_effects.append(self.universe.serialise())
            sleep(flash_duration)

            self.set_universe_color(BLACK)
            self.light_effects.append(self.universe.serialise())
            sleep(pause_duration)

    def color_flicker_effect(self, flicker_speed, flicker_intensity, number_of_flickers):
        fade_interval = int(flicker_speed * 10)

        for _ in range(number_of_flickers):
            random_color = Color(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )

            flicker_color = random_color * flicker_intensity

            self.lights_transition(flicker_color.serialise(), fade_interval)

    def dim_effect(self):
        self.lights_transition(Color(200, 50, 0, 100).serialise(), 10)

    def soft_white_effect(self):
        self.lights_transition(Color(150, 150, 100, 255).serialise(), 10)

    def random_color_change_effect(self, change_interval, number_of_changes):
        for _ in range(number_of_changes):
            for light in self.universe.lights:
                random_color = Color(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
                light.set_colour(random_color)

            self.light_effects.append(self.universe.serialise())
            time.sleep(change_interval)

    def rainbow_wave_effect(self, number_of_waves):
        lights = []
        rainbow_9_colors = [
            Color(255, 0, 0), Color(255, 127, 0), Color(255, 255, 0), Color(0, 255, 0),
            Color(0, 0, 255), Color(75, 0, 130), Color(143, 0, 255), Color(255, 0, 255),
            Color(255, 0, 127)
        ]
        states = []
        for i in range(NUMBER_OF_LIGHTS):
            light = DMXLight4Slot(address=light_map[i])
            self.universe.add_light(light)
            lights.append(light)

        for cycle in range(NUMBER_OF_ROWS):
            for i in range(NUMBER_OF_ROWS):
                for j in range(NUMBER_OF_COLUMNS):
                    lights[i * NUMBER_OF_COLUMNS + j].set_colour(rainbow_9_colors[(i - cycle) % NUMBER_OF_ROWS])

            states.append(self.universe.serialise())

        states.append(states[0])
        new_states = self.interpolate(states, 20)

        for _ in range(number_of_waves):
            for state in new_states:
                self.light_effects.append(state)
                

    def fireball_circle_effect(self, number_of_fades):
        path = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
            (2, 9), (3, 9), (4, 9), (5, 9),
            (5, 8), (5, 7), (5, 6), (5, 5),
            (4, 5), (3, 5), (2, 5), (1, 5),
            (1, 4), (1, 3), (1, 2), (1, 1),
            (1, 0), (2, 0), (3, 0), (4, 0),
            (5, 0), (5, 1), (5, 2), (5, 3),
            (5, 4), (4, 4), (3, 4), (2, 4)
        ]

        for _ in range(number_of_fades):
            for i, coords in enumerate(path):
                light = DMXLight4Slot(address=light_coord_to_id(coords[0], coords[1]))
                light.set_colour(RED)
                self.universe.add_light(light)
                self.light_effects.append(self.universe.serialise())
                time.sleep(0.05)
                self.universe.remove_light(light)

    def police_lights_effect(self, number_of_cycles):
        for _ in range(number_of_cycles):
            self.set_universe_color(RED)
            self.light_effects.append(self.universe.serialise())
            time.sleep(0.5)
            self.set_universe_color(BLUE)
            self.light_effects.append(self.universe.serialise())
            time.sleep(0.5)

    def main(self):
        self.set_universe_color(BLACK)
        self.interface.set_frame(self.universe.serialise())
        self.interface.send_update()

    def execute_light_effect(self, duration=None):
        if duration is not None:
            start_time = time.time()
            end_time = start_time + duration
            while time.time() < end_time:
                for snapshot in self.light_effects:
                    self.interface.set_frame(snapshot)
                    self.interface.send_update()
        else:
            for snapshot in self.light_effects:
                self.interface.set_frame(snapshot)
                self.interface.send_update()



       
