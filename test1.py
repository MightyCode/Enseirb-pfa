from dmx import Colour, DMXInterface, DMXUniverse, DMXLight4Slot
from dmx.colour import WHITE

PURPLE = Colour(255, 255, 255)

# Open an interface
with DMXInterface("FT232R") as interface:
    # Create a universe
    universe = DMXUniverse()

    # Define a light
    light = DMXLight4Slot(address=1)

    # Add the light to a universe
    universe.add_light(light)

    # Set light to purple
    light.set_colour(WHITE)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()