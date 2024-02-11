#Ques13: Implement notifications in a flask app using websockets to notify users of updates.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@socketio.on('notification')
def handle_notification(data):
    emit('new_notification', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
