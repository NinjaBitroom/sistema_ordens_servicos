"""."""

from collections.abc import Iterable, Mapping
from typing import Any, Unpack

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from sqlmodel import SQLModel
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.protocols.form.exclusion_config import ExclusionConfig
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
        model: type[TModel] | None = None,
        only: Iterable[str] | None = None,
        field_args: Mapping[str, Mapping[str, Any]] | None = None,
        type_name: str | None = None,
        **exclusion_config: Unpack[ExclusionConfig],
    ) -> None:
        """."""
        self.__MODEL = model
        self.__ONLY = only
        self.__FIELD_ARGS = field_args
        self.__TYPE_NAME = type_name
        self.__EXCLUSION_CONFIG = exclusion_config

    def model_type_to_form_type(
        self, model_class: type[TModel]
    ) -> type[TForm]:
        """."""
        return model_form(
            model=model_class,
            db_session=DB.session,
            base_class=FlaskForm,
            converter=SqlModelConverter(),
            field_args=self.__FIELD_ARGS,
            only=self.__ONLY,
            type_name=self.__TYPE_NAME,
            exclude=self.__EXCLUSION_CONFIG.get("exclude"),
            exclude_pk=self.__EXCLUSION_CONFIG.get("exclude_pk", True),
            exclude_fk=self.__EXCLUSION_CONFIG.get("exclude_fk", True),
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
