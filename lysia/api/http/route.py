from typing import Literal

from ...constants import DISCORD_API_URL

METHOD = Literal[
    "GET",
    "POST",
    "PUT",
    "DELETE",
]


class Route:
    def __init__(self, method: METHOD, path: str) -> None:
        self.method = method
        self.path = path

    @property
    def url(self) -> str:
        return f"{DISCORD_API_URL}/{self.path}"
