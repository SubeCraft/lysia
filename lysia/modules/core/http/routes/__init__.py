from .base import *
from .gateway import *
from .guild import *
from .user import *

__all__ = ("RESTRoute", "Routes")


class Routes(
    GatewayRoutes,
    UserRoutes,
    GuildRoutes
): ...
