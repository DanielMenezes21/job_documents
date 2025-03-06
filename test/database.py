import sqlite3

def criar_banco():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            rg TEXT UNIQUE NOT NULL,
            endereco TEXT NOT NULL,
            estado_civil TEXT NOT NULL,
            sigla_estado_cliente TEXT NOT NULL,
            cidade_cliente TEXT NOT NULL,
            cep_cliente TEXT NOT NULL,
            telefone_cliente TEXT NOT NULL,
            email_cliente TEXT NOT NULL,
            nacionalidade_cliente TEXT NOT NULL,
            profissao_cliente TEXT NOT NULL,
            secretaria_emissora_rg TEXT NOT NULL,
            estado_emissor_rg TEXT NOT NULL
        )
    """)

    # Inserindo alguns dados fictícios
    cursor.executemany("""
        INSERT INTO pessoas (nome, cpf, rg, endereco, estado_civil, sigla_estado_cliente, cidade_cliente, cep_cliente, telefone_cliente, email_cliente, nacionalidade_cliente, profissao_cliente, secretaria_emissora_rg, estado_emissor_rg)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        ("Fulano da Silva", "123.456.789-00", "12345678", "end_example", "casado", "SP", "São Paulo", "12345-678", "email@example.com", "Brasileiro", "Desenvolvedor", "12345678", "SSP", "SP"),
        ("Ciclano da Silva", "987.654.321-00", "87654321", "end_example", "solteiro", "SP", "São Paulo", "12345-678", "example@gmail.com", "Brasileiro", "Desenvolvedor", "87654321", "SSP", "SP"),
    ])

    conn.commit()
    return conn

# Criar banco ao executar o script
criar_banco()
