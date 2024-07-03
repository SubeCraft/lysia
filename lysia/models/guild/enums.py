__all__ = (
    "DefaultMessageNotificationLevel",
    "ExplicitContentFilterLevel",
    "GuildMFALevel",
    "VerificationLevel",
    "GuildNSFWLevel",
    "GuildPremiumTier",
    "SystemChannelFlags",
    "GuildFeatures",
    "GuildMutableFeatures"
)

from enum import Enum, IntEnum, IntFlag, StrEnum


class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    """Members will receive notifications for all messages by default"""

    ONLY_MENTIONS = 1
    """Members will receive notifications only for messages that @mention them by default."""


class ExplicitContentFilterLevel(IntEnum):
    DISABLED = 0
    """Media content will not be scanned."""

    MEMBERS_WITHOUT_ROLES = 1
    """Media content sent by members without roles will be scanned."""

    ALL_MEMBERS = 2
    """Media content sent by all members will be scanned."""


class GuildMFALevel(IntEnum):
    NONE = 0
    """Guild has no MFA/2FA requirement for moderation actions."""

    ELEVATED = 1
    """Guild has a 2FA requirement for moderation actions."""


class VerificationLevel(IntEnum):
    NONE = 0
    """Unrestricted."""

    LOW = 1
    """Must have verified email on account ."""

    MEDIUM = 2
    """Must be registered on Discord for longer than 5 minutes."""

    HIGH = 3
    """Must be a member of the server for longer than 10 minutes."""

    VERY_HIGH = 4
    """Must have a verified phone number."""


class GuildNSFWLevel(IntEnum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class GuildPremiumTier(IntEnum):
    NONE = 0
    """Guild has not unlocked any Server Boost perks."""

    TIER_1 = 1
    """Guild has unlocked Server Boost level 1 perks."""

    TIER_2 = 2
    """Guild has unlocked Server Boost level 2 perks."""

    TIER_3 = 3
    """Guild has unlocked Server Boost level 3 perks."""


class SystemChannelFlags(IntFlag):
    NONE = 0

    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    """Suppress member join notifications."""

    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    """Suppress server boost notifications."""

    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    """Suppress server setup tips."""

    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    """Hide member join sticker reply buttons."""

    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    """Suppress role subscription purchase and renewal notifications."""

    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5
    """Hide role subscription sticker reply buttons."""


class GuildFeatures(str, Enum):
    ANIMATED_BANNER = "ANIMATED_BANNER"
    """Guild has access to set an animated guild banner image."""

    ANIMATED_ICON = "ANIMATED_ICON"
    """Guild has access to set an animated guild icon."""

    APPLICATION_COMMAND_PERMISSIONS_V2 = "APPLICATION_COMMAND_PERMISSIONS_V2"
    """Guild is using the old permissions configuration behavior."""

    AUTO_MODERATION = "AUTO_MODERATION"
    """Guild has set up auto moderation rules."""

    BANNER = "BANNER"
    """Guild has access to set a guild banner image."""

    COMMUNITY = "COMMUNITY"
    """Guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates."""

    CREATOR_MONETIZABLE_PROVISIONAL = "CREATOR_MONETIZABLE_PROVISIONAL"
    """Guild has enabled monetization."""

    CREATOR_STORE_PAGE = "CREATOR_STORE_PAGE"
    """Guild has enabled the role subscription promo page."""

    DEVELOPER_SUPPORT_SERVER = "DEVELOPER_SUPPORT_SERVER"
    """Guild has been set as a support server on the App Directory."""

    DISCOVERABLE = "DISCOVERABLE"
    """Guild is able to be discovered in the directory."""

    FEATURABLE = "FEATURABLE"
    """Guild is able to be featured in the directory."""

    INVITES_DISABLED = "INVITES_DISABLED"
    """Guild has paused invites, preventing new users from joining."""

    INVITE_SPLASH = "INVITE_SPLASH"
    """Guild has access to set an invite splash background."""

    MEMBER_VERIFICATION_GATE_ENABLED = "MEMBER_VERIFICATION_GATE_ENABLED"
    """Guild has enabled Membership Screening."""

    MORE_STICKERS = "MORE_STICKERS"
    """Guild has increased custom sticker slots."""

    NEWS = "NEWS"
    """Guild has access to create announcement channels."""

    PARTNERED = "PARTNERED"
    """Guild is partnered."""

    PREVIEW_ENABLED = "PREVIEW_ENABLED"
    """Guild can be previewed before joining via Membership Screening or the directory."""

    RAID_ALERTS_DISABLED = "RAID_ALERTS_DISABLED"
    """Guild has disabled alerts for join raids in the configured safety alerts channel."""

    ROLE_ICONS = "ROLE_ICONS"
    """Guild is able to set role icons."""

    ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE = "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE"
    """Guild has role subscriptions that can be purchased."""

    ROLE_SUBSCRIPTIONS_ENABLED = "ROLE_SUBSCRIPTIONS_ENABLED"
    """Guild has enabled role subscriptions."""

    TICKETED_EVENTS_ENABLED = "TICKETED_EVENTS_ENABLED"
    """Guild has enabled ticketed events."""

    VANITY_URL = "VANITY_URL"
    """Guild has access to set a vanity URL."""

    VERIFIED = "VERIFIED"
    """Guild is verified."""

    VIP_REGIONS = "VIP_REGIONS"
    """Guild has access to set 384kbps bitrate in voice (previously VIP voice servers)."""

    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"
    """Guild has enabled the welcome screen."""

    class GuildFeatures(StrEnum):
        ANIMATED_BANNER = "ANIMATED_BANNER"
        """Guild has access to set an animated guild banner image."""

        ANIMATED_ICON = "ANIMATED_ICON"
        """Guild has access to set an animated guild icon."""

        APPLICATION_COMMAND_PERMISSIONS_V2 = "APPLICATION_COMMAND_PERMISSIONS_V2"
        """Guild is using the old permissions configuration behavior."""

        AUTO_MODERATION = "AUTO_MODERATION"
        """Guild has set up auto moderation rules."""

        BANNER = "BANNER"
        """Guild has access to set a guild banner image."""

        COMMUNITY = "COMMUNITY"
        """Guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates."""

        CREATOR_MONETIZABLE_PROVISIONAL = "CREATOR_MONETIZABLE_PROVISIONAL"
        """Guild has enabled monetization."""

        CREATOR_STORE_PAGE = "CREATOR_STORE_PAGE"
        """Guild has enabled the role subscription promo page."""

        DEVELOPER_SUPPORT_SERVER = "DEVELOPER_SUPPORT_SERVER"
        """Guild has been set as a support server on the App Directory."""

        DISCOVERABLE = "DISCOVERABLE"
        """Guild is able to be discovered in the directory."""

        FEATURABLE = "FEATURABLE"
        """Guild is able to be featured in the directory."""

        INVITES_DISABLED = "INVITES_DISABLED"
        """Guild has paused invites, preventing new users from joining."""

        INVITE_SPLASH = "INVITE_SPLASH"
        """Guild has access to set an invite splash background."""

        MEMBER_VERIFICATION_GATE_ENABLED = "MEMBER_VERIFICATION_GATE_ENABLED"
        """Guild has enabled Membership Screening."""

        MORE_STICKERS = "MORE_STICKERS"
        """Guild has increased custom sticker slots."""

        NEWS = "NEWS"
        """Guild has access to create announcement channels."""

        PARTNERED = "PARTNERED"
        """Guild is partnered."""

        PREVIEW_ENABLED = "PREVIEW_ENABLED"
        """Guild can be previewed before joining via Membership Screening or the directory."""

        RAID_ALERTS_DISABLED = "RAID_ALERTS_DISABLED"
        """Guild has disabled alerts for join raids in the configured safety alerts channel."""

        ROLE_ICONS = "ROLE_ICONS"
        """Guild is able to set role icons."""

        ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE = "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE"
        """Guild has role subscriptions that can be purchased."""

        ROLE_SUBSCRIPTIONS_ENABLED = "ROLE_SUBSCRIPTIONS_ENABLED"
        """Guild has enabled role subscriptions."""

        TICKETED_EVENTS_ENABLED = "TICKETED_EVENTS_ENABLED"
        """Guild has enabled ticketed events."""

        VANITY_URL = "VANITY_URL"
        """Guild has access to set a vanity URL."""

        VERIFIED = "VERIFIED"
        """Guild is verified."""

        VIP_REGIONS = "VIP_REGIONS"
        """Guild has access to set 384kbps bitrate in voice (previously VIP voice servers)."""

        WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"
        """Guild has enabled the welcome screen."""


class GuildMutableFeatures(StrEnum):
    COMMUNITY = "COMMUNITY"
    """Enables Community Features in the guild."""

    DISCOVERABLE = "DISCOVERABLE"
    """Enables discovery in the guild, making it publicly listed."""

    INVITES_DISABLED = "INVITES_DISABLED"
    """Pauses all invites/access to the server."""

    RAID_ALERTS_DISABLED = "RAID_ALERTS_DISABLED"
    """Disables alerts for join raids."""
