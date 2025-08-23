import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

dburl = os.getenv("DATABASE_URL")
try:
    conn = psycopg2.connect(dburl)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")