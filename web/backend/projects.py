from __main__ import app
import json
import os
from flask import jsonify, request

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