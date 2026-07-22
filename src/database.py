import sqlite3


DATABASE_NAME = "database.db"


def create_database():
    """
    Crée la base de données et la table users si elles n'existent pas.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            first_name TEXT NOT NULL,

            last_name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            language TEXT DEFAULT 'Français'

        )
    """)

    connection.commit()

    connection.close()
    