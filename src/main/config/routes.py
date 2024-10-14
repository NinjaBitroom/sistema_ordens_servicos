"""."""

from flask import Flask

from src.main.routes.brand_routes import BRAND_BLUEPRINT
from src.main.routes.client_routes import CLIENT_BLUEPRINT
from src.main.routes.employee_position_routes import (
    EMPLOYEE_POSITION_BLUEPRINT,
)
from src.main.routes.employee_routes import EMPLOYEE_BLUEPRINT
from src.main.routes.root_routes import ROOT_BLUEPRINT
from src.main.routes.service_order_routes import SERVICE_ORDER_BLUEPRINT
from src.main.routes.supplier_routes import SUPPLIER_BLUEPRINT


def setup_routes(app: Flask) -> None:
    """."""
    blueprints = (
        ROOT_BLUEPRINT,
        CLIENT_BLUEPRINT,
        SUPPLIER_BLUEPRINT,
        SERVICE_ORDER_BLUEPRINT,
        EMPLOYEE_BLUEPRINT,
        EMPLOYEE_POSITION_BLUEPRINT,
        BRAND_BLUEPRINT,
    )
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
