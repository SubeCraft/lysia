__all__ = (
    "LibraryError",
    "HTTPError",
    "Unauthorized",
    "Forbidden",
    "NotFound"
)

from httpx import Response
from pydantic import ConfigDict
from pydantic.dataclasses import dataclass


@dataclass(config=ConfigDict(arbitrary_types_allowed=True))
class LibraryError(RuntimeError):
    """Base class for all sub error."""

    message: str
    "The text of the error."


@dataclass
class HTTPError(LibraryError):
    """A HTTP error."""

    response: Response
    "The response of the HTTP request."


class Unauthorized(HTTPError):
    """The token is not valid."""


class Forbidden(HTTPError):
    """The token did not have permission to the ressource."""


class NotFound(HTTPError):
    """The URL doesn't exist."""
