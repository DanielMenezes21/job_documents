import sqlite3

def criar_banco():
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            rg TEXT UNIQUE NOT NULL,
            endereco TEXT NOT NULL,
            estado_civil TEXT NOT NULL 
        )
    """)

    # Inserindo alguns dados fictícios
    cursor.executemany("""
        INSERT INTO pessoas (nome, cpf, rg, endereco, estado_civil) VALUES (?, ?, ?, ?, ?)
    """, [
        ("João Silva", "123.456.789-00", "12345678", "end_example", "casado"),
        ("Maria Souza", "98765432100", "98765432", "endereco", "solteira"),
        ("Carlos Lima", "11122233344", "11223344", "exemplo", "viuvo")
    ])

    conn.commit()
    conn.close()

# Criar banco ao executar o script
criar_banco()
