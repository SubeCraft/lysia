from asyncio import run
from logging import DEBUG

from lysia.implementations.client import Client


async def main() -> None:
    client = Client(
        "TOKEN",
        logging=True,
        logging_level=DEBUG
    )

    print(await client.rest.get_gateway())

    await client.rest.close()

run(main())
