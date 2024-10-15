"""."""

from collections.abc import Iterable, Mapping
from typing import Any, Unpack

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from sqlmodel import SQLModel
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.protocols.form.exclusion_config import ExclusionConfig
from src.protocols.helpers.model_to_form_operation import ModelToFormOperation
from src.services.extensions.database import DB
from src.utils.sql_model_converter import SqlModelConverter


class Mapper(ModelToFormOperation[SQLModel, FlaskForm]):
    """."""

    def __init__(
        self,
        only: Iterable[str] | None = None,
        field_args: Mapping[str, Mapping[str, Any]] | None = None,
        type_name: str | None = None,
        **exclusion_config: Unpack[ExclusionConfig],
    ) -> None:
        """."""
        self.__ONLY = only
        self.__FIELD_ARGS = field_args
        self.__TYPE_NAME = type_name
        self.__EXCLUSION_CONFIG = exclusion_config

    def model_to_form(self, model: type[SQLModel]) -> type[FlaskForm]:
        """."""
        return model_form(
            model=model,
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
