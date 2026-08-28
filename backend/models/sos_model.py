from database.db import get_connection


def create_sos(
    name,
    phone,
    location,
    disaster_type,
    description,
    priority,
    assigned_team,
    status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sos_requests
        (
            name,
            phone,
            location,
            disaster_type,
            description,
            priority,
            assigned_team,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        name,
        phone,
        location,
        disaster_type,
        description,
        priority,
        assigned_team,
        status
    ))

    conn.commit()
    conn.close()


def get_all_sos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sos_requests")

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:

        data.append({
            "id": row[0],
            "name": row[1],
            "phone": row[2],
            "location": row[3],
            "disaster_type": row[4],
            "description": row[5],
            "priority": row[6],
            "assigned_team": row[7],
            "status": row[8]
        })

    return data


def update_sos_status(sos_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE sos_requests SET status=? WHERE id=?",
        (status, sos_id)
    )

    conn.commit()
    conn.close()


def delete_sos(sos_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sos_requests WHERE id=?",
        (sos_id,)
    )

    conn.commit()
    conn.close()


def get_dashboard_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM sos_requests"
    )
    total_requests = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM sos_requests WHERE priority >= 4"
    )
    high_priority = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(DISTINCT assigned_team) FROM sos_requests"
    )
    active_teams = cursor.fetchone()[0]

    conn.close()

    return {
        "total_requests": total_requests,
        "high_priority": high_priority,
        "active_teams": active_teams
    }