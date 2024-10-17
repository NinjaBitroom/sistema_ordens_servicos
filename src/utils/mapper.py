"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from sqlmodel import SQLModel
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.protocols.form.model_form_config import ModelFormConfig
from src.protocols.helpers.form_to_model_operation import FormToModelOperation
from src.protocols.helpers.model_type_to_form_type_operation import (
    ModelTypeToFormTypeOperation,
)
from src.services.extensions.database import DB
from src.utils.sql_model_converter import SqlModelConverter


class Mapper[TForm: FlaskForm, TModel: SQLModel](
    ModelTypeToFormTypeOperation[TModel, TForm],
    FormToModelOperation[TForm, TModel],
):
    """."""

    def __init__(
        self,
        model: type[TModel],
        form: type[TForm],
        model_form_config: ModelFormConfig,
    ) -> None:
        """."""
        self.__MODEL = model
        self.__FORM = form
        self.__MODEL_FORM_CONFIG = model_form_config

    def model_type_to_form_type(
        self, model_class: type[TModel]
    ) -> type[TForm]:
        """."""
        return model_form(
            model=model_class,
            db_session=self.__MODEL_FORM_CONFIG.get("db_session", DB.session),
            base_class=self.__FORM,
            converter=self.__MODEL_FORM_CONFIG.get(
                "converter", SqlModelConverter()
            ),
            field_args=self.__MODEL_FORM_CONFIG.get("field_args"),
            only=self.__MODEL_FORM_CONFIG.get("only"),
            type_name=self.__MODEL_FORM_CONFIG.get("type_name"),
            exclude=self.__MODEL_FORM_CONFIG.get("exclude"),
            exclude_pk=self.__MODEL_FORM_CONFIG.get("exclude_pk", True),
            exclude_fk=self.__MODEL_FORM_CONFIG.get("exclude_fk", True),
        )

    def form_to_model(self, form: TForm) -> TModel:
        """."""
        if not self.__MODEL:
            msg = "Model not set"
            raise ValueError(msg)
        cleaned_data = {}
        for field in self.__MODEL.model_fields:
            if form.data.get(field) is None:
                continue
            if isinstance(form.data[field], SQLModel):
                cleaned_data[f"{field}_id"] = form.data[field].id
            cleaned_data[field] = form.data[field]
        return self.__MODEL(**cleaned_data)
