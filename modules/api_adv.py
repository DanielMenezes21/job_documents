from flask import Flask, request, jsonify
import sqlite3
from modules.database_adv import criar_banco

app = Flask(__name__)
def get_db_connection():
    conn = criar_banco()
    return conn

@app.route('/buscar_adv', methods=['GET'])
def buscar():
    filtro = request.args.get('filtro', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT username, password, identidade_oab
        FROM advogados
        WHERE username LIKE ? 
        LIMIT 10
    """, (filtro + "%",))
    resultados = cursor.fetchall()
    conn.close()
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
