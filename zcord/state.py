from __future__ import annotations

from zcord.http.client import HTTPClient
from zcord.http.rest import REST
from zcord.missing import MISSING
from zcord.models import Channel, Guild, Message, Snowflake, User


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

    async def fetch_guild(
        self,
        guild_id: int | Snowflake,
        *,
        with_counts: bool | MISSING = MISSING,
    ) -> Guild:
        return await REST.fetch_guild(
            self._http, guild_id, with_counts=with_counts
        )
