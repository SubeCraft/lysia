__all__ = ("RESTRoute",)

from typing import Any, Literal, Self

from pydantic import BaseModel, Field

from ....constants import DISCORD_REST_URL


class RESTRoute(BaseModel):
    method: Literal["GET", "POST", "PATCH", "DELETE", "PUT"] = Field()
    path: str = Field()

    def format(self, **args: Any) -> Self:
        """Return the self instance and format the path with URL parameters. Or just doing nothinh if no parameters present."""

        self.path = self.path.format_map(args)

        return self

    @property
    def url(self) -> str:
        """Return the full URL."""

        return DISCORD_REST_URL + self.path
