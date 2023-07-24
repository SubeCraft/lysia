from lysia.implementations.rest_client import RestClient
from lysia.api.http.routes.gateway import get_gateway_bot
from asyncio import run


async def main() -> None:
    client = RestClient("TOKEN")

    data = await client.discord_request(get_gateway_bot())

    print(data)

    await client.close()

run(main())
