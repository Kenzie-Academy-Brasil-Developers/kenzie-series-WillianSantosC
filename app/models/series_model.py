from app.models import DatabaseConnector


class Series(DatabaseConnector):

    def __init__(self, *args, **kwargs) -> None:
        self.serie = kwargs['serie'].title()
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre'].title()
        self.imdb_rating = kwargs['imdb_rating']

    @classmethod
    def create(cls):
        cls.get_conn_cur()
        
        cls.cur.execute(""" 
            CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            )
        """)

        cls.commit_and_close()
    
    @classmethod
    def get_all(cls):
        cls.get_conn_cur()

        cls.cur.execute("SELECT * FROM ka_series")

        series = cls.cur.fetchall()

        cls.commit_and_close()

        return series

    @classmethod
    def add_to_database(cls,data: dict):
        cls.get_conn_cur()

        query = ("""
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s,%s,%s,%s,%s)
            RETURNING *
        """)

        cls.cur.execute(query, data)

        cls.commit_and_close()

    @classmethod
    def get_by_id(cls,serie_id: int):
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series WHERE id = %s"

        cls.cur.execute(query,(serie_id,))

        result = cls.cur.fetchall()

        cls.commit_and_close()

        return result

