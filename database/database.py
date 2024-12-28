import _sqlite3

def get_connection():
    """
    Database connection
    """
    connection = _sqlite3.connect("/database/test.db")
    return connection
