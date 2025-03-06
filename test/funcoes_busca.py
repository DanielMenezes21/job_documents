import sqlite3

def buscar_pessoas_por_nome(conn, filtro):
    """Busca clientes pelo nome ou CPF que começam com o texto digitado."""
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, cpf, rg, endereco, estado_civil, sigla_estado_cliente, cidade_cliente, cep_cliente, telefone_cliente, email_cliente, nacionalidade_cliente, profissao_cliente, secretaria_emissora_rg, estado_emissor_rg
        FROM pessoas
        WHERE nome LIKE ? OR cpf LIKE ?
        LIMIT 10
    """, (filtro + "%", filtro + "%"))
    
    resultados = cursor.fetchall()
    return resultados

