__all__ = (
    "LIBRARY_NAME",
    "LIBRARY_VERSION",
    "LIBRARY_GIT",
    "DISCORD_API_VERSION",
    "DISCORD_CDN_URL",
    "DISCORD_REST_URL"
)

from importlib.metadata import distribution

LIBRARY_NAME = "Lysia"
LIBRARY_VERSION = distribution(LIBRARY_NAME).metadata["version"]
LIBRARY_GIT = "https://github.com/SubeCraft/Lysia"

DISCORD_API_VERSION = 10
DISCORD_CDN_URL = "https://cdn.discordapp.com"
DISCORD_REST_URL = f"https://discord.com/api/v{DISCORD_API_VERSION}"
