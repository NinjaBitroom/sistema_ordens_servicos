"""."""

from dataclasses import fields
from typing import cast

from src.forms.cliente_form import ClienteForm
from src.models.cliente_model import ClienteModel
from src.protocols.db_add_one_operation import DbAddOneOperation
from src.protocols.form_controller import FormController
from src.services.base_model import BaseModel


class ClientCreateController(FormController):
    """."""

    def __init__(
        self,
        form: ClienteForm,
        db_add_one_operation: DbAddOneOperation[ClienteModel],
    ) -> None:
        """."""
        self.form = form
        self.db_add_one_operation = db_add_one_operation

    def validate(self) -> None | Exception:
        """."""
        if self.form.validate_on_submit():
            cleaned_data = {}
            for field in fields(cast(BaseModel, ClienteModel)):
                if field.name not in self.form.data:
                    continue
                cleaned_data[field.name] = getattr(self.form, field.name).data
            self.db_add_one_operation.add_one(ClienteModel(**cleaned_data))
            return None
        errors_list = list[str]()
        for field, errors in self.form.errors.items():
            for error in errors:
                errors_list.append(f"{field}: {error}")
        return Exception(*errors_list)
