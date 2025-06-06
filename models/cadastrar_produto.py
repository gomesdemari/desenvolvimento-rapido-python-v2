import sqlite3

def cadastrar_produto(nome, tipo, fornecedor, preco, quantidade):
    db_connection = sqlite3.connect("banco.db")
    cursor = db_connection.cursor()
    try:
        cursor.execute("INSERT INTO produtos (nome, tipo, fornecedor, preco, quantidade) VALUES (?, ?, ?, ?, ?)", (nome, tipo, fornecedor, preco, quantidade))
        db_connection.commit()
        db_connection.close()
        return True
    except sqlite3.IntegrityError:
        db_connection.close()
        return False