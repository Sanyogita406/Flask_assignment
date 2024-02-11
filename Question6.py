#Ques6: Build a flask app allows user to upload files and display them on the website.

from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('path/to/save/file')
    return 'File uploaded successfully!'

import os
@app.route('/files')
def display_files():
    files = os.listdir('path/to/save/file')
    return render_template('files.html', files=files)


if __name__ == '__main__':
    app.run(host = '0.0.0.0'. post = 5000)