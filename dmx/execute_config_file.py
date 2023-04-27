import json
from dmx.interface import DMXInterface

# Charger le fichier JSON
with open('./effects_config.json', 'r') as file:
    data = json.load(file)

# Créer une instance de l'interface DMX
interface = DMXInterface('nom_du_driver') # Remplacer 'nom_du_driver' par le nom du driver DMX

# Ouvrir l'interface DMX
interface.open()

# Parcourir les commandes DMX du fichier JSON
for command in data['commands']:
    address = command['address']
    value = command['value']

    # Mettre à jour le frame DMX avec la commande
    frame = [0] * 512  # Créer un frame DMX vide
    frame[address - 1] = value  # Mettre à jour la valeur à l'adresse spécifiée

    # Envoyer la mise à jour sur l'interface DMX
    interface.set_frame(frame)
    interface.send_update()

# Fermer l'interface DMX
interface.close()
