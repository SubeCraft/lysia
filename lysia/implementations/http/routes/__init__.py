from .base import *
from .gateway import *
from .user import *
from .guild import *


__all__ = ("RESTRoute", "Routes")


class Routes(
    GatewayRoutes,
    UserRoutes,
    GuildRoutes
): ...
