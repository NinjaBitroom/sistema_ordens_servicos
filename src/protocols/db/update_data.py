"""."""

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass
class UpdateData[T]:
    """."""

    object: T
    data: Mapping[Any, Any]
