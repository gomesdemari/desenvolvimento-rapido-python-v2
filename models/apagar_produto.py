import sqlite3

def apagar_produto(id_produto):
    db_connection = sqlite3.connect("banco.db")
    cursor = db_connection.cursor()
    try:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        if cursor.rowcount == 0:
            db_connection.close()
            return False 
        db_connection.commit()
        db_connection.close()
        return True
    except sqlite3.IntegrityError:
        db_connection.close()
        return False