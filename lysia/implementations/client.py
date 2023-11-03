__all__ = ("Client",)

from asyncio import get_event_loop
from collections.abc import Callable
from typing import Any

from colorlog import INFO, ColoredFormatter, StreamHandler, getLogger

from ..models.api import IntentsFlag
from .internal.gateway import InternalGatewayClient
from .internal.rest import InternalRestClient


class Client:
    def __init__(
            self,
            token: str,
            *,
            intents: IntentsFlag = IntentsFlag.DEFAULT,
            logging: bool = False,
            logging_color: bool = True,
            logging_level: int = INFO
    ) -> None:
        self.token = token
        self.intents = intents

        self.logger = getLogger("lysia")

        if logging:
            handler = StreamHandler()
            handler.setFormatter(ColoredFormatter(
                "{asctime} {name} {log_color}{bold}{levelname}{reset} {message}",
                "%d/%m/%Y %H:%M:%S",
                style="{",
                no_color=not logging_color
            ))

            self.logger.setLevel(logging_level)
            self.logger.addHandler(handler)

        self.rest = InternalRestClient(self)
        self.gateway = InternalGatewayClient(self)

        self.listeners = {}

    def listen(self, event_name: str, callback: Callable[[Any], None]) -> None:
        self.listeners[event_name.upper()] = callback

    def start(self) -> None:
        loop = get_event_loop()

        try:
            loop.run_until_complete(self.gateway.start())
        except KeyboardInterrupt:
            loop.run_until_complete(self.close())

    async def close(self) -> None:
        await self.rest.close()
        await self.gateway.close()
