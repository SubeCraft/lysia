__all__ = ("DiscordRessource",)

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ..implementations.http.client import HTTPClient


class DiscordRessource(BaseModel):
    """A base class for all Discord ressources who need rest method."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    rest: HTTPClient = Field(default=None, repr=False)

    def dump(self) -> dict[str, Any]:
        """Return the model without rest field."""

        return self.model_dump(exclude={"rest"})
