__all__ = (
    "LibraryException",
    "HTTPException",
    "GatewayException",
    "Unauthorized",
    "Forbidden",
    "NotFound"
)

from typing import Any

from httpx import Response


class LibraryException(Exception):
    """The base class exception for all sub library exception."""


class HTTPException(LibraryException):
    """A HTTP error."""

    def __init__(self, response: Response, data: dict[str, Any]) -> None:
        self.response = response
        self.data = data


class GatewayException(LibraryException):
    """A Gateway error."""


class Unauthorized(HTTPException):
    """Triggered when the token is not valid."""


class Forbidden(HTTPException):
    """The token did not have permission to the ressource."""


class NotFound(HTTPException):
    """The URL doesn't exist."""
