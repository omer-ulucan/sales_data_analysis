from database.database import get_connection

def create_tables():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
        
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS sales(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT,
                            product TEXT,
                            price REAL,
                            quantity INTEGER
                        );
                        """)
            
            connection.commit()
    except Exception as e:
        raise Exception(f"Error while creating tables: {e}")
    
if __name__ == "__main__":
    create_tables()