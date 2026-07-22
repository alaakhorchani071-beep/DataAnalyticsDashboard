import sqlite3
import bcrypt


DATABASE_NAME = "database.db"


def create_user(first_name, last_name, email, password, language):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


    try:

        cursor.execute(
            """
            INSERT INTO users
            (first_name, last_name, email, password, language)

            VALUES (?, ?, ?, ?, ?)
            """,

            (
                first_name,
                last_name,
                email,
                hashed_password,
                language
            )
        )


        connection.commit()

        return True


    except sqlite3.IntegrityError:

        return False


    finally:

        connection.close()



def login_user(email, password):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,

        (email,)
    )


    user = cursor.fetchone()


    connection.close()


    if user:

        stored_password = user[4]


        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):

            return user


    return None