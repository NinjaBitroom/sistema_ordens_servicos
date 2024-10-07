"""."""

from dataclasses import dataclass
from http import HTTPStatus


@dataclass
class HttpResponse[T]:
    """."""

    status_code: HTTPStatus
    body: T
