from flask import jsonify, request
from psycopg2 import errors

from app.models import conn
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
    
    serie = (new_serie['serie'], new_serie['seasons'], new_serie['released_date'], new_serie['genre'], new_serie['imdb_rating'])
   
    Series.add_to_database(serie)

    return jsonify(new_serie), 201