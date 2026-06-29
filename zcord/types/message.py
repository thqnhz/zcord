from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Any, Self

from zcord.utils import _MISSING

from .snowflake import Snowflake
from .user import User


class _MessageType(IntEnum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTO_MODERATION_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
    GUILD_INCIDENT_ALERT_MODE_ENABLED = 36
    GUILD_INCIDENT_ALERT_MODE_DISABLED = 37
    GUILD_INCIDENT_REPORT_RAID = 38
    GUILD_INCIDENT_REPORT_FALSE_ALARM = 39
    PURCHASE_NOTIFICATION = 44
    POLL_RESULT = 46


@dataclass(frozen=True)
class Message:
    """Represent a Discord Message

    Attributes:
        id: The ID of the message.
        channel_id: The ID of the channel the message was sent in.
        author: The author of this message.
        content: The message content.
        timestamp: The timestamp when this message was sent.
        edited_timestamp: The timestamp when this message was edited.
        tts: Whether this message is a text-to-speech message.
        mention_everyone: Whether this message mentions everyone.
        mentions: Users mentioned in this message.
        mention_roles: Roles mentioned in this message.
        mention_channels: Channels mentioned in this message.
        attachments: Attached files in this message.
        embeds: Embeded contents in this message.
        reactions: Reactions to this message.
        pinned: Whether this message is pinned.
        webhook_id: The webhook's ID if this message was sent via webhook.
        type: The type of the message.
        activity: Activity object sent via Rich presence related embeds.
        application: Partial application object sent via
                     Rich presence related embeds.
        application_id: The application ID if this message was sent
                        via an `Interaction` or an application-owned
                        webhook.
        flags: The message flags combined as a bitfield.
        message_reference: The source of the crosspost, channel follow add,
                           pin, or reply message.
        message_snapshots: The message associated with the `message_reference`.
                           This is a minimal subset of fields in a `Message`.
        referenced_message: The message associated with the `message_reference`.
        interaction_metadata: Message interaction metadata.
        thread: The thread that was started from this message.
        components: Interactive components in this message.
        sticker_items: Stickers in this message.
        position: The approximated position of the message in a thread.
        role_subscription_data: Data of the subscription if this message is a
                                `ROLE_SUBSCRIPTION_PURCHASE` message
        resolved: Data for users, members, channels, and roles referenced in
                  this message.
        poll: A poll.
        call: The call associated with this message.
        shared_client_theme: The custom client-side theme shared
                             in this message.
    """

    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: datetime
    edited_timestamp: datetime | None
    tts: bool
    mention_everyone: bool
    mentions: list[User]
    mention_roles: list[Snowflake]
    mention_channels: list | _MISSING
    attachments: list
    embeds: list
    reactions: list | _MISSING
    pinned: bool
    webhook_id: Snowflake | _MISSING
    type: _MessageType
    activity: Any | _MISSING
    application: Any | _MISSING
    application_id: Snowflake | _MISSING
    flags: int | _MISSING
    message_reference: Any | _MISSING
    message_snapshots: Any | _MISSING
    referenced_message: Message | _MISSING | None
    interaction_metadata: Any | _MISSING
    thread: Any | _MISSING  # NOTE: Channel
    components: list
    sticker_items: Any | _MISSING
    position: int | _MISSING
    role_subscription_data: Any | _MISSING
    resolved: Any | _MISSING
    poll: Any | _MISSING
    call: Any | _MISSING
    shared_client_theme: Any | _MISSING

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        id = Snowflake(payload.get("id", -1))
        channel_id = Snowflake(payload.get("channel_id", -1))
        author = User._from_payload(payload.get("author", {}))
        content: str = payload.get("content", "")
        timestamp = datetime.fromisoformat(str(payload.get("timestamp")))
        e_t = payload.get("edited_timestamp")
        if e_t is not None:
            edited_timestamp = datetime.fromisoformat(str(e_t))
        else:
            edited_timestamp = None
        tts: bool = payload.get("tts", False)
        mention_everyone: bool = payload.get("mention_everyone", False)
        mentions: list = payload.get("mentions", [])
        if len(mentions) != 0:
            mentions: list[User] = [User._from_payload(u) for u in mentions]
        mention_roles: list = payload.get("mention_roles", [])
        if len(mention_roles) != 0:
            mention_roles: list[Snowflake] = [
                Snowflake(r) for r in mention_roles
            ]
        mention_channels: list = payload.get("mention_channels", _MISSING)
        attachments: list = payload.get("attachments", [])
        embeds: list = payload.get("embeds", [])
        reactions: list = payload.get("reactions", _MISSING)
        pinned: bool = payload.get("pinned", False)
        webhook_id = payload.get("webhook_id", _MISSING)
        if webhook_id is not _MISSING:
            webhook_id = Snowflake(webhook_id)
        type = _MessageType(payload.get("type", 0))
        activity = payload.get("activity", _MISSING)
        application = payload.get("application", _MISSING)
        application_id: int = payload.get("application_id", _MISSING)
        if application_id is not _MISSING:
            application_id = Snowflake(application_id)
        flags: int = payload.get("flags", _MISSING)
        message_reference = payload.get("message_reference", _MISSING)
        message_snapshots = payload.get("message_snapshots", _MISSING)
        referenced_message = payload.get("referenced_message", _MISSING)
        interaction_metadata = payload.get("interaction_metadata", _MISSING)
        thread = payload.get("thread", _MISSING)
        components: list = payload.get("components", _MISSING)
        sticker_items: list = payload.get("sticker_items", _MISSING)
        position: int = payload.get("position", _MISSING)
        role_subscription_data = payload.get("role_subscription_data", _MISSING)
        resolved = payload.get("resolved", _MISSING)
        poll = payload.get("poll", _MISSING)
        call = payload.get("call", _MISSING)
        shared_client_theme = payload.get("shared_client_theme", _MISSING)

        return cls(
            id=id,
            channel_id=channel_id,
            author=author,
            content=content,
            timestamp=timestamp,
            edited_timestamp=edited_timestamp,
            tts=tts,
            mention_everyone=mention_everyone,
            mentions=mentions,
            mention_roles=mention_roles,
            mention_channels=mention_channels,
            attachments=attachments,
            embeds=embeds,
            reactions=reactions,
            pinned=pinned,
            webhook_id=webhook_id,
            type=type,
            activity=activity,
            application=application,
            application_id=application_id,
            flags=flags,
            message_reference=message_reference,
            message_snapshots=message_snapshots,
            referenced_message=referenced_message,
            interaction_metadata=interaction_metadata,
            thread=thread,
            components=components,
            sticker_items=sticker_items,
            position=position,
            role_subscription_data=role_subscription_data,
            poll=poll,
            resolved=resolved,
            call=call,
            shared_client_theme=shared_client_theme,
        )
