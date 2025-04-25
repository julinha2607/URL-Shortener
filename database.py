import sqlite3

def init_db():
# Abre (ou cria) o arquivo links.db dentro da pasta instance/.
    conn = sqlite3.connect('instance/links.db')
# cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id TEXT PRIMARY KEY,
            original TEXT NOT NULL,
            clicks INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def get_db():
    return sqlite3.connect('instance/links.db')
