__all__ = (
    "Role",
    "RoleTags"
)

from pydantic import Field

from ..base import DiscordRessource
from ..common.types import Snowflake
from .enums import RoleFlags


class RoleTags(DiscordRessource):
    bot_id: Snowflake | None = Field(default=None)
    """The id of the bot this role belongs to."""

    integration_id: Snowflake | None = Field(default=None)
    """The id of the integration this role belongs to."""

    premium_subscriber: None = Field(default=None)
    """Whether this is the guild's Booster role."""

    subscription_listing_id: Snowflake | None = Field(default=None)
    """The id of this role's subscription sku and listing."""

    available_for_purchase: None = Field(default=None)
    """Whether this role is available for purchase."""

    guild_connections: None = Field(default=None)
    """Whether this role is a guild's linked role."""


class Role(DiscordRessource):
    """Roles represent a set of permissions attached to a group of users."""

    id: Snowflake = Field(default="")
    """Role id."""

    name: str = Field(default="")
    """Role name."""

    color: int = Field(default=0)
    """Integer representation of hexadecimal color code."""

    hoist: bool = Field(default=False)
    """If this role is pinned in the user listing."""

    icon: str | None = Field(default=None)
    """Role icon hash."""

    unicode_emoji: str | None = Field(default=None)
    """Role icon emoji hash."""

    position: int = Field(default=0)
    """Position of this role."""

    permissions: str = Field(default="")
    """Permission bit set."""

    managed: bool = Field(default=False)
    """Whether this role is managed by an integration."""

    mentionable: bool = Field(default=False)
    """Whether this role is mentionable."""

    tags: RoleTags | None = Field(default=None)
    """The tags this role has."""

    flags: RoleFlags = Field(default=0)
    """Role flags combined as a bitfield."""
