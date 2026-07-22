import sqlite3
import bcrypt


DATABASE_NAME = "database.db"



# ==========================
# CREER UN UTILISATEUR
# ==========================

def register_user(username, password):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()


    # Vérifier si l'utilisateur existe

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,)
    )


    existing_user = cursor.fetchone()


    if existing_user:

        connection.close()

        return False



    # Crypter le mot de passe

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


    cursor.execute(
        """
        INSERT INTO users
        (username, password)

        VALUES (?, ?)
        """,

        (
            username,
            hashed_password
        )
    )


    connection.commit()

    connection.close()


    return True





# ==========================
# CONNEXION UTILISATEUR
# ==========================

def login_user(username, password):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,

        (username,)
    )


    user = cursor.fetchone()


    connection.close()


    if user:


        stored_password = user[2]


        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):

            return True


    return False