from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sos_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    disaster_type TEXT,
    priority INTEGER,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized successfully!")