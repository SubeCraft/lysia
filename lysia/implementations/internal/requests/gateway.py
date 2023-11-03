__all__ = ("GatewayRequests",)

from typing import Any

from ....models.utils import Restable


class GatewayRequests(Restable):
    async def get_gateway(self) -> dict[str, str]:
        return await self.rest.request("GET", "/gateway")

    async def get_gateway_bot(self) -> dict[str, Any]:
        return await self.rest.request("GET", "/gateway/bot")
