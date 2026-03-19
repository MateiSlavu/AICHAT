from database.db import get_db_connection

def init_db():
    con = get_db_connection()
    with con:
        con.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER
            )
        ''')

if __name__ == "__main__":
    init_db()