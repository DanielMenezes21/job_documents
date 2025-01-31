import sqlite3
import os
import sys

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("advogados.db")
cursor = conn.cursor()

# Criar a tabela de usuários (caso ainda não exista)
cursor.execute("""
CREATE TABLE IF NOT EXISTS advogados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    identidade_OAB TEXT NOT NULL UNIQUE
)
""")

# Inserir um usuário de teste (somente na primeira vez)
cursor.execute("INSERT OR IGNORE INTO advogados (username, password, identidade_OAB) VALUES (?, ?, ?)", ("admin", "123", "None"))
conn.commit()

conn.close()

def get_db_path():
    if getattr(sys, 'frozen', False):  # Executável gerado pelo PyInstaller
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "advogados.db")
