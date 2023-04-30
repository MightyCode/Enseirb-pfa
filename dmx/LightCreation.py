from dmx.DMXInterface import DMXInterface
from dmx.DMXUniverse import DMXUniverse
from interface.python.Interface import Interface
from dmx.light import DMXLight4Slot, Color
from time import sleep
import json
import numpy as np
from dmx.LightEffects import LightEffects, NUMBER_OF_LIGHTS, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS

class LightCreation(Interface):
    def __init__(self):
        super().__init__()
        self.universe = DMXUniverse(NUMBER_OF_LIGHTS)
        self.interface = DMXInterface(self.universe)
        self.effects = LightEffects(self.universe, self.interface)
    
    def readProject(self, path):
        
        self.loadCustomEffects(path)
        
        # ouvre le fichier json et le charge dans l'interface en mettant chaque effet dans self.referenceEffects: list = []
        with open(path, 'r') as file:
            self.referenceEffects = json.load(file)
            self.length = len(self.referenceEffects)
        
    
    def loadCustomEffects(self, path):
        pass
            
    
    def computeTick(self, tick):
        # Exécuter les effets de lumière pour le tick spécifié
        self.interface.set_frame(self.referenceEffects[tick])
        self.interface.send_update()
    
    def preCompute(self):
        pass
    
    def doScenarii(self):
        # Exécuter le scénario de lumière en utilisant le matériel requis (DMX)
        # ...
        self.preCompute()
        for tick in range(self.length):
            self.computeTick(tick)
            sleep(0.1)
