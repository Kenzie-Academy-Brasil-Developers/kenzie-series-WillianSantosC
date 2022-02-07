from flask import Flask
from flask import Flask

from app.routes.register_blueprint import bp_register
from app.routes.retrieve_blueprint import bp_retrieve
from app.routes.retrive_by_id_blueprint import bp_retrieve_by_id

def init_app(app: Flask):
    app.register_blueprint(bp_register)
    app.register_blueprint(bp_retrieve)
    app.register_blueprint(bp_retrieve_by_id)