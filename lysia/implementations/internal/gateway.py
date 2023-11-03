__all__ = ("InternalGatewayClient",)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client


class InternalGatewayClient:
    def __init__(self, client: "Client") -> None:
        self.client = client
        self.logger = self.client.logger.getChild("gateway")

    async def start(self) -> None:
        pass

    async def close(self) -> None:
        pass
