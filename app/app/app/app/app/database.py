import sqlite3


DATABASE = "library.db"


def connect():

    return sqlite3.connect(
        DATABASE
    )


def create_database():

    db = connect()

    cursor = db.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tracks (

            id INTEGER PRIMARY KEY,

            file TEXT,

            rating INTEGER DEFAULT 0,

            color TEXT DEFAULT '',

            event TEXT DEFAULT '',

            energy TEXT DEFAULT '',

            mood TEXT DEFAULT ''

        )
        """
    )

    db.commit()

    db.close()
