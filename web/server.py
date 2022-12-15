from flask import Flask
import socketio
import eventlet

flask_app = Flask(__name__)
sio = socketio.Server(cors_allowed_origins='*')

@flask_app.route('/')
def index():
    """
        The root of the website.
        Returns the content of the index.html file.
    """
    return flask_app.send_static_file('index.html')


@sio.event
def connect(sid, environ):
    print("[+] Client connected: ", sid)


@sio.event
def disconnect(sid):
    print("[-] Client disconnected: ", sid)


@sio.event
def message(sid, data):
    print("[*] Client message: ", sid, data)


@sio.on('light_frame')
def light_frame(sid, data):
    print("[*] Light frame: ", sid, data)
    sio.emit('light_frame', data)


if __name__ == '__main__':
    # Start the server
    app = socketio.WSGIApp(sio, flask_app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
