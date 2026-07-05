from __future__ import annotations

from zcord.http import HTTPClient
from zcord.types import Channel, Message, Snowflake


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
