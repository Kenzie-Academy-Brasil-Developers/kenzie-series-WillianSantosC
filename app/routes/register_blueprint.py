from flask import Blueprint

from app.controllers import register_controller

bp_register = Blueprint("register", __name__)

bp_register.post('/series')(register_controller.add_serie)
