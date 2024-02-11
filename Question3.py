#Ques3. Develop a flask app that uses URL parameters to display dynamic content. 

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/user/<username>')
def show_user(username):
    return f'Hello, {username}!'

 if __name__ == '__main__':
    app.run(host = '0.0.0.0'. port = 5000)

