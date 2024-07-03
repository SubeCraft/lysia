__all__ = ("DiscordRessource", "DiscordRESTRessource")

from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator

from ..modules.core.http import HTTPClient


class DiscordRessource(BaseModel):
    """A base class for all Discord ressources."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class DiscordRESTRessource(DiscordRessource):
    """A base class for all Discord ressources who need rest attribute."""

    rest: HTTPClient = Field(None, exclude=True, repr=False)
    """The HTTP client."""

    @field_validator("*")
    @classmethod
    def add_rest_field[T](cls, value: T, _info: ValidationInfo) -> T:
        """Set the rest field at HTTPClient in any DiscordRESTRessource subclass."""

        if isinstance(value, DiscordRESTRessource):
            value.rest = _info.data["rest"]

        return value
