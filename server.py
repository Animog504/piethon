from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import app

server = Flask(__name__)
socketio = SocketIO(server)

if __name__ == '__main__':
   socketio.run(server)

@socketio.on('connect')
def handle_connection():
   emit('data', {
    "analysis": {
        "total":app.total,
        "most_cost_effective":app.most_cost_effective
    },
    "charts": {
        "pies_by_cost": app.pies_by_cost,
        "pies_by_weight": app.pies_by_weight,
        "pies_by_cost_per_pound": app.pies_by_cost_per_pound
    }
})