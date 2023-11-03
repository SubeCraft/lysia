__all__ = ("InternalRestClient",)

from asyncio import sleep
from typing import TYPE_CHECKING, Any

from httpx import AsyncClient, codes

from ...constants import DISCORD_REST_URL, LIBRARY_GIT, LIBRARY_VERSION
from ...models.exceptions import Forbidden, HTTPException, NotFound, Unauthorized
from .requests.gateway import GatewayRequests

if TYPE_CHECKING:
    from ..client import Client


class InternalRestClient(GatewayRequests):
    def __init__(self, client: "Client") -> None:
        super().__init__(self)

        self.logger = client.logger.getChild("rest")

        self.http_client = AsyncClient(
            base_url=DISCORD_REST_URL,
            headers={
                "Authorization": f"Bot {client.token}",
                "User-Agent": f"DiscordBot ({LIBRARY_GIT}, {LIBRARY_VERSION})",
            })

    async def request(
            self,
            method: str,
            url: str,
            *,
            parameters: dict[str, Any] | None = None,
            payload: dict[str, Any] | None = None,
            headers: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Make a request at the Discord API."""

        while True:
            response = await self.http_client.request(
                method,
                url,
                json=payload,
                params=parameters,
                headers=headers
            )

            self.logger.debug(f"{response} {response.request}")

            match response.status_code:
                case codes.OK | codes.CREATED: return response.json()

                case codes.UNAUTHORIZED: raise Unauthorized(response, response.json())
                case codes.FORBIDDEN: raise Forbidden(response, response.json())
                case codes.NOT_FOUND: raise NotFound(response, response.json())

                case codes.TOO_MANY_REQUESTS:
                    retry_after: float = response.json()["retry_after"]

                    self.logger.info(f"You have been rate limited. Retrying after {round(retry_after)} seconds")
                    await sleep(round(retry_after))
                    self.logger.info("Retrying ...")

                    continue

                case codes.BAD_GATEWAY:
                    self.logger.info("Server error, Retrying in 10 seconds")
                    await sleep(10)
                    self.logger.info("Retrying ...")

                    continue

                case _:
                    raise HTTPException(response, response.json())

    async def close(self) -> None:
        await self.http_client.aclose()
