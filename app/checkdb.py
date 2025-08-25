import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

dburl = os.getenv("DATABASE_URL")
try:
    conn = psycopg2.connect(dburl)
    print("Connection successful!")
    curr = conn.cursor()
    curr.execute("SELECT * from tenants;")
    rows = curr.fetchall()
    for row in rows:
        print(f"id={row[0]}, name={row[1]}")
    #     print(row)
    curr.close()
    
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")