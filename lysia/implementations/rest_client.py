from typing import TYPE_CHECKING, Any

from aiohttp import ClientSession

from ..constants import LIBRARY_VERSION

if TYPE_CHECKING:
    from lysia.api.http.route import Route


class RestClient:
    def __init__(self, token: str) -> None:
        self.client = ClientSession()

        self.DEFAULT_HEADER = {
            "Authorization": f"Bot {token}",
            "User-Agent": f"DiscordBot (https://github.com/SubeCraft/Lysia, {LIBRARY_VERSION})",
        }

    async def discord_request(self, route: "Route") -> Any:
        async with self.client.request(
            route.method, route.url, headers=self.DEFAULT_HEADER,
        ) as response:
            return await response.json()


    async def create_websocket(self, url: str):
        return await self.client.ws_connect(url, timeout=60.0, autoclose=False)

    async def close(self) -> None:
        await self.client.close()
