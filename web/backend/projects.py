from __main__ import app
import json
import os
from flask import jsonify, request

def is_project_valid(config: dict):
    """
        Checks that the given JSON conforms to the project schema.
        @param config: The JSON to check.
        @return: True if the JSON is valid, False otherwise.
    """
    required_fields = ['id', 'audio']
    for field in required_fields:
        if field not in config or config[field] == '':
            return False, 'Missing field: ' + field
        
    # Check that audio file exists
    if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], config['audio'])):
        return False, 'Audio file does not exist'
    
    return True, ''

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

    # Check schema validity
    project_valid, error = is_project_valid(project)

    if not project_valid:
        return jsonify({'error': error}), 400

    # Write project to file, overwriting if it already exists
    with open(os.path.join('projects', project['id']+'.json'), 'w') as f:
        json.dump(project, f)

    return jsonify(project), 201

# This route handles GET requests to retrieve project data with a given ID.
# The ID is passed as a parameter in the URL.
@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    # Open the JSON file for the given ID and load its contents.
    with open(os.path.join('projects', id+'.json'), 'r') as f:
        project = json.load(f)
        
    # Return the project data as a JSON response.
    return jsonify(project)

# This route handles PUT requests to update project data with a given ID.
# The ID is passed as a parameter in the URL.
@app.route('/projects/<id>', methods=['PUT'])
def update_project(id):
    # Get the updated project data from the request body.
    project = request.json

    # Open the JSON file for the given ID and write the updated data.
    with open(os.path.join('projects', id+'.json'), 'w') as f:
        json.dump(project, f)

    # Return the updated project data as a JSON response.
    return jsonify(project)

# This route handles DELETE requests to delete project data with a given ID.
# The ID is passed as a parameter in the URL.
@app.route('/projects/<id>', methods=['DELETE'])
def delete_project(id):
    # Remove the JSON file for the given ID.
    os.remove(os.path.join('projects', id+'.json'))

    # Return an empty response with status code 204 (No Content).
    return '', 204