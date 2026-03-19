import sqlite3

def create_db():
    conn = sqlite3.connect("satellites.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        satellite TEXT,
        start_time TEXT,
        end_time TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_pass(satellite, start, end):
    conn = sqlite3.connect("satellites.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO passes (satellite, start_time, end_time)
    VALUES (?, ?, ?)
    """, (satellite, str(start), str(end)))

    conn.commit()
    conn.close()


def get_all_passes():
    conn = sqlite3.connect("satellites.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM passes")
    rows = cursor.fetchall()

    conn.close()
    return rows


# TEST
if __name__ == "__main__":
    create_db()

    insert_pass("ISS", "10:00", "10:05")
    insert_pass("Hubble", "11:00", "11:06")

    data = get_all_passes()
    print(data)