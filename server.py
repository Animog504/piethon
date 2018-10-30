from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import app

server = Flask(__name__)
socketio = SocketIO(server)

if __name__ == '__main__':
   socketio.run(server)

@socketio.on('connect')
def handle_connection():
   emit('data', app.output)