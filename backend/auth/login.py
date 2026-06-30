import bcrypt

from backend.database.database import get_connection


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,
               full_name,
               email,
               password,
               role
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return False, "Invalid Email"

    stored_password = user[3]

    if bcrypt.checkpw(
        password.encode(),
        stored_password.encode()
    ):

        return True, {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "role": user[4]
        }

    return False, "Incorrect Password"