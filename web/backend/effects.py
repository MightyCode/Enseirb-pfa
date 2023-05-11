from __main__ import app
import json
import os
from flask import jsonify, request

# Read directory 'effects' and find the highest id
def get_highest_id():
    highest_id = 0
    for file in os.listdir('effects'):
        with open(os.path.join('effects', file), 'r') as f:
            effect = json.load(f)
            if int(effect['id']) > highest_id:
                highest_id = int(effect['id'])
    return highest_id

HIGHEST_ID = get_highest_id()

# Effect CRUD endpoints
@app.route('/effects', methods=['GET'])
def get_effects():
    effects = []
    for file in os.listdir('effects'):
        with open(os.path.join('effects', file), 'r') as f:
            effect = json.load(f)
            effects.append(effect)
    return jsonify(effects)

@app.route('/effects', methods=['POST'])
def create_effect():
    global HIGHEST_ID

    effect = request.json
    with open(os.path.join('effects', str(HIGHEST_ID + 1) + '.json'), 'w') as f:
        effect['id'] = str(HIGHEST_ID + 1)
        json.dump(effect, f)
        HIGHEST_ID += 1
        
    return jsonify(effect), 201

@app.route('/effects/<id>', methods=['GET'])
def get_effect(id):
    with open(os.path.join('effects', id+'.json'), 'r') as f:
        effect = json.load(f)
    return jsonify(effect)

@app.route('/effects/<id>', methods=['PUT'])
def update_effect(id):
    effect = request.json
    with open(os.path.join('effects', id+'.json'), 'w') as f:
        json.dump(effect, f)
    return jsonify(effect)

@app.route('/effects/<id>', methods=['DELETE'])
def delete_effect(id):
    os.remove(os.path.join('effects', id+'.json'))
    return '', 204