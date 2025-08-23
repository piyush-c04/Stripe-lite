import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

dburl = os.getenv("DATABASE_URL")
try:
    conn = psycopg2.connect(dburl)
    print("Connection successful!")
    # curr = conn.cursor()
    # curr.execute("SELECT * from test;")
    # rows = curr.fetchall()
    # for row in rows:
    #     print(row)
    # curr.close()
    
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")