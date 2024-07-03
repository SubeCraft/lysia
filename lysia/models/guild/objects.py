__all__ = (
    "Guild",
    "GuildPreview",
    "UnavailableGuild",
    "GuildWidgetSettings",
    "GuildWidget",
    "GuildBan",
    "WelcomeScreen",
    "WelcomeScreenChannel"
)

from typing import TYPE_CHECKING

from pydantic import Field

from ..base import DiscordRessource, DiscordRESTRessource
from ..common.locales import Locales
from ..common.types import AssetHash, Snowflake
from ..role.objects import Role
from .enums import (
    DefaultMessageNotificationLevel,
    ExplicitContentFilterLevel,
    GuildFeatures,
    GuildMFALevel,
    GuildNSFWLevel,
    GuildPremiumTier,
    SystemChannelFlags,
    VerificationLevel,
)

if TYPE_CHECKING:
    from ..user.objects import User


class WelcomeScreenChannel(DiscordRessource):
    channel_id: Snowflake = Field(default="")
    """The channel's id."""

    description: str = Field(default="")
    """The description shown for the channel."""

    emoji_id: Snowflake | None = Field(default=None)
    """The emoji id, if the emoji is custom."""

    emoji_name: str | None = Field(default=None)
    """The emoji name if custom, the unicode character if standard, or null if no emoji is set."""


class WelcomeScreen(DiscordRessource):
    description: str | None = Field(default=None)
    """The server description shown in the welcome screen."""

    welcome_channels: list[WelcomeScreenChannel] = Field(default_factory=list)
    """The channels shown in the welcome screen, up to 5."""


class Guild(DiscordRESTRessource):
    """A Discord Guild."""

    id: Snowflake = Field(default="")
    """Guild id."""

    name: str = Field(default="")
    """Guild name."""

    icon: AssetHash | None = Field(default=None)
    """Guild icon hash."""

    icon_hash: AssetHash | None = Field(default=None)
    """Guild icon hash, returned when in the template object."""

    splash: AssetHash | None = Field(default=None)
    """Guild splash hash."""

    discovery_splash: AssetHash | None = Field(default=None)
    """Guild discovery splash hash."""

    owner: bool = Field(default=False)
    """True if the user is the owner of the guild"""

    owner_id: Snowflake = Field(default="")
    """Id of owner."""

    permissions: str = Field(default="")
    """Total permissions for the user in the guild (excludes overwrites and implicit permissions."""

    afk_channel_id: Snowflake | None = Field(default=None)
    """Id of afk channel."""

    afk_timeout: int = Field(default=0)
    """Afk timeout in seconds."""

    widget_enabled: bool = Field(default=False)
    """True if the server widget is enabled."""

    widget_channel_id: Snowflake | None = Field(default=None)
    """The channel id that the widget will generate an invite to, or None if set to no invite."""

    verification_level: VerificationLevel = Field(default=VerificationLevel.NONE)
    """Verification level required for the guild."""

    default_message_notifications: DefaultMessageNotificationLevel = Field(default=DefaultMessageNotificationLevel.ALL_MESSAGES)
    """Default message notifications level."""

    explicit_content_filter: ExplicitContentFilterLevel = Field(default=ExplicitContentFilterLevel.DISABLED)
    """Explicit content filter level."""

    roles: list[Role] = Field(default_factory=list)
    """Roles in the guild."""

    # emojis: list[Emoji] = Field(default_factory=list)
    """Custom guild emojis."""

    features: list[GuildFeatures] = Field(default_factory=list)
    """Enabled guild features."""

    mfa_level: GuildMFALevel = Field(default=GuildMFALevel.NONE)
    """Required MFA level for the guild."""

    application_id: Snowflake | None = Field(default=None)
    """Application id of the guild creator if it is bot-created."""

    system_channel_id: Snowflake | None = Field(default=None)
    """The id of the channel where guild notices such as welcome messages and boost events are posted."""

    system_channel_flags: SystemChannelFlags = Field(default=SystemChannelFlags.NONE)
    """System channel flags."""

    rules_channel_id: Snowflake | None = Field(default=None)
    """The id of the channel where Community guilds can display rules and/or guidelines."""

    max_presences: int | None = Field(default=None)
    """The maximum number of presences for the guild (null is always returned, apart from the largest of guilds)."""

    max_members: int | None = Field(default=None)
    """The maximum number of members for the guild."""

    vanity_url_code: AssetHash | None = Field(default="")
    """The vanity url code for the guild."""

    description: str | None = Field(default=None)
    """The description of a guild."""

    banner: AssetHash | None = Field(default=None)
    """Banner hash."""

    premium_tier: GuildPremiumTier = Field(default=GuildPremiumTier.NONE)
    """Premium tier (Server Boost level)."""

    premium_subscription_count: int = Field(default=0)
    """The number of boosts this guild currently has."""

    preferred_locale: Locales = Field(default=Locales.ENGLISH_US)
    """
    The preferred locale of a Community guild.
    Used in server discovery and notices from Discord, and sent in interactions; defaults to "en-US"
    """

    public_updates_channel_id: Snowflake | None = Field(default=None)
    """The id of the channel where admins and moderators of Community guilds receive notices from Discord."""

    max_video_channel_users: int | None = Field(default=None)
    """The maximum amount of users in a video channel."""

    max_stage_video_channel_users: int | None = Field(default=None)
    """The maximum amount of users in a stage video channel."""

    approximate_member_count: int | None = Field(default=None)
    """
    Approximate number of members in this guild,
    returned from the GET /guilds/<id> and /users/@me/guilds endpoints when with_counts is true.
    """

    approximate_presence_count: int | None = Field(default=None)
    """
    Approximate number of non-offline members in this guild,
    returned from the GET /guilds/<id> and /users/@me/guilds endpoints when with_counts is true.
    """

    welcome_screen: WelcomeScreen | None = Field(default=None)
    """The welcome screen of a Community guild, shown to new members, returned in an Invite's guild object."""

    nsfw_level: GuildNSFWLevel = Field(default=GuildNSFWLevel.DEFAULT)
    """Guild NSFW level."""

    # stickers: list[Sticker] = Field(default_factory=list)
    """Custom guild stickers."""

    premium_progress_bar_enabled: bool = Field(default=False)
    """Whether the guild has the boost progress bar enabled."""

    safety_alerts_channel_id: Snowflake | None = Field(default=None)
    """The id of the channel where admins and moderators of Community guilds receive safety alerts from Discord."""


class GuildPreview(DiscordRessource):
    """A Discord Guild Preview."""

    id: Snowflake = Field(default="")
    """Guild id."""

    name: str = Field(default="")
    """Guild name."""

    icon: AssetHash | None = Field(default=None)
    """Guild icon hash."""

    splash: AssetHash | None = Field(default=None)
    """Guild splash hash."""

    discovery_splash: AssetHash | None = Field(default=None)
    """Guild discovery splash hash."""

    # emojis: list[Emoji] = Field(default_factory=list)
    """Custom guild emojis."""

    features: list[GuildFeatures] = Field(default_factory=list)
    """Enabled guild features."""

    approximate_member_count: int | None = Field(default=None)
    """
    Approximate number of members in this guild,
    returned from the GET /guilds/<id> and /users/@me/guilds endpoints when with_counts is true.
    """

    approximate_presence_count: int | None = Field(default=None)
    """
    Approximate number of non-offline members in this guild,
    returned from the GET /guilds/<id> and /users/@me/guilds endpoints when with_counts is true.
    """

    description: str | None = Field(default=None)
    """The description of a guild."""

    # stickers: list[Sticker] = Field(default_factory=list)
    """Custom guild stickers."""


class UnavailableGuild(DiscordRessource):
    id: Snowflake = Field(default="")
    unavailable: bool = Field(default=True)


class GuildWidgetSettings(DiscordRessource):
    enabled: bool = Field(default=False)
    """Whether the widget is enabled."""

    channel_id: Snowflake | None = Field(default=None)
    """The widget channel id."""


class GuildWidget(DiscordRessource):
    id: Snowflake = Field(default="")
    """Guild id."""

    name: str = Field(default="")
    """Guild name (2-100 characters)."""

    instant_invite: str | None = Field(default=None)
    """Instant invite for the guilds specified widget invite channel."""

    # channels: list[Channel] = Field(default_factory=list)
    """Array of partial channel objects	voice and stage channels which are accessible by @everyone."""

    members: list["User"] = Field(default_factory=list)
    """Special widget user objects that includes users presence (Limit 100)."""

    presence_count: int = Field(default=0)
    """Number of online members in this guild."""


class GuildBan(DiscordRessource):
    """A Discord Member ban."""

    reason: str | None = Field(default=None)
    """The reason for the ban."""

    user: "User" = Field(default=None)
    """The banned user."""
