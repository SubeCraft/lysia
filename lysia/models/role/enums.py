__all__ = (
    "RoleFlags",
)

from enum import IntFlag


class RoleFlags(IntFlag):
    IN_PROMPT = 1 << 0
    """Role can be selected by members in an onboarding prompt."""
