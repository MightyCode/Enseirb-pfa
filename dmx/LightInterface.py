from DMXInterface import DMXInterface
from DMXUniverse import DMXUniverse
from interface.python.Interface import Interface
import json
from LightEffects import LightEffects, NUMBER_OF_LIGHTS, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS
from time import sleep

class LightInterface(Interface):
    def __init__(self):
        super().__init__()
        self.universe = DMXUniverse(NUMBER_OF_LIGHTS)
        self.interface = DMXInterface(self.universe)
        self.effects = LightEffects(self.universe, self.interface)
    
    def read_project(self, path):
        """ Reads a project from a json file and load it into the interface

        Args:
            path (String): path to the json file
        """
        self.load_effect_from(path)
        with open(path, 'r') as file:
            self.referenceEffects = json.load(file)
            self.length = len(self.referenceEffects)
        
    
    def load_effect_from(self, path):
        pass
            
    
    def compute_tick(self, tick):
        """ Computes the light effects for the specified tick

        Args:
            tick (int): number of the tick to compute
        """
        self.interface.set_frame(self.referenceEffects[tick])
        self.interface.send_update()
    
    def pre_compute(self):
        pass
    
    def do_scenarii(self):
        """ Executes the light effects
        """
        # Exécuter le scénario de lumière en utilisant le matériel requis (DMX)
        # ...
        for tick in range(self.length):
            self.compute_tick(tick)
            sleep(0.1)


#testing purposes

if __name__ == "__main__":
    
    lc = LightInterface()
    lc.read_project("test.json")
    lc.pre_compute()
    lc.do_scenarii()