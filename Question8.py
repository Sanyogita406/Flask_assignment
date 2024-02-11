#Ques8. Implement user authentication and registration in a Flask app using Flask-Login.


pip install flask-login
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)

from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
         pass
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
