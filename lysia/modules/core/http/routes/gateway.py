__all__ = ("GatewayRoutes",)

from .base import RESTRoute


class GatewayRoutes:
    GET_GATEWAY = RESTRoute(method="GET", path="/gateway")
    """https://discord.com/developers/docs/topics/gateway#get-gateway"""

    GET_GATEWAY_BOT = RESTRoute(method="GET", path="/gateway/bot")
    """https://discord.com/developers/docs/topics/gateway#get-gateway-bot"""
