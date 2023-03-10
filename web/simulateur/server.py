from flask import Flask, send_from_directory
import socketio
import eventlet
from pathlib import Path

flask_app = Flask(__name__)
sio = socketio.Server(cors_allowed_origins='*')


@flask_app.route('/')
def index():
    """
        The root of the website.
        Returns the content of the index.html file.
    """
    return flask_app.send_static_file('index.html')


@flask_app.route('/configs/<path:path>')
def send_config(path):
    """
        Serve config files from ../config.
        THe config file is a JSON file.
        Sends the MIME type of an javascript module.
    """
    file_path = Path(__file__).parent / '..' / 'configs' / path
    return send_from_directory(file_path.parent, file_path.name)



@sio.event
def connect(sid, environ):
    pass


@sio.event
def disconnect(sid):
    pass


@sio.event
def message(sid, data):
    pass


@sio.on('light_frame')
def light_frame(sid, data):
    sio.emit('light_frame', data)


if __name__ == '__main__':
    # Start the server
    app = socketio.WSGIApp(sio, flask_app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
