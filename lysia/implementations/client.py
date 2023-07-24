from asyncio import get_event_loop
from collections.abc import Callable

from ..api.gateway.gateway import Gateway
from .rest_client import RestClient


class Client:
    def __init__(self, token: str) -> None:
        self.token = token

        self.rest = RestClient(self.token)
        self.gateway = Gateway(self)

        self.listeners = {}

    def listen(self, event_name: str, callback: Callable[[], None]) -> None:
        self.listeners[event_name.upper()] = callback

    def start(self) -> None:
        loop = get_event_loop()

        try:
            loop.run_until_complete(self.gateway.start())
        except KeyboardInterrupt:
            loop.run_until_complete(self.close())

    async def close(self):
        await self.rest.close()
        await self.gateway.close()
