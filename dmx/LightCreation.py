from dmx.DMXInterface import DMXInterface
from dmx.DMXUniverse import DMXUniverse
from interface.python.Interface import Interface
from dmx.light import DMXLight4Slot, Color
import json
import numpy as np
from dmx.LightEffects import LightEffects, NUMBER_OF_LIGHTS, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS

class LightCreation(Interface):
    def __init__(self):
        super().__init__()
        self.universe = DMXUniverse(NUMBER_OF_LIGHTS)
        self.interface = DMXInterface(self.universe)
        self.effects = LightEffects(self.universe, self.interface)
    
    def read_project(self, path):
        
        self.load_effect_from(path)
        
        # ouvre le fichier json et le charge dans l'interface en mettant chaque effet dans self.referenceEffects: list = []
        with open(path, 'r') as file:
            self.referenceEffects = json.load(file)
            self.length = len(self.referenceEffects)
        
    
    def load_effect_from(self, path):
        pass
            
    
    def compute_tick(self, tick):
        # Exécuter les effets de lumière pour le tick spécifié
        self.interface.set_frame(self.referenceEffects[tick])
        self.interface.send_update()
    
    def pre_compute(self):
        pass
    
    def do_scenarii(self):
        # Exécuter le scénario de lumière en utilisant le matériel requis (DMX)
        # ...
        for tick in range(self.length):
            self.compute_tick(tick)
            sleep(0.1)
