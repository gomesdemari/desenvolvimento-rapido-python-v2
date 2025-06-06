import sqlite3
from utils.gerar_senha import gerar_hash

def verificar_login(usuario, senha):
    db_connection = sqlite3.connect("banco.db")
    cursor = db_connection.cursor()
    senha_hash = gerar_hash(senha)

    cursor.execute("SELECT nome FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha_hash))
    result = cursor.fetchone()
    db_connection.close()

    if result:
        return result[0]  
    return None