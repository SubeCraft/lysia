__all__ = ("GuildRoutes",)

from .base import RESTRoute


class GuildRoutes:
    CREATE_GUILD = RESTRoute(method="POST", path="/guilds")
    """https://discord.com/developers/docs/resources/guild#create-guild"""

    GET_GUILD = RESTRoute(method="GET", path="/guilds/{guild_id}")
    """https://discord.com/developers/docs/resources/guild#get-guild"""

    GET_GUILD_PREVIEW = RESTRoute(method="GET", path="/guilds/{guild_id}/preview")
    """https://discord.com/developers/docs/resources/guild#get-guild-preview"""

    MODIFY_GUILD = RESTRoute(method="PATCH", path="/guilds/{guild_id}")
    """https://discord.com/developers/docs/resources/guild#modify-guild"""

    DELETE_GUILD = RESTRoute(method="DELETE", path="/guilds/{guild_id}")
    """https://discord.com/developers/docs/resources/guild#delete-guild"""

    GET_GUILD_CHANNELS = RESTRoute(method="GET", path="/guilds/{guild_id}/channels")
    """https://discord.com/developers/docs/resources/guild#get-guild-channels"""

    CREATE_GUILD_CHANNEL = RESTRoute(method="POST", path="/guilds/{guild_id}/channels")
    """https://discord.com/developers/docs/resources/guild#get-guild-channels"""

    MODIFY_GUILD_CHANNEL_POSITION = RESTRoute(method="PATCH", path="/guilds/{guild_id}/channels")
    """https://discord.com/developers/docs/resources/guild#modify-guild-channel-positions"""

    LIST_ACTIVATE_GUILD_THREADS = RESTRoute(method="GET", path="/guilds/{guild_id}/threads/active")
    """https://discord.com/developers/docs/resources/guild#list-active-guild-threads"""

    GET_GUILD_MEMBER = RESTRoute(method="GET", path="/guilds/{guild_id}/members/{user_id}")
    """https://discord.com/developers/docs/resources/guild#get-guild-member"""

    LIST_GUILD_MEMBER = RESTRoute(method="GET", path="/guilds/{guild_id}/members")
    """https://discord.com/developers/docs/resources/guild#list-guild-members"""

    SEARCH_GUILD_MEMBERS = RESTRoute(method="GET", path="/guilds/{guild_id}/members/search")
    """https://discord.com/developers/docs/resources/guild#search-guild-members"""

    ADD_GUILD_MEMBER = RESTRoute(method="PUT", path="/guilds/{guild_id}/members/{user_id}")
    """https://discord.com/developers/docs/resources/guild#add-guild-member"""

    MODIFY_GUILD_MEMBER = RESTRoute(method="PATCH", path="/guilds/{guild_id}/members/{user_id}")
    """https://discord.com/developers/docs/resources/guild#modify-guild-member"""

    MODIFY_CURRENT_MEMBER = RESTRoute(method="PATCH", path="/guilds/{guild_id}/members/@me")
    """https://discord.com/developers/docs/resources/guild#modify-current-member"""

    ADD_GUILD_MEMBER_ROLE = RESTRoute(method="PUT", path="/guilds/{guild_id}/members/{user_id}/roles/{role_id}")
    """https://discord.com/developers/docs/resources/guild#add-guild-member-role"""

    REMOVE_GUILD_MEMBER_ROLE = RESTRoute(method="DELETE", path="/guilds/{guild_id}/members/{user_id}/roles/{role_id}")
    """https://discord.com/developers/docs/resources/guild#remove-guild-member-role"""

    REMOVE_GUILD_MEMBER = RESTRoute(method="DELETE", path="/guilds/{guild_id}/members/{user_id}")
    """https://discord.com/developers/docs/resources/guild#remove-guild-member"""

    GET_GUILD_BANS = RESTRoute(method="GET", path="/guilds/{guild_id}/bans")
    """https://discord.com/developers/docs/resources/guild#get-guild-bans"""

    GET_GUILD_BAN = RESTRoute(method="GET", path="/guilds/{guild_id}/bans/{user_id}")
    """https://discord.com/developers/docs/resources/guild#get-guild-ban"""

    CREATE_GUILD_BAN = RESTRoute(method="PUT", path="/guilds/{guild_id}/bans/{user_id}")
    """https://discord.com/developers/docs/resources/guild#create-guild-ban"""

    REMOVE_GUILD_BAN = RESTRoute(method="DELETE", path="/guilds/{guild_id}/bans/{user_id}")
    """https://discord.com/developers/docs/resources/guild#remove-guild-ban"""

    BULK_GUILD_BAN = RESTRoute(method="POST", path="/guilds/{guild_id}/bulk-ban")
    """https://discord.com/developers/docs/resources/guild#bulk-guild-ban"""

    GET_GUILD_ROLES = RESTRoute(method="GET", path="/guilds/{guild_id}/roles")
    """https://discord.com/developers/docs/resources/guild#get-guild-roles"""

    CREATE_GUILD_ROLE = RESTRoute(method="GET", path="/guilds/{guild_id}/roles")
    """https://discord.com/developers/docs/resources/guild#create-guild-role"""

    MODIFY_GUILD_ROLE_POSITIONS = RESTRoute(method="PATCH", path="/guilds/{guild_id}/roles")
    """https://discord.com/developers/docs/resources/guild#modify-guild-role-positions"""

    MODIFY_GUILD_ROLE = RESTRoute(method="PATCH", path="/guilds/{guild_id}/roles/{role_id}")
    """https://discord.com/developers/docs/resources/guild#modify-guild-role"""

    MODIFY_GUILD_MFA_LEVEL = RESTRoute(method="POST", path="/guilds/{guild_id}/mfa")
    """https://discord.com/developers/docs/resources/guild#modify-guild-mfa-level"""

    DELETE_GUILD_ROLE = RESTRoute(method="DELETE", path="/guilds/{guild_id}/roles/{role_id}")
    """https://discord.com/developers/docs/resources/guild#delete-guild-role"""

    GET_GUILD_PRUNE_COUNT = RESTRoute(method="GET", path="/guilds/{guild_id}/prune")
    """https://discord.com/developers/docs/resources/guild#get-guild-prune-count"""

    BEGIN_GUILD_PRUNE = RESTRoute(method="POST", path="/guilds/{guild_id}/prune")
    """https://discord.com/developers/docs/resources/guild#begin-guild-prune"""

    GET_GUILD_VOICE_REGIONS = RESTRoute(method="GET", path="/guilds/{guild_id}/regions")
    """https://discord.com/developers/docs/resources/guild#get-guild-voice-regions"""

    GET_GUILD_INVITE = RESTRoute(method="GET", path="/guilds/{guild_id}/regions")
    """https://discord.com/developers/docs/resources/guild#get-guild-invites"""

    GET_GUILD_INTEGRATION = RESTRoute(method="GET", path="/guilds/{guild_id}/integrations")
    """https://discord.com/developers/docs/resources/guild#get-guild-integrations"""

    DELETE_GUILD_INTERGRATION = RESTRoute(method="DELETE", path="/guilds/{guild_id}/integrations/{integration_id}")
    """https://discord.com/developers/docs/resources/guild#delete-guild-integration"""

    GET_GUILD_WIDGET_SETTINGS = RESTRoute(method="GET", path="/guilds/{guild_id}/widget")
    """https://discord.com/developers/docs/resources/guild#get-guild-widget-settings"""

    MODIFY_GUILD_WIDGET = RESTRoute(method="PATCH", path="/guilds/{guild_id}/widget")
    """https://discord.com/developers/docs/resources/guild#modify-guild-widget"""

    GET_GUILD_WIDGET = RESTRoute(method="GET", path="/guilds/{guild_id}/widget.json")
    """https://discord.com/developers/docs/resources/guild#get-guild-widget"""

    GET_GUILD_VANITY_URL = RESTRoute(method="GET", path="/guilds/{guild_id}/vanity-url")
    """https://discord.com/developers/docs/resources/guild#get-guild-vanity-url"""

    GET_GUILD_WIDGET_IMAGE = RESTRoute(method="GET", path="/guilds/{guild_id}/widget.png")
    """https://discord.com/developers/docs/resources/guild#get-guild-widget-image"""

    GET_GUILD_WELCOME_SCREEN = RESTRoute(method="GET", path="/guilds/{guild_id}/welcome-screen")
    """https://discord.com/developers/docs/resources/guild#get-guild-welcome-screen"""

    MODIFY_GUILD_WELCOME_SCREEN = RESTRoute(method="PATCH", path="/guilds/{guild_id}/welcome-screen")
    """https://discord.com/developers/docs/resources/guild#modify-guild-welcome-screen"""

    GET_GUILD_ONBOARDING = RESTRoute(method="GET", path="/guilds/{guild_id}/onboarding")
    """https://discord.com/developers/docs/resources/guild#get-guild-onboarding"""

    MODIFY_GUILD_ONBOARDING = RESTRoute(method="PUT", path="/guilds/{guild_id}/onboarding")
    """https://discord.com/developers/docs/resources/guild#modify-guild-onboarding"""

    MODIFY_CURRENT_USER_VOICE_STATE = RESTRoute(method="PATCH", path="/guilds/{guild_id}/voice-states/@me")
    """https://discord.com/developers/docs/resources/guild#modify-current-user-voice-state"""

    MODIFY_USER_VOICE_STATE = RESTRoute(method="PATCH", path="/guilds/{guild_id}/voice-states/{user_id}")
    """https://discord.com/developers/docs/resources/guild#modify-user-voice-state"""
