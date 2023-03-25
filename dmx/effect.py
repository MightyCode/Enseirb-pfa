from dmx.interact import *

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


def strobe_effect(universe, interface):
    i = 0
    while True:
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
    
    if universe.has_light_at_address(light_coord(1, 4)):
        universe.get_light_at_address(light_coord(1, 4)).set_colour(WHITE)
    else:
        universe.add_light(DMXLight4Slot(address=light_coord(2, 4)).set_colour(WHITE))

    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()


def rainbow_wave_effect(universe, interface):
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
    while True:
        for s in new_states:
            interface.set_frame(s)
            interface.send_update()


def fireball_circle_effect(universe, interface):
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
        
        
def virus_spreading_wave_effect(universe, random, interface):
    # Create a list of lights
    lights = [DMXLight4Slot(address=light_map[i]) for i in range(NUMBER_OF_LIGHTS)]

    # Add the lights to the universe
    for l in lights:
        universe.add_light(l)

    # Turn off all lights
    for l in lights:
        l.set_colour(Color(0, 0, 0, 0))
    interface.set_frame(universe.serialise())
    interface.send_update()

    # Pick a random light to start with
    current_light = random.randint(0, NUMBER_OF_LIGHTS - 1)

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
    


def light_number_to_coords(light_number):
    return light_number // NUMBER_OF_COLUMNS, light_number % NUMBER_OF_COLUMNS