from flask import Flask, request, jsonify, redirect, render_template
from database import init_db, get_db
from utils import generate_id

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original = data.get('url')
    if not original:
        return jsonify({"error": "URL não fornecida"}), 400

    id = generate_id()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO links (id, original, clicks) VALUES (?, ?, ?)", (id, original, 0))
    conn.commit()
    conn.close()
    return jsonify({"short_url": f"http://localhost:5000/s/{id}"})

@app.route('/s/<id>')
def redirect_url(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT original, clicks FROM links WHERE id=?", (id,))
    row = cursor.fetchone()

    if row:
        new_clicks = row[1] + 1
        cursor.execute("UPDATE links SET clicks=? WHERE id=?", (new_clicks, id))
        conn.commit()
        conn.close()
        return redirect(row[0])
    conn.close()
    return "Link não encontrado", 404

@app.route('/stats/<id>')
def stats(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT clicks FROM links WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify({"clicks": row[0]})
    return jsonify({"error": "Link não encontrado"}), 404

# Isso permite usar o app em testes sem rodar o servidor de verdade
def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
