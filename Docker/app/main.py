import os
import time
import psycopg2
from fastapi import FastAPI

app = FastAPI()

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

def get_conn():
    # simple retry so the API waits for Postgres to be ready
    for _ in range(20):
        try:
            return psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        except Exception:
            time.sleep(0.5)
        raise RuntimeError("Could not connect to DB")
    
@app.on_event("startup")
def startup():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            ts TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.get("/")
def root():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES RETURNING id;")
    new_id = cur.fetchone()[0]
    conn.commit()
    
    cur.execute("SELECT COUNT(*) FROM visits;")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()
    return {"message": "Hello from Docker!", "new_visit_id": new_id, "total_visits": count}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello {name}"}