from __main__ import app
import os
from flask import jsonify, request
from werkzeug.utils import secure_filename

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'wav', 'mp3', 'ogg'}

# Route for audio file upload
@app.route('/audios', methods=['POST'])
def upload_file():
    # Check if file is present in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400

    uploaded_file = request.files['file']

    # Check if file has a valid filename and extension
    if uploaded_file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(uploaded_file.filename):
        return jsonify({'error': 'Invalid file type'}), 400
    
    # Check if file already exists
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)):
        return jsonify({'error': 'File already exists', 'filename': secure_filename(uploaded_file.filename) }), 409

    # Save file to upload folder
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify({'success': 'File uploaded successfully', 'filename': filename}), 200

