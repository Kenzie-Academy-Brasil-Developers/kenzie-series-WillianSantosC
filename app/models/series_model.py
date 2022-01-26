from os import getenv
import psycopg2

configs = {
    "host": getenv("DB_HOST"),
    "database": getenv("DB_NAME"),
    "user": getenv("DB_USER"),
    "password": getenv("DB_PASSWORD"),
}

class Series:

    def __init__(self, *args, **kwargs) -> None:
        self.serie = kwargs['serie'].title()
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre'].title()
        self.imdb_rating = kwargs['imdb_rating']

    @staticmethod
    def create():
        conn = psycopg2.connect(**configs)

        cur = conn.cursor()

        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            )
        """)

        conn.commit()

        cur.close()
        conn.close()
    
    @staticmethod
    def get_all():
        conn = psycopg2.connect(**configs)

        cur = conn.cursor()

        cur.execute("SELECT * FROM ka_series")

        series = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()

        return series

    @staticmethod
    def add_to_database(data: dict):
        conn = psycopg2.connect(**configs)

        cur = conn.cursor()

        query = ("""
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s,%s,%s,%s,%s)
            RETURNING *
        """)

        cur.execute(query, data)

        conn.commit()

        cur.close()
        conn.close()

    @staticmethod
    def get_by_id(serie_id: int):
        conn = psycopg2.connect(**configs)

        cur = conn.cursor()

        query = "SELECT * FROM ka_series WHERE id = %s"

        cur.execute(query,(serie_id,))

        result = cur.fetchall()

        conn.commit()

        cur.close()
        conn.close()

        return result

