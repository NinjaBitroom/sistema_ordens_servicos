"""."""

from dataclasses import fields
from typing import cast

from src.forms.cliente_form import ClienteForm
from src.models.cliente_model import ClienteModel
from src.protocols.controller import Controller
from src.protocols.db_add_one_operation import DbAddOneOperation
from src.protocols.validaton import Validation
from src.services.base_model import BaseModel


class ClientCreateController(Controller):
    """."""

    def __init__(
        self,
        validation: Validation,
        db_add_one_operation: DbAddOneOperation[ClienteModel],
    ) -> None:
        """."""
        self.validation = validation
        self.db_add_one_operation = db_add_one_operation

    def handle(self, request: ClienteForm) -> None | Exception:
        """."""
        exception = self.validation.validate(request)
        if exception is None:
            cleaned_data = {}
            for field in fields(cast(BaseModel, ClienteModel)):
                if field.name not in request.data:
                    continue
                cleaned_data[field.name] = getattr(request, field.name).data
            self.db_add_one_operation.add_one(ClienteModel(**cleaned_data))
            return None
        return exception
