from dataclasses import dataclass
from typing import Literal

from ...models.enums import OPCode
from ...models.events.api import Payload


@dataclass
class Packet:
    op: Literal[
        OPCode.DISPATCH,
        OPCode.HEARTBEAT,
        OPCode.IDENTIFY,
        OPCode.PRESENCE_UPDATE,
        OPCode.VOICE_STATE_UPDATE,
        OPCode.RESUME,
        OPCode.RECONNECT,
        OPCode.REQUEST_GUILD_MEMBERS,
        OPCode.INVALIDATE_SESSION,
        OPCode.HELLO,
        OPCode.HEARTBEAT_ACK,
    ]
    d: Payload
    s: int | None = None
    t: str | None = None
