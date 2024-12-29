from database.database import get_connection
from datetime import datetime

def insert_analysis_result(analysis_name, result):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                           INSERT INFO analysis_result (analysis_name, result, created_at)
                           VALUES (?, ?, ?)
                           """, (analysis_name, result, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            connection.commit()
    except Exception as e:
        raise Exception(f"Error inserting analysi result: {e}")
    
def get_analysis_result():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM analysis_results")
            rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise Exception(f"Error fetching analysis result: {e}")