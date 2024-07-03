__all__ = ("GuildMember",)

from datetime import datetime

from pydantic import Field

from ..base import DiscordRESTRessource
from ..common.types import AssetHash, Snowflake
from ..user.objects import User
from .enums import GuildMemberFlags


class GuildMember(DiscordRESTRessource):
    """A Discord Guild Member."""

    user: User | None = Field(default=None)
    """The user this guild member represents."""

    nick: str | None = Field(default=None)
    """This user's guild nickname."""

    avatar: AssetHash | None = Field(default=None)
    """The member's guild avatar hash."""

    roles: list[Snowflake] = Field(default_factory=list)
    """Array of role object ids."""

    joined_at: datetime = Field(default=datetime.now())
    """When the user joined the guild."""

    premium_since: datetime | None = Field(default=None)
    """When the user started boosting the guild."""

    deaf: bool = Field(default=False)
    """Whether the user is deafened in voice channels."""

    mute: bool = Field(default=False)
    """Whether the user is muted in voice channels."""

    flags: GuildMemberFlags = Field(default=GuildMemberFlags.NONE)
    """Guild member flags represented as a bit set, defaults to 0"""

    pending: bool | None = Field(default=None)
    """Whether the user has not yet passed the guild's Membership Screening requirements."""

    permissions: str | None = Field(default=None)
    """
    Total permissions of the member in the channel, including overwrites,
    returned when in the interaction object.
    """

    communication_disabled_until: datetime | None = Field(default=None)
    """
    When the user's timeout will expire and the user will be able to communicate in the guild again,
    null or a time in the past if the user is not timed out.
    """
