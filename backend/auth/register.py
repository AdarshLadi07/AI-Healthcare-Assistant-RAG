import bcrypt

from backend.database.database import get_connection


def register_user(full_name, email, password, role="Patient"):
    """
    Register a new user.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return False, "Email already registered."

    # Hash password
    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    # Insert new user
    cursor.execute(
        """
        INSERT INTO users
        (full_name, email, password, role)
        VALUES (?, ?, ?, ?)
        """,
        (
            full_name,
            email,
            hashed_password.decode(),
            role
        )
    )

    conn.commit()
    conn.close()

    return True, "Registration Successful."