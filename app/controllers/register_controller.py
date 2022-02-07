from flask import jsonify, request
from psycopg2 import errors

from app.models.series_model import Series

def add_serie():
    data = request.get_json()

    try:
        new_serie = Series(**data).__dict__
    except KeyError:
         return {
                    "error": "chave(s) incorreta(s)",
                    "permitidas": [
                    "serie",
                    "seasons",
                    "released_date",
                    "genre",
                    "imdb_rating"
                    ],
                    "recebidas": list(data.keys())
                 }, 400
    
    try:
        Series.add_to_database(list(new_serie.values()))
    except errors.UniqueViolation:
        return jsonify(erro= 'Série já cadastrada!'), 422
    except errors.UndefinedTable:
        Series.create()

    return jsonify(new_serie), 201