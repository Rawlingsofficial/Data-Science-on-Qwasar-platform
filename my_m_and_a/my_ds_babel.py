import sqlite3
import csv
import pandas as pd
from io import StringIO

def sql_to_csv(database, table_name):
    # Connect to the database
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_names = [row[1] for row in cursor.fetchall()]
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    csv_string = ','.join(column_names) + '\n'
    
    for row in rows:
        csv_string += ','.join(map(str, row)) + '\n'

    connection.close()
    csv_string = csv_string.strip()
    return csv_string

def csv_to_sql(csv_content: str, database_name: str, table_name: str) -> None:
    data = pd.read_csv(csv_content)
    
    # Connect to the SQLite database
    with sqlite3.connect(database_name) as conn:
        # Insert the data into the specified table in the database
        data.to_sql(table_name, conn, if_exists='replace', index=False)
