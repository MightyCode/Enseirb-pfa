from __main__ import app
import json
import os
from flask import jsonify, request

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
    effect = request.json
    with open(os.path.join('effects', effect['id']+'.json'), 'w') as f:
        json.dump(effect, f)
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