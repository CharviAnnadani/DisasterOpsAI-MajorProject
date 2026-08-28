import sqlite3

conn = sqlite3.connect("disasterops.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sos_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    location TEXT NOT NULL,
    disaster_type TEXT NOT NULL,
    description TEXT NOT NULL,
    priority INTEGER,
    assigned_team TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database Initialized Successfully")