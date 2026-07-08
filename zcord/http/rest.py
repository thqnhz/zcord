from __future__ import annotations

from zcord.http import HTTPClient
from zcord.types import Channel, Guild, Message, Snowflake
from zcord.utils import MISSING


class REST:
    @staticmethod
    async def send_message(
        http: HTTPClient, channel_id: int | Snowflake | Channel, **kwargs
    ) -> Message:
        """
        Send a message to a channel.
        """
        resp = await http.request(
            "POST",
            f"/channels/{int(channel_id)}/messages",
            json={"content": kwargs["content"]},
        )
        return Message._from_payload(dict(resp))

    @staticmethod
    async def fetch_guild(
        http: HTTPClient,
        guild_id: int | Snowflake,
        *,
        with_counts: bool | MISSING = MISSING,
    ) -> Guild:
        """
        Fetch a guild with guild ID.
        """
        endpoint = f"/guilds/{guild_id}"
        # TODO: with_counts handling
        resp = await http.request("GET", endpoint)
        return Guild._from_payload(dict(resp))
