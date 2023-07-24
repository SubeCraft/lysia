from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Payload:
    ...


@dataclass
class IdentifyConnectionProperties(Payload):
    os: str
    browser: str
    device: str


@dataclass
class IdentifyPayload(Payload):
    token: str
    properties: IdentifyConnectionProperties
    compress: bool = False
    large_threshold: int = 50
    # TODO: Implement
    # TODO: Implement

    # TODO: Implement
    intents: int = 513


@dataclass
class HeartbeatPayload(Payload):
    d: int


@dataclass
class HelloPayload(Payload):
    heartbeat_interval: int

    # Only for have no error.
    _trace: dict = field(repr=False)


@dataclass
class ReadyPayload(Payload):
    v: Literal[10]
    session_id: str
    resume_gateway_url: str
    shard: tuple[int, int]

    # Only for have no error.
    user_settings: dict


@dataclass
class ResumePayload(Payload):
    pass
