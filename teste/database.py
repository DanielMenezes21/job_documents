import sqlite3

def criar_banco():
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            rg TEXT UNIQUE NOT NULL
        )
    """)

    # Inserindo alguns dados fictícios
    cursor.executemany("""
        INSERT INTO pessoas (nome, cpf, rg) VALUES (?, ?, ?)
    """, [
        ("João Silva", "123.456.789-00", "MG-12.345.678"),
        ("Maria Souza", "987.654.321-00", "SP-98.765.432"),
        ("Carlos Lima", "111.222.333-44", "RJ-11.223.344")
    ])

    conn.commit()
    conn.close()

# Criar banco ao executar o script
criar_banco()
