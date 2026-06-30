import sqlite3

DATABASE_NAME = "database/healthcare.db"


def get_connection():
    """
    Create SQLite connection.
    """

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    return conn