import json

def generate_effects_config():
    effects = []
    
    while True:
        effect_name = input("Entrez le nom de l'effet (ou 'q' pour quitter) : ")
        
        if effect_name == 'q':
            break
        
        effect_params = {}
        
        # Demander les paramètres spécifiques à l'effet
        if effect_name == 'pulse_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["color"] = {
                "r": int(input("Couleur R : ")),
                "g": int(input("Couleur G : ")),
                "b": int(input("Couleur B : "))
            }
            effect_params["interpolation_rate"] = int(input("Taux d'interpolation : "))
        
        elif effect_name == 'pulse_in_rythm':
            effect_params["beat"] = float(input("Durée d'un battement : "))
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["color"] = {
                "r": int(input("Couleur R : ")),
                "g": int(input("Couleur G : ")),
                "b": int(input("Couleur B : "))
            }
        
        elif effect_name == 'pulse_rainbow_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["interpolation_rate"] = int(input("Taux d'interpolation : "))
            effect_params["number_of_pulses"] = int(input("Nombre de pulses : "))
        
        elif effect_name == 'fading_rainbow_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["fade_speed"] = float(input("Vitesse de fondu : "))
            effect_params["number_of_fades"] = int(input("Nombre de fondues : "))
        
        elif effect_name == 'color_flicker_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["flicker_speed"] = float(input("Vitesse de scintillement : "))
            effect_params["flicker_intensity"] = float(input("Intensité de scintillement : "))
            effect_params["number_of_flickers"] = int(input("Nombre de scintillements : "))
        
        elif effect_name == 'strobe_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["number_of_strobes"] = int(input("Nombre de flashs : "))
        
        elif effect_name == 'dim_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
        
        elif effect_name == 'soft_white_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
        
        elif effect_name == 'light_test':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
        
        elif effect_name == 'random_color_change_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["change_interval"] = float(input("Intervalle de changement de couleur : "))
            effect_params["number_of_changes"] = int(input("Nombre de changements de couleur : "))
        
        elif effect_name == 'rainbow_wave_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["number_of_waves"] = int(input("Nombre de vagues : "))
        
        elif effect_name == 'fireball_circle_effect':
            effect_params["universe"] = int(input("Universe : "))
            effect_params["interface"] = input("Interface : ")
            effect_params["number_of_fades"] = int(input("Nombre de fondues : "))
        
        else:
            print("Effet non reconnu.")
            continue
        
        effect = {
            "name": effect_name,
            "params": effect_params
        }
        
        effects.append(effect)
    
    # Générer le fichier JSON
    config = {
        "effects": effects
    }
    
    with open("effects_config.json", "w") as file:
        json.dump(config, file)
    
    print("Fichier 'effects_config.json' généré avec succès !")

