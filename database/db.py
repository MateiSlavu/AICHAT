import sqlite3
from config import DATABASE_PATH

def get_db_connection():
    con = sqlite3.connect(DATABASE_PATH)
    con.text_factory = str
    return con