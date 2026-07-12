from __future__ import annotations

from zcord.errors import MutuallyExclusiveParamsError
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


def _mutually_exclusive(**params) -> None:
    passed = [name for name, value in params.items() if value is not MISSING]
    if len(passed) > 1:
        raise MutuallyExclusiveParamsError(
            f"Expected only 1 parameters from {', '.join(params)}"
            f", got {len(passed)}: {', '.join(passed)}"
        )


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
    async def fetch_channel_messages(
        http: HTTPClient,
        channel_id: int | Snowflake,
        *,
        around: int | Snowflake | MISSING = MISSING,
        before: int | Snowflake | MISSING = MISSING,
        after: int | Snowflake | MISSING = MISSING,
        limit: int = 50,
    ) -> list[Message]:
        """
        Fetch the messages in a channel.

        Params:
            channel_id:
                The channel to fetch the messages.
            around:
                Get messages around this message ID.
            before:
                Get messages before this message ID.
            after:
                Get messages after this message ID.

        Notes:
            `around`, `before` and `after` are mutually exclusive.

        Returns:
            A list of [`Message`][] from newest to oldest.

        Raises
            HTTPError:
                The request failed.
            MutuallyExclusiveParamsError:
                Parameters which mutually exclusive to each other have been \
                passed.
            ValueError:
                An incorrect value of `limit` has been passed.
        """
        _mutually_exclusive(around=around, before=before, after=after)
        if limit <= 0 or limit > 100:
            raise ValueError(f"Expected 1-100 messages, got {limit}")
        endpoint = f"/channels/{channel_id}/messages"
        endpoint += _build_query(
            around=around, before=before, after=after, limit=limit
        )
        resp = await http.request("GET", endpoint)
        return [Message._from_payload(m) for m in resp]

    @staticmethod
    async def fetch_channel_message(
        http: HTTPClient,
        *,
        channel_id: int | Snowflake,
        message_id: int | Snowflake,
    ) -> Message:
        """
        Fetch a specific message in a channel.

        Params:
            channel_id:
                The channnel ID to get the message.
            message_id:
                The message ID.

        Returns:
            A Discord [`Message`][].

        Raise:
            HTTPError:
                The request failed.
        """
        endpoint = f"/channels/{channel_id}/messages/{message_id}"
        resp = await http.request("GET", endpoint)
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

        Returns:
            A Discord [`Guild`][].

        Raises:
            HTTPError:
                The request failed.
        """
        endpoint = f"/guilds/{guild_id}{_build_query(with_counts=with_counts)}"
        resp = await http.request("GET", endpoint)
        return Guild._from_payload(dict(resp))
