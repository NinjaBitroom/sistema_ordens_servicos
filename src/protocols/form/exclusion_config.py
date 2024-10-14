"""."""

from collections.abc import Iterable
from typing import TypedDict


class ExclusionConfig(TypedDict, total=False):
    """."""

    exclude: Iterable[str]
    exclude_pk: bool
    exclude_fk: bool
