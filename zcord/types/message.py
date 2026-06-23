from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Any, Self

from .snowflake import Snowflake


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


@dataclass
class Message:
    """Represent a Discord Message"""

    id: Snowflake
    channel_id: Snowflake
    author: Any  # NOTE: User object
    content: str
    timestamp: datetime
    edited_timestamp: datetime | None
    tts: bool
    mention_everyone: bool
    mentions: list
    mention_roles: list
    mention_channels: list | None
    attachments: list
    embeds: list
    reactions: list | None
    nonce: int | str | None  # Never seen this one before
    pinned: bool
    webhook_id: Snowflake | None
    type: _MessageType
    activity: Any | None
    application: Any | None
    application_id: Snowflake | None
    flags: int | None
    message_reference: Any | None
    message_snapshots: Any | None
    referenced_message: Message | None
    interaction_metadata: Any | None
    interaction: Any | None
    thread: Any | None  # NOTE: Channel
    components: list
    sticker_items: Any | None
    stickers: list
    position: int | None
    role_subscription_data: Any | None
    resolved: Any | None
    poll: Any | None
    call: Any | None
    shared_client_theme: Any | None

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        id = Snowflake(payload.get("id", -1))
        channel_id = Snowflake(payload.get("id", -1))
        author = payload.get("author")
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
        mention_roles: list = payload.get("mention_roles", [])
        mention_channels: list = payload.get("mention_channels", [])
        attachments: list = payload.get("attachments", [])
        embeds: list = payload.get("embeds", [])
        reactions: list = payload.get("reactions", [])
        nonce = payload.get("nonce")
        pinned: bool = payload.get("pinned", False)
        webhook_id = Snowflake(payload.get("webhook_id", -1))
        type: int = _MessageType(payload.get("type", 0))
        activity = payload.get("activity")
        application = payload.get("application")
        application_id = Snowflake(payload.get("application_id", -1))
        flags: int | None = payload.get("flags")
        message_reference = payload.get("message_reference")
        message_snapshots = payload.get("message_snapshots")
        referenced_message = (
            Message._from_payload(payload.get("referenced_message", {}))
            if payload.get("referenced_message")
            else None
        )
        interaction_metadata = payload.get("interaction_metadata")
        interaction = payload.get("interaction")
        thread = payload.get("thread")
        components = payload.get("components", [])
        sticker_items = payload.get("sticker_items")
        stickers = payload.get("stickers", [])
        position = payload.get("position")
        role_subscription_data = payload.get("role_subscription_data")
        resolved = payload.get("resolved")
        poll = payload.get("poll")
        call = payload.get("call")
        shared_client_theme = payload.get("shared_client_theme")

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
            nonce=nonce,
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
            interaction=interaction,
            thread=thread,
            components=components,
            sticker_items=sticker_items,
            stickers=stickers,
            position=position,
            role_subscription_data=role_subscription_data,
            poll=poll,
            resolved=resolved,
            call=call,
            shared_client_theme=shared_client_theme,
        )
