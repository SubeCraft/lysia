__all__ = (
    "Restable",
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..implementations.internal.rest import InternalRestClient


class Restable:
    def __init__(self, rest: "InternalRestClient") -> None: self.rest = rest
