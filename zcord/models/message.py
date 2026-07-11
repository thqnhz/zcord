from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Self

from zcord.enums import MessageType
from zcord.missing import MISSING
from zcord.models.channel import Channel
from zcord.models.snowflake import Snowflake
from zcord.models.user import User
from zcord.utils import from_payload


@dataclass(frozen=True, slots=True)
class Message:
    """Represent a Discord message.

    Attributes:
        id:
            The ID of the message.
        channel_id:
            The ID of the channel the message was sent in.
        author:
            The author of this message.
        content:
            The message content.
        timestamp:
            The timestamp when this message was sent.
        edited_timestamp:
            The timestamp when this message was edited.
        tts:
            Whether this message is a text-to-speech message.
        mention_everyone:
            Whether this message mentions everyone.
        mentions:
            Users mentioned in this message.
        mention_roles:
            Roles mentioned in this message.
        mention_channels:
            Channels mentioned in this message.
        attachments:
            Attached files in this message.
        embeds:
            Embeded contents in this message.
        reactions:
            Reactions to this message.
        pinned:
            Whether this message is pinned.
        webhook_id:
            The webhook's ID if this message was sent via webhook.
        type:
            The type of the message.
        activity:
            Activity object sent via Rich presence related embeds.
        application:
            Partial application object sent via Rich presence related embeds.
        application_id:
            The application ID if this message was sent via an `Interaction`
            or an application-owned webhook.
        flags:
            The message flags combined as a bitfield.
        message_reference:
            The source of the crosspost, channel follow add, pin, or reply
            message.
        message_snapshots:
            The message associated with the `message_reference`. This is a
            minimal subset of fields in a `Message`.
        referenced_message:
            The message associated with the `message_reference`.
        interaction_metadata:
            Message interaction metadata.
        thread:
            The thread that was started from this message.
        components:
            Interactive components in this message.
        sticker_items:
            Stickers in this message.
        position:
            The approximated position of the message in a thread.
        role_subscription_data:
            Data of the subscription if this message is a
            `ROLE_SUBSCRIPTION_PURCHASE` message
        resolved:
            Data for users, members, channels, and roles referenced in
            this message.
        poll:
            A poll.
        call:
            The call associated with this message.
        shared_client_theme:
            The custom client-side theme shared in this message.
    """

    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: datetime
    tts: bool
    mention_everyone: bool
    mentions: list[User]
    mention_roles: list[Snowflake]
    attachments: list
    embeds: list
    pinned: bool
    type: MessageType
    edited_timestamp: datetime | None = None
    mention_channels: list | MISSING = MISSING
    reactions: list | MISSING = MISSING
    webhook_id: Snowflake | MISSING = MISSING
    activity: Any | MISSING = MISSING
    application: Any | MISSING = MISSING
    application_id: Snowflake | MISSING = MISSING
    flags: int | MISSING = MISSING
    message_reference: Any | MISSING = MISSING
    message_snapshots: Any | MISSING = MISSING
    referenced_message: Message | None | MISSING = MISSING
    interaction_metadata: Any | MISSING = MISSING
    thread: Channel | MISSING = MISSING
    components: list | MISSING = MISSING
    sticker_items: Any | MISSING = MISSING
    position: int | MISSING = MISSING
    role_subscription_data: Any | MISSING = MISSING
    resolved: Any | MISSING = MISSING
    poll: Any | MISSING = MISSING
    call: Any | MISSING = MISSING
    shared_client_theme: Any | MISSING = MISSING

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        return from_payload(
            cls,
            payload,
            id=Snowflake,
            channel_id=Snowflake,
            author=User._from_payload,
            timestamp=datetime.fromisoformat,
            edited_timestamp=datetime.fromisoformat,
            mentions=User._from_payload,
            mention_roles=Snowflake,
            mention_channels=Channel._from_payload,
            webhook_id=Snowflake,
            type=MessageType,
            application_id=Snowflake,
            thread=Channel._from_payload,
        )
