import sqlite3

def listagem_usuarios():
    db_connection = sqlite3.connect("banco.db")
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        db_connection.commit()
        db_connection.close()
        return usuarios
    except Exception as e:
        return []