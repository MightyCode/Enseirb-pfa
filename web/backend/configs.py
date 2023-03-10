from __main__ import app
import json
import os
from flask import jsonify, request

def is_config_valid(config: dict):
    """
        Checks that the given JSON conforms to the config schema.
        @param config: The JSON to check.
        @return: True if the JSON is valid, False otherwise.
    """
    required_fields = ['id', 'nbLights', 'nbSpeakers']
    for field in required_fields:
        if field not in config:
            return False
        
    return True

# Config CRUD endpoints
@app.route('/configs', methods=['GET'])
def get_configs():
    configs = []

    for file in os.listdir('configs'):
        with open(os.path.join('configs', file), 'r') as f:
            config = json.load(f)
            configs.append(config)
            
    return jsonify(configs)

@app.route('/configs', methods=['POST'])
def create_config():
    config = request.json

    # Check that config is valid
    if not is_config_valid(config):
        return jsonify({'error': 'Invalid config'}), 400
    
    # Check that config doesn't already exist
    if os.path.exists(os.path.join('configs', config['id']+'.json')):
        return jsonify({'error': 'Config already exists'}), 409

    # Saves the config
    with open(os.path.join('configs', config['id']+ '.json'), 'w') as f:
        json.dump(config, f)

    return jsonify(config), 201

@app.route('/configs/<id>', methods=['GET'])
def get_config(id):
    with open(os.path.join('configs', id+'.json'), 'r') as f:
        config = json.load(f)
    return jsonify(config)

@app.route('/configs/<id>', methods=['PUT'])
def update_config(id):
    config = request.json
    with open(os.path.join('configs', id+'.json'), 'w') as f:
        json.dump(config, f)
    return jsonify(config)

@app.route('/configs/<id>', methods=['DELETE'])
def delete_config(id):
    os.remove(os.path.join('configs', id+'.json'))
    return '', 204