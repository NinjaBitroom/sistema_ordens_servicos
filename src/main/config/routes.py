from flask import Flask

from src.main.routes.client_routes import client_blueprint
from src.main.routes.root_routes import root_blueprint


def setup_routes(app: Flask) -> None:
    app.register_blueprint(root_blueprint)
    app.register_blueprint(client_blueprint)
