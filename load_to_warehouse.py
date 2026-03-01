import duckdb
import os
import pandas as pd

def load_to_duckdb():
    # 1. Define where our cleaned data is
    csv_path = "data/silver/weather_cleaned.csv"
    db_path = "data/gold/weather_warehouse.db"
    
    # 2. Ensure the Gold folder exists
    os.makedirs("data/gold", exist_ok=True)
    
    # 3. Connect to DuckDB (it creates the file if it doesn't exist)
    con = duckdb.connect(db_path)
    
    # 4. Create a table and insert the CSV data
    # DuckDB is "smart"—it can read a CSV directly into a table!
    con.execute(f"""
        CREATE TABLE IF NOT EXISTS weather_history AS 
        SELECT * FROM read_csv_auto('{csv_path}')
    """)
    
    # 5. Append new data if the table already exists
    con.execute(f"INSERT INTO weather_history SELECT * FROM read_csv_auto('{csv_path}')")
    
    # 6. Check if it worked by printing the count of rows
    row_count = con.execute("SELECT count(*) FROM weather_history").fetchone()[0]
    
    print(f"🏆 Data loaded into DuckDB Warehouse!")
    print(f"📊 Total records in your Gold layer: {row_count}")
    
    con.close()

if __name__ == "__main__":
    load_to_duckdb()