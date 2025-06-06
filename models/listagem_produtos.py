import sqlite3

def listagem_produtos():
    db_connection = sqlite3.connect("banco.db")
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        db_connection.commit()
        db_connection.close()
        return produtos
    except Exception as e:
        return []