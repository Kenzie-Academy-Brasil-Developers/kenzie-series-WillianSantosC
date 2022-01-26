from flask import jsonify
from psycopg2 import errors

from app.models.series_model import Series
from app.models import conn

def get_serie_by_id(serie_id: int):
    try:
        Series.get_by_id(serie_id)
    except errors.UndefinedTable:
        conn.rollback()
        Series.create()
        return jsonify(data= {}), 404
    
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

    serie_list = [dict(zip(serie_keys, serie)) for serie in Series.get_by_id(serie_id)]

    if serie_list == []: 
        return jsonify(data= {}), 404

    return jsonify(data= serie_list), 200

