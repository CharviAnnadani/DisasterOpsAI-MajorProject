from database.db import get_connection

def create_sos(name, latitude, longitude, disaster_type, priority, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sos_requests
        (name, latitude, longitude, disaster_type, priority, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, latitude, longitude, disaster_type, priority, status))

    conn.commit()
    conn.close()


def get_all_sos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sos_requests")

    rows = cursor.fetchall()

    data = [dict(row) for row in rows]

    conn.close()

    return data


def update_sos_status(sos_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE sos_requests
        SET status = ?
        WHERE id = ?
    """, (status, sos_id))

    conn.commit()
    conn.close()


def delete_sos(sos_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM sos_requests
        WHERE id = ?
    """, (sos_id,))

    conn.commit()
    conn.close()