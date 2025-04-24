from app import get_connection
import time

# نحاول الاتصال عدة مرات لتجنب crash لو كانت قاعدة البيانات تتأخر
for i in range(10):
    try:
        conn = get_connection()
        break
    except Exception as e:
        print(f"Waiting for db... ({i+1}/10)")
        time.sleep(3)
else:
    raise Exception("Database connection failed after 10 attempts")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
)
""")

cur.execute("INSERT INTO users (username, password) VALUES (%s, %s) ON CONFLICT DO NOTHING", ("admin", "password"))

conn.commit()
conn.close()
