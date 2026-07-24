import sqlite3


DATABASE_NAME = "database.db"



def create_database():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()


    # Table utilisateurs

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            email TEXT,

            password TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            language TEXT DEFAULT 'English'

        )
        """
    )



    # Table historique

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            filename TEXT,

            action TEXT,

            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )



    connection.commit()

    connection.close()
