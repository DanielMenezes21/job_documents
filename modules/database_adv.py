import sqlite3

def criar_banco():
    conn = sqlite3.connect("advogados.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS advogados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            identidade_oab TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM advogados WHERE username = ?", ("Admin",))
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO advogados (username, password, identidade_oab)
            VALUES (?, ?, ?)
        """, [
            ("Admin", "123", "None")
        ])

    conn.commit()
    return conn

criar_banco()