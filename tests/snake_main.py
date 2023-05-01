from dmx import Color, DMXInterface, DMXUniverse, DMXLight4Slot
from dmx.color import *
from dmx.light import *

import time
import pygame
import numpy as np


def light_test(universe, interface):
    
    if universe.has_light_at_address(light_coord_to_id(1, 4)):
        universe.get_light_at_address(light_coord_to_id(1, 4)).set_colour(WHITE)
    else:
        universe.add_light(DMXLight4Slot(address=light_coord_to_id(2, 4)).set_colour(WHITE))

    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

if __name__ == "__main__": 
    with DMXInterface("SIMULATOR") as interface:
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((300, 300))

        ROW: int = 6
        COL: int = 9

        NUMBER = ROW * COL

        lights = [0] * NUMBER

        EMPTY, FRUIT, SNAKE = range(3)

        #cells = init(ROW, COL)

        UP, RIGHT, DOWN, LEFT = range(4)

        direction: int = UP
    
        # Create a game loop
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = LEFT
                    if event.key == pygame.K_RIGHT:
                        direction = RIGHT
                    if event.key == pygame.K_DOWN:
                        direction = DOWN
                    if event.key == pygame.K_UP:
                        direction = UP
                    # Get the state of all keyboard keys

            print(direction)
            clock.tick(300)

            universe = DMXUniverse()

            for i in range(NUMBER):
                light = DMXLight4Slot(address=light_map[i])
                if direction == UP:
                    light.set_colour(Color(200, 50, 0, 100))
                elif direction == DOWN:
                    light.set_colour(Color(0, 50, 0, 100))
                elif direction == LEFT:
                    light.set_colour(Color(0, 200, 50, 100))
                elif direction == RIGHT:
                    light.set_colour(Color(50, 0, 200, 100))

                # Add the light to a universe
                universe.add_light(light)
                lights.append(light)

                # Update the interface's frame to be the universe's current state
            interface.set_frame(universe.serialise())

            # Send an update to the DMX network
            interface.send_update()

        pygame.quit()

    
