from backend.database.database import get_connection


def execute_query(query, values=()):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    conn.commit()
    conn.close()


def fetch_one(query, values=()):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    data = cursor.fetchone()

    conn.close()

    return data


def fetch_all(query, values=()):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    data = cursor.fetchall()

    conn.close()

    return data


# ========================================
# CHAT HISTORY
# ========================================

def save_chat(user_email, question, answer):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history(
            user_email,
            question,
            answer
        )
        VALUES(?,?,?)
        """,
        (user_email, question, answer)
    )

    conn.commit()
    conn.close()


def get_chat_history(user_email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question,
               answer,
               created_at
        FROM chat_history
        WHERE user_email=?
        ORDER BY id DESC
        """,
        (user_email,)
    )

    history = cursor.fetchall()

    conn.close()

    return history