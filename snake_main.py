import time
from dmx import Colour, DMXInterface, DMXUniverse, DMXLight4Slot
from dmx.colour import *
from dmx.light import *
import pygame
import numpy as np


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((300, 300))


if __name__ == "__main__": 
    
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

        for i in range(NUMBER):
            light = DMXLight4Slot(address=light_map[i])
            light.set_colour(Colour(200, 50, 0, 100))
            # Add the light to a universe
            universe.add_light(light)
            lights.append(light)

            # Update the interface's frame to be the universe's current state
        interface.set_frame(universe.serialise())

        # Send an update to the DMX network
        interface.send_update()
        light_test(universe, interface)

    pygame.quit()

    
