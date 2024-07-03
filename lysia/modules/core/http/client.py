__all__ = ("HTTPClient",)

from asyncio import sleep
from pprint import pformat
from typing import TYPE_CHECKING, Any

from httpx import AsyncClient, codes

from ....constants import DISCORD_CDN_URL, LYSIA_GIT, LYSIA_LOGGER, LYSIA_VERSION
from ..errors import Forbidden, HTTPError, NotFound, Unauthorized
from .types import TokenType

if TYPE_CHECKING:
    from .routes.base import RESTRoute


class HTTPClient:
    """
    An HTTP client for any request to the Discord API/CDN.
    """

    def __init__(self, token: str, token_type: TokenType = TokenType.BOT) -> None:
        self._client = AsyncClient(
            headers={
                "Authorization": f"{token_type} {token}",
                "User-Agent": f"DiscordBot ({LYSIA_GIT}, {LYSIA_VERSION})",
            }
        )

    @LYSIA_LOGGER.catch
    async def request(
            self,
            route: "RESTRoute",
            *,
            parameters: dict[str, Any] | None = None,
            payload: dict[str, Any] | None = None,
            headers: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Make a request at the Discord API."""

        while True:
            response = await self._client.request(
                route.method,
                route.url,
                json=payload,
                params=parameters,
                headers=headers,
            )

            LYSIA_LOGGER.debug(f"{route.method} {response.url} -> {response.status_code}")
            LYSIA_LOGGER.trace(f"\n{pformat(response.json())}")

            match response.status_code:
                case codes.OK | codes.CREATED: return response.json()
                case codes.NO_CONTENT: return {}

                case codes.UNAUTHORIZED:
                    raise Unauthorized("The token was invalid.", response)
                case codes.FORBIDDEN:
                    raise Forbidden("The token you passed did not have permission to the resource.", response)
                case codes.NOT_FOUND:
                    raise NotFound("The resource at the location specified doesn't exist.", response)
                case codes.TOO_MANY_REQUESTS:
                    retry_after: float = float(response.json()["retry_after"])

                    LYSIA_LOGGER.info(f"You have been rate limited. Retrying after {retry_after} seconds")
                    await sleep(retry_after)
                    LYSIA_LOGGER.info("Retrying ...")

                    continue

                case codes.BAD_GATEWAY:
                    LYSIA_LOGGER.info("Server error, Retrying in 10 seconds")
                    await sleep(10)
                    LYSIA_LOGGER.info("Retrying ...")

                    continue

                case _: raise HTTPError("HTTP error.", response)

    @LYSIA_LOGGER.catch
    async def request_cdn(self, url: str) -> bytes:
        """Make a request at the Discord CDN."""

        response = await self._client.get(DISCORD_CDN_URL + url)

        LYSIA_LOGGER.debug(f"GET {url} -> [{response.status_code}]")

        match response.status_code:
            case codes.OK: return response.read()

            case _: raise HTTPError("HTTP error.", response)

    async def close(self) -> None:
        """Close the HTTP client connection."""

        await self._client.aclose()
