from flask import Blueprint
from app.controllers import retrieve_controler

bp_retrieve = Blueprint("retrieve", __name__)

bp_retrieve.get('/series')(retrieve_controler.get_all_series)