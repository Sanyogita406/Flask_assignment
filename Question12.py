#Ques12: Build a Flask app that updates data in real-time using WebSocket connections.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
   pass

@socketio.on('disconnect')
def handle_disconnect():
    pass

@socketio.on('update_data')
def handle_update_data(data):
    emit('data_updated', updated_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(host = '0.0.0.0', post = 50000)
