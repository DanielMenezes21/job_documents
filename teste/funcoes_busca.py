import sqlite3

def buscar_pessoas_por_nome(filtro):
    """Busca clientes pelo nome ou CPF que começam com o texto digitado."""
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, cpf, rg FROM pessoas
        WHERE nome LIKE ? OR cpf LIKE ?
        LIMIT 10
    """, (filtro + "%", filtro + "%"))
    
    resultados = cursor.fetchall()
    conn.close()
    return resultados

