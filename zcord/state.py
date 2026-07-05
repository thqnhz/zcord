from __future__ import annotations

from zcord.http.client import HTTPClient
from zcord.http.rest import REST
from zcord.types import Channel, Message, Snowflake, User


class ConnectionState:
    _http: HTTPClient
    _channels: dict[int, Channel]
    _users: dict[int, User]

    def __init__(self, token: str):
        self._http = HTTPClient(token)

    async def send_message(
        self, channel_id: int | Snowflake, **kwargs
    ) -> Message:
        return await REST.send_message(self._http, channel_id, **kwargs)
