"""."""

from flask import Flask

from src.main.routes.client_routes import CLIENT_BLUEPRINT
from src.main.routes.root_routes import ROOT_BLUEPRINT
from src.main.routes.service_order_routes import SERVICE_ORDER_BLUEPRINT
from src.main.routes.supplier_routes import SUPPLIER_BLUEPRINT


def setup_routes(app: Flask) -> None:
    """."""
    app.register_blueprint(ROOT_BLUEPRINT)
    app.register_blueprint(CLIENT_BLUEPRINT)
    app.register_blueprint(SUPPLIER_BLUEPRINT)
    app.register_blueprint(SERVICE_ORDER_BLUEPRINT)
