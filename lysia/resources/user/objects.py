__all__ = ("User", "ClientUser")

from pydantic import Field

from ...implementations.http.routes.user import UserRoutes
from ..base import DiscordRessource
from ..common.locales import Locales
from ..common.types import AssetHash, Snowflake
from .enums import PremiumTypes, UserFlags


class User(DiscordRessource):
    """A Discord User."""
    
    id: Snowflake = Field(default="")
    """The user's id."""

    username: str = Field(default="")
    """The user's username."""

    discriminator: str = Field(default="0")
    """The user's Discord-tag."""

    global_name: str | None = Field(default=None)
    """The user's display name, if it is set. For bots, this is the application name."""

    avatar: AssetHash | None = Field(default=None)
    """The user's avatar hash."""

    bot: bool = Field(default=False)
    """Whether the user belongs to an OAuth2 application."""

    system: bool = Field(default=False)
    """Whether the user is an Official Discord System user (part of the urgent message system)."""

    mfa_enabled: bool = Field(default=False)
    """Whether the user has two factor enabled on their account."""

    banner: str | None = Field(default=None)
    """The user's banner hash"""

    accent_color: int | None = Field(default=None)
    """The user's banner color encoded as an integer representation of hexadecimal color code."""

    locale: Locales = Field(default=Locales.ENGLISH_US)
    """The user's chosen language option."""

    verified: bool = Field(default=False)
    """Whether the email on this account has been verified."""

    email: str | None = Field(default=None)
    """The user's email"""

    flags: UserFlags = Field(default=UserFlags.NONE)
    """The flags on a user's account."""

    premium_type: PremiumTypes = Field(default=PremiumTypes.NONE)
    """The type of Nitro subscription on a user's account."""

    public_flags: UserFlags = Field(default=UserFlags.NONE)
    """The public flags on a user's account."""

    avatar_decoration: AssetHash | None = Field(default=None)
    """The user's avatar decoration hash."""


class ClientUser(User):
    """A Discord Client User."""

    async def get_current_user(self) -> "ClientUser":
        """
        Returns the user object of the requester's account.
        For OAuth2, this requires the identify scope, which will return the object without an email,
        and optionally the email scope, which returns the object with an email.
        """

        return ClientUser(rest=self.rest, **await self.rest.request(UserRoutes.GET_CURRENT_USER))

    async def get_user(self, user_id: str) -> "User":
        """Returns a user object for a given user ID."""

        return User(rest=self.rest, **await self.rest.request(UserRoutes.GET_USER.format(user_id=user_id)))

    async def modify_current_user(
            self,
            username: str | None = None,
            avatar: str | None = None
    ) -> "ClientUser":
        """
        Returns a list of partial guild objects the current user is a member of.
        For OAuth2, requires the guilds scope.
        """

        payload: dict[str, str] = {}

        if username: payload["username"] = username
        if avatar: payload["avatar"] = avatar

        return ClientUser(
            rest=self.rest,
            **await self.rest.request(UserRoutes.MODIFY_CURRENT_USER, payload=payload)
        )

    async def leave_guild(self, guild_id: str) -> None:
        """Leave a guild."""

        await self.rest.request(UserRoutes.LEAVE_GUILD.format(guild_id=guild_id))

    # TODO: Add the following routes
    # https://discord.com/developers/docs/resources/user#get-current-user-guilds
    # https://discord.com/developers/docs/resources/user#get-current-user-guild-member
    # https://discord.com/developers/docs/resources/user#create-dm
    # https://discord.com/developers/docs/resources/user#create-group-dm
    # https://discord.com/developers/docs/resources/user#get-current-user-connections
    # https://discord.com/developers/docs/resources/user#get-current-user-application-role-connection
    # https://discord.com/developers/docs/resources/user#update-current-user-application-role-connection

