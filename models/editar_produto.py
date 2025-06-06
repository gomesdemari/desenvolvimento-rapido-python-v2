import sqlite3

def editar_produto(produto_id, nome, tipo, fornecedor, preco, quantidade):
    db_connection = sqlite3.connect("banco.db")
    cursor = db_connection.cursor()
    try:
        cursor.execute("""
            UPDATE produtos
            SET nome = ?, tipo = ?, fornecedor = ?, preco = ?, quantidade = ?
            WHERE id = ?
        """, (nome, tipo, fornecedor, preco, quantidade, produto_id))
        if cursor.rowcount == 0:
            db_connection.close()
            return False  
        cursor.execute("SELECT COUNT(*) FROM produtos WHERE nome = ? AND id != ?", (nome, produto_id))
        if cursor.fetchone()[0] > 0:
            db_connection.close()
            return False  
        db_connection.commit()
        db_connection.close()
        return True
    except Exception as e:
        print(f"Erro ao editar produto: {e}")
        db_connection.close()
        return False