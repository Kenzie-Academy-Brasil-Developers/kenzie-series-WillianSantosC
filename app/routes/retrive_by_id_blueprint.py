from flask import Blueprint

from app.controllers import retrieve_by_id_controller
bp_retrieve_by_id = Blueprint("retrieve_id", __name__)

bp_retrieve_by_id.get('/series/<int:serie_id>')(retrieve_by_id_controller.get_serie_by_id)