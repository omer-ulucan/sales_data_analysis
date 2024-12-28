import sqlite3

def get_connection():
    """
    Database connection
    """
    try:
        connection = sqlite3.connect("database/test.db")
        connection.execute("PRAGMA foreign_keys = ON")
        return connection
    except sqlite3.Error as e:
        raise Exception(f"Database connection error: {e}")
