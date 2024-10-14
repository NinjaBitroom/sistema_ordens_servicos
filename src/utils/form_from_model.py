"""."""

from collections.abc import Iterable, Mapping
from typing import Any, Unpack

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from sqlmodel import SQLModel
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.protocols.form.exclusion_config import ExclusionConfig
from src.services.extensions.database import DB
from src.utils.sql_model_converter import (
    SqlModelConverter,
)


def make_form_from_model(
    model: type[SQLModel],
    only: Iterable[str] | None = None,
    field_args: Mapping[str, Mapping[str, Any]] | None = None,
    type_name: str | None = None,
    **exclusion_config: Unpack[ExclusionConfig],
) -> type[FlaskForm]:
    """."""
    return model_form(
        model=model,
        db_session=DB.session,
        base_class=FlaskForm,
        converter=SqlModelConverter(),
        field_args=field_args,
        only=only,
        type_name=type_name,
        exclude=exclusion_config.get("exclude"),
        exclude_pk=exclusion_config.get("exclude_pk", True),
        exclude_fk=exclusion_config.get("exclude_fk", True),
    )
