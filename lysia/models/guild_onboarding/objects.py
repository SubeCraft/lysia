__all__ = (
    "GuildOnboarding",
    "GuildOnboardingPrompt",
    "GuildOnboardingPromptOption"
)

from pydantic import Field

from ..base import DiscordRessource
from ..common.types import Snowflake
from .enums import GuildOnboardingMode, GuildOnboardingPromptTypes


class GuildOnboardingPromptOption(DiscordRessource):
    id: Snowflake = Field(default="")
    """ID of the prompt option."""

    channel_ids: list[Snowflake] = Field(default="")
    """IDs for channels a member is added to when the option is selected."""

    role_ids: list[Snowflake] = Field(default="")
    """IDs for roles assigned to a member when the option is selected."""

    # emoji: Emoji | None = Field(default=None)
    """Emoji of the option."""

    emoji_id: Snowflake | None = Field(default=None)
    """Emoji ID of the option."""

    emoji_name: str | None = Field(default=None)
    """Emoji name of the option."""

    emoji_animated: bool | None = Field(default=None)
    """Whether the emoji is animated."""

    title: str = Field(default="")
    """Title of the option."""

    description: str | None = Field(default=None)
    """Description of the option."""


class GuildOnboardingPrompt(DiscordRessource):
    id: Snowflake = Field(default="")
    """ID of the prompt."""

    type: GuildOnboardingPromptTypes = Field(default=GuildOnboardingPromptTypes.MULTIPLE_CHOICE)
    """Type of prompt."""

    options: list[GuildOnboardingPromptOption] = Field(default_factory=list)
    """Options available within the prompt."""

    title: str = Field(default="")
    """Title of the prompt."""

    single_select: bool = Field(default=False)
    """Indicates whether users are limited to selecting one option for the prompt."""

    required: bool = Field(default=False)
    """Indicates whether the prompt is required before a user completes the onboarding flow."""

    in_onboarding: bool = Field(default=False)
    """
    Indicates whether the prompt is present in the onboarding flow.
    If false, the prompt will only appear in the Channels & Roles tab
    """


class GuildOnboarding(DiscordRessource):
    guild_id: Snowflake = Field(default="")
    """ID of the guild this onboarding is part of."""

    prompts: list[GuildOnboardingPrompt] = Field(default_factory=list)
    """Prompts shown during onboarding and in customize community."""

    default_channel_ids: list[Snowflake] = Field(default_factory=list)
    """Channel IDs that members get opted into automatically."""

    enabled: bool = Field(default=False)
    """Whether onboarding is enabled in the guild."""

    mode: GuildOnboardingMode = Field(default=GuildOnboardingMode.ONBOARDING_DEFAULT)
    """Current mode of onboarding."""
