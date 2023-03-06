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

import configs, effects, projects, audio

# Run on 0.0.0.0
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)