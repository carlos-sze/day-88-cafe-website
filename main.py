from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cafe')
    cafes = cursor.fetchall()
    conn.close()
    return render_template('index.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("loc"),
        has_sockets = bool(request.form.get("sockets")),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        can_take_calls = bool(request.form.get("calls")),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price"),

        conn = sqlite3.connect('cafes.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price) VALUES (?,?,?,?,?,?,?,?,?,?)',
                       (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_cafe(id):
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cafes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
