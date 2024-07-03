__all__ = ("UserRoutes",)

from .base import RESTRoute


class UserRoutes:
    GET_CURRENT_USER = RESTRoute(method="GET", path="/users/@me")
    """https://discord.com/developers/docs/resources/user#get-current-user"""

    GET_USER = RESTRoute(method="GET", path="/users/{user_id}")
    """https://discord.com/developers/docs/resources/user#get-user"""

    MODIFY_CURRENT_USER = RESTRoute(method="PATCH", path="/users/@me")
    """https://discord.com/developers/docs/resources/user#modify-current-user"""

    GET_CURRENT_USER_GUILDS = RESTRoute(method="GET", path="/users/@me/guilds")
    """https://discord.com/developers/docs/resources/user#get-current-user-guilds"""

    GET_CURRENT_USER_GUILD_MEMBER = RESTRoute(method="GET", path="/users/@me/guilds/{guild_id}/member")
    """https://discord.com/developers/docs/resources/user#get-current-user-guild-member"""

    LEAVE_GUILD = RESTRoute(method="DELETE", path="/users/@me/guilds/{guild_id}")
    """https://discord.com/developers/docs/resources/user#leave-guild"""

    CREATE_DM = RESTRoute(method="POST", path="/users/@me/channels")
    """https://discord.com/developers/docs/resources/user#create-dm"""

    CREATE_GROUP_DM = RESTRoute(method="POST", path="/users/@me/channels")
    """https://discord.com/developers/docs/resources/user#create-group-dm"""

    GET_CURRENT_USER_CONNECTIONS = RESTRoute(method="GET", path="/users/@me/connections")
    """https://discord.com/developers/docs/resources/user#get-current-user-connections"""

    GET_CURRENT_USER_APPLICATION_ROLE_CONNECTION = RESTRoute(method="GET", path="/users/@me/applications/{application_id}/role-connection")
    """https://discord.com/developers/docs/resources/user#get-current-user-application-role-connection"""

    UPDATE_CURRENT_USER_APPLICATION_ROLE_CONNECTION = RESTRoute(method="PUT", path="/users/@me/applications/{application_id}/role-connection")
    """https://discord.com/developers/docs/resources/user#update-current-user-application-role-connection"""
