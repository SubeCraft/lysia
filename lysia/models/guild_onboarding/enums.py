__all__ = (
    "GuildOnboardingMode",
    "GuildOnboardingPromptTypes"
)

from enum import IntEnum


class GuildOnboardingMode(IntEnum):
    """Defines the criteria used to satisfy Onboarding constraints that are required for enabling."""

    ONBOARDING_DEFAULT = 0
    """Counts only Default Channels towards constraints."""

    ONBOARDING_ADVANCED = 1
    """Counts Default Channels and Questions towards constraints."""


class GuildOnboardingPromptTypes(IntEnum):
    MULTIPLE_CHOICE = 0
    DROPDOWN = 1
