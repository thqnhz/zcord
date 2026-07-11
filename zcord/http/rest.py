from __future__ import annotations

from zcord.http import HTTPClient
from zcord.models import Channel, Guild, Message, Snowflake
from zcord.utils import MISSING


def _build_query(**params) -> str:
    filtered = {}
    for k, v in params.items():
        if v is MISSING:
            continue
        if isinstance(v, bool):
            v = str(v).lower()
        filtered[k] = v
    if not filtered:
        return ""
    return "?" + "&".join(f"{k}={v}" for k, v in filtered.items())


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
        endpoint = f"/guilds/{guild_id}{_build_query(with_counts=with_counts)}"
        resp = await http.request("GET", endpoint)
        return Guild._from_payload(dict(resp))
