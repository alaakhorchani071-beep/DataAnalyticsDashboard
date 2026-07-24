import sqlite3
import bcrypt


DATABASE_NAME = "database.db"



# ==========================
# CREATION D'UN COMPTE
# ==========================

def register_user(username, email, password, language):


    connection = sqlite3.connect(
        DATABASE_NAME
    )


    cursor = connection.cursor()



    # Vérifier si l'utilisateur existe déjà

    cursor.execute(
        """
        SELECT username
        FROM users
        WHERE username = ?
        """,
        (username,)
    )


    user = cursor.fetchone()



    if user:

        connection.close()

        return False



    # Crypter le mot de passe

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )



    # Ajouter l'utilisateur

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            email,
            password,
            language
        )

        VALUES (?, ?, ?, ?)

        """,
        (
            username,
            email,
            hashed_password,
            language
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
        SELECT password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )



    user = cursor.fetchone()



    connection.close()



    if user:


        stored_password = user[0]



        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):

            return True



    return False





# ==========================
# RECUPERER PROFIL UTILISATEUR
# ==========================

def get_user_profile(username):


    connection = sqlite3.connect(
        DATABASE_NAME
    )


    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT 
            username,
            email,
            language,
            created_at

        FROM users

        WHERE username = ?

        """,
        (username,)
    )



    user = cursor.fetchone()



    connection.close()



    return user
def get_user_statistics(username):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username = ?
        """,
        (username,)
    )


    total_actions = cursor.fetchone()[0]


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username = ?
        AND action = 'Report'
        """,
        (username,)
    )


    total_reports = cursor.fetchone()[0]


    connection.close()


    return total_actions, total_reports
