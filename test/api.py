from flask import Flask, request, jsonify
import sqlite3
from database import criar_banco

app = Flask(__name__)
def get_db_connection():
    conn = criar_banco()
    return conn

@app.route('/buscar', methods=['GET'])
def buscar():
    filtro = request.args.get('filtro', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome, cpf, rg, endereco, estado_civil, sigla_estado_cliente, cidade_cliente, cep_cliente, telefone_cliente, email_cliente, nacionalidade_cliente, profissao_cliente, secretaria_emissora_rg, estado_emissor_rg
        FROM pessoas
        WHERE nome LIKE ? OR cpf LIKE ?
        LIMIT 10
    """, (filtro + "%", filtro + "%"))
    resultados = cursor.fetchall()
    conn.close()
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
