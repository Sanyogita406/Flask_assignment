#Ques9: Create a restful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    return jsonify({'message': 'Book added successfully'})

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', post = 5000)
