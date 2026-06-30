from backend.database.database import get_connection


def create_users_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        role TEXT DEFAULT 'user'
    )
    """)

    conn.commit()

    conn.close()


def create_chat_history_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_email TEXT NOT NULL,

        question TEXT NOT NULL,

        answer TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()


def initialize_database():

    create_users_table()

    create_chat_history_table()