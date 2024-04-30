__all__ = (
    "LYSIA_VERSION",
    "LYSIA_AUTHORS",
    "LYSIA_GIT",

    "LYSIA_LOGGER",

    "DISCORD_API_VERSION",
    "DISCORD_CDN_URL",
    "DISCORD_REST_URL"
)
from importlib.metadata import metadata

from loguru import logger

metadata = metadata("lysia").json

LYSIA_VERSION = metadata["version"]
LYSIA_AUTHORS = metadata["author"]
LYSIA_GIT = metadata["home_page"]

LYSIA_LOGGER = logger.bind(name="lysia")

DISCORD_API_VERSION = 10
DISCORD_CDN_URL = "https://cdn.discordapp.com"
DISCORD_REST_URL = f"https://discord.com/api/v{DISCORD_API_VERSION}"
