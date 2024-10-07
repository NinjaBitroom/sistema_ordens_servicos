"""."""

from dataclasses import dataclass
from http import HTTPMethod


@dataclass
class HttpRequest[T]:
    """."""

    method: HTTPMethod
    body: T
