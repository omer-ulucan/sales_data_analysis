import pandas as pd
from database.database import get_connection
from data_analysis.analysis import clean_data

def insert_csv_to_sales(file_path):
    try:
        df = pd.read_csv(file_path, encoding="latin1")
        cleaned_df = clean_data(df)
        
        with get_connection() as connection:
            cleaned_df.to_sql("sales", connection, if_exists="append", index=False)
        print("CSV data inserted successfully")
    except Exception as e:
        raise Exception(f"Error inserting CSV data: {e}")
    
if __name__ == "__main__":
    file_path = "C:\Users\omer_\OneDrive\Desktop\sales_analysis\sales_data_set\sales_data_sample.csv"
    insert_csv_to_sales(file_path)