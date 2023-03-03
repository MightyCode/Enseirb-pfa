from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

# Set CORS headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Check if folders exist, create them if not
folders = ["effects", "configs", "projects"]
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

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
    # TODO: Check if config already exists
    # TODO: Check if config is valid
    config = request.json
    with open(os.path.join('configs', config['id']+'.json'), 'w') as f:
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

# Project CRUD endpoints
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = []
    for file in os.listdir('projects'):
        with open(os.path.join('projects', file), 'r') as f:
            project = json.load(f)
            projects.append(project)
    return jsonify(projects)

@app.route('/projects', methods=['POST'])
def create_project():
    project = request.json
    with open(os.path.join('projects', project['id']+'.json'), 'w') as f:
        json.dump(project, f)
    return jsonify(project), 201

@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    with open(os.path.join('projects', id+'.json'), 'r') as f:
        project = json.load(f)
    return jsonify(project)

@app.route('/projects/<id>', methods=['PUT'])
def update_project(id):
    project = request.json
    with open(os.path.join('projects', id+'.json'), 'w') as f:
        json.dump(project, f)
    return jsonify(project)

@app.route('/projects/<id>', methods=['DELETE'])
def delete_project(id):
    os.remove(os.path.join('projects', id+'.json'))
    return '', 204

# Run on 0.0.0.0
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)