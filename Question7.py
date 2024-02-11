#Ques7. Integrate a SQLite database with flask to perform CRUD operations on a list of items.

from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect('items.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
''')
conn.commit()
@app.route('/items', methods=['GET'])
def get_items():
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    return render_template('items.html', items=items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    cursor.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    return render_template('item.html', item=item)

@app.route('/items', methods=['POST'])
def add_item():
    name = request.form['name']
    description = request.form['description']
    cursor.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    return redirect('/items')

@app.route('/items/<int:item_id>', methods=['POST'])
def update_item(item_id):
    name = request.form['name']
    description = request.form['description']
    cursor.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, item_id))
    conn.commit()
    return redirect('/items')

@app.route('/items/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    return redirect('/items')
if __name__ == '__main__':
    app.run(host = '0.0.0.0', post = 5000, debug=True)
