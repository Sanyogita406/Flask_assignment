#Ques5: Implement user sessions in a flask app to store and display user-specific data.

from flask import Flask, session
from flask_session import Session
app = Flask(__name__)


app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
Session(app)

@app.route('/login', methods=['POST'])
def login():
    session['user_id'] = user.id
    session['username'] = user.username
    return 'Logged in successfully'


@app.route('/profile')
def profile():
    # Retrieve user-specific data from session
    user_id = session.get('user_id')
    username = session.get('username')
    
    # Display user-specific data
    return f'User ID: {user_id}, Username: {username}'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)


