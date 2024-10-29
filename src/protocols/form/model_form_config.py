"""."""

from collections.abc import Iterable, Mapping
from typing import Any, TypedDict

from sqlmodel import Session
from wtforms_sqlalchemy.orm import (  # pyright: ignore[reportMissingTypeStubs]
    ModelConverterBase,
)


class ModelFormConfig(TypedDict, total=False):
    """."""

    db_session: Session
    converter: ModelConverterBase
    only: Iterable[str] | None
    field_args: Mapping[str, Mapping[str, Any]] | None
    type_name: str | None
    exclude: Iterable[str]
    exclude_pk: bool
    exclude_fk: bool
