from flask import jsonify
from psycopg2 import errors

from app.models.series_model import Series

def get_all_series():
    try:
        Series.get_all()
    except errors.UndefinedTable:
        Series.create()

    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

    series_list = [dict(zip(serie_keys, serie)) for serie in Series.get_all()]

    return jsonify(data= series_list), 200