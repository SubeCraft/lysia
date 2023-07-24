from asyncio import all_tasks, create_task, sleep
from dataclasses import asdict
from typing import TYPE_CHECKING
from platform import platform

from ...constants import DISCORD_API_VERSION
from ...models.enums import OPCode
from ...models.events.api import (
    HeartbeatPayload,
    HelloPayload,
    IdentifyConnectionProperties,
    IdentifyPayload,
)
from ..http.routes.gateway import get_gateway_bot
from .packet import Packet

if TYPE_CHECKING:
    from aiohttp import ClientWebSocketResponse

    from lysia.implementations.client import Client


class Gateway:
    def __init__(self, client: "Client") -> None:
        self.client = client

        self.websocket: ClientWebSocketResponse | None = None

        self.sequence: int | None = None
        self.heartbeat_interval = 0

    async def websocket_connect(self, url: str, reconnect: bool = False) -> None:
        if reconnect: self.websocket: ClientWebSocketResponse = await self.client.rest.create_websocket(url)
        else: self.websocket: ClientWebSocketResponse = await self.client.rest.create_websocket(url)

        while True:
            packet = await self.ws_receive()
            print(packet)
            await self.dispatch_opcode(packet)

    async def ws_send(self, packet: Packet) -> None:
        await self.websocket.send_json(asdict(packet))

    async def ws_receive(self) -> Packet:
        data = await self.websocket.receive_json()
        return Packet(**data)

    async def dispatch_opcode(self, packet: Packet) -> None:
        print(packet)
        match packet.op:
            case OPCode.DISPATCH: await self.dispatch_event(packet)
            case OPCode.HEARTBEAT: await self.heartbeat()
            case OPCode.RECONNECT: pass
            case OPCode.INVALIDATE_SESSION: pass
            case OPCode.HELLO:
                self.heartbeat_interval = HelloPayload(**packet.d).heartbeat_interval
                await self.identify()
            case OPCode.HEARTBEAT_ACK: pass

    async def dispatch_event(self, packet: Packet) -> None:
        self.sequence = packet.s
        print(packet)
        match packet.t:
            case "READY": pass

    async def identify(self) -> None:
        await self.ws_send(
            Packet(
                OPCode.IDENTIFY,
                IdentifyPayload(self.client.token, IdentifyConnectionProperties(platform(), "lysia", "lysia"))
            )
        )

        create_task(self.heartbeat_loop())

    async def heartbeat(self) -> None:
        await self.ws_send(Packet(OPCode.HEARTBEAT, HeartbeatPayload(self.sequence)))

    async def heartbeat_loop(self) -> None:
        while True:
            await self.heartbeat()
            await sleep(self.heartbeat_interval / 1000)

    async def start(self) -> None:
        websocket_url = await self.client.rest.discord_request(get_gateway_bot())
        await self.websocket_connect(websocket_url["url"] + f"/?v={DISCORD_API_VERSION}&encoding=json")

    async def close(self) -> None:
        await self.websocket.close()

