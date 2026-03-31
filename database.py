import sqlite3

conn = sqlite3.connect("project.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
score INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
task_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
task TEXT,
points INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")

