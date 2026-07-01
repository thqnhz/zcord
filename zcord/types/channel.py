from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Any

from zcord.utils import MISSING

from .snowflake import Snowflake
from .user import User


class ChannelType(IntEnum):
    """
    Represent the type of a Discord channel.

    | Name | Value | Description |
    |------|-------|-------------|
    | `GUILD_TEXT` | `0` | A text channel in a guild. |
    | `DM` | `1` |   A direct message channel. |
    | `GUILD_VOICE` | `2` | A voice channel in a guild. |
    | `GROUP_DM` | `3` | A group direct message channel. |
    | `GUILD_CATEGORY` | `4` | A guild category. |
    | `GUILD_ANNOUNCEMENT` | `5` | A guild news channel. |
    | `ANNOUNCEMENT_THREAD` | `10` | A thread in a `GUILD_ANNOUNCEMENT` \
                                     channel. |
    | `PUBLIC_THREAD` | `11` | A thread in a `GUILD_TEXT` \
                               or `GUILD_FORUM` channel. |
    | `PRIVATE_THREAD` | `12` | A private thread in a `GUILD_TEXT` \
                                or `GUILD_FORUM` channel. |
    | `GUILD_STAGE_VOICE` | `13` | A stage channel in a guild. |
    | `GUILD_DIRECTORY` | `14` | The channel in a hub containing \
                                 the listed servers. |
    | `GUILD_FORUM` | `15` | A thread-only channel. |

    Notes:
        `GUILD_MEDIA (16)` is unstable so this library won't add it.
    """

    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_ANNOUNCEMENT = 5
    ANNOUNCEMENT_THREAD = 10
    PUBLIC_THREAD = 11
    PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13
    GUILD_DIRECTORY = 14
    GUILD_FORUM = 15
    # GUILD_MEDIA = 16  # unstable


@dataclass(frozen=True)
class Channel:
    """
    Represent a Discord server or DM channel.

    Attributes:
        id:
            The ID of the channel.
        type:
            The channel type.
        guild_id:
            The guild id the message belongs to.
        position:
            The sorting position of the channel.
        permission_overwrites:
            A list of explicit permission overwrites for members and roles.
        name:
            The name of the channel.

            **Notes**: Can only be in 1-100 characters range.
        topic:
            The channel's topic.

            **Notes**: For most `ChannelType`, it can be up to 1024
            characters long. Except `GUILD_FORUM` which can be up to
            4096 characters.
        nsfw:
            Whether the channel is age-restricted.
        last_message_id:
            The ID of the last message sent in this channel.
        bitrate:
            The bit per second of the voice channel.
        user_limit:
            The user limit of the voice channel.
        rate_limit_per_user:
            The channel slowmode in seconds. This ranges from 0-21600.
        recipients:
            The recipients of the DM.
        icon:
            The icon hash of the Group DM.
        owner_id:
            The ID of the Group DM or a thread.
        applicaiton_id:
            The app ID of the Group DM if it's created by a bot.
        managed:
            Whether the channel is managed.
        parent_id:
            For guild channels, it's the parent category ID.
            For threads, it's the text channel ID.
        last_pin_timestamp:
            When the last pinned message was pinned.
        rtc_region:
            ID of the region of the voice channel. Automatic when set to None.
        video_quality_mode:
            The camera video quality mode of the voice channel.
            `1` when not present.
        message_count:
            Number of messages in a thread.

            **Notes**: Can be inaccurate if the thread was created before
            July 1st, 2022.
        member_count:
            Approximate count of users in a thread.

            **Notes**: stop counting at 50.
        thread_metadata:
            Thread specific fields.
        member:
            Thread member object for the current user, if they have joined the
            thread.
        default_auto_archive_duration:
            Default duration for threads to be auto archived (in minutes).

            **Notes**: Can be set to 60, 1440, 4320, 10080.
        permissions:
            Computed permissions for the invoking user in the channel, including
            overwrites.
        flags:
            Channel flags combined as a bitfield.
        total_message_sent:
            Number of messages ever sent in a thread.

            **Notes**: Unlike `message_count`, the value won't
            decrease when a message is deleted.
        available_tags:
            The set of tags that can be used in a `GUILD_FORUM` channel.
        applied_tags:
            The IDs of the set of tags that have been applied to a thread in a
            `GUILD_FORUM` channel.
        default_reaction_emoji:
            The emoji to show in the add reaction button on a thread in a
            `GUILD_FORUM` channel.
        default_thread_rate_limit_per_user:
            The initial `rate_limit_per_user` to set on newly created threads
            in a channel.
        default_sort_order:
            The default sort order type used to order posts in `GUILD_FORUM`
            channel.
        default_forum_layout:
            The default forum layout view used to display posts in `GUILD_FORUM`
            channel.
    """

    id: Snowflake
    type: ChannelType
    guild_id: Snowflake | MISSING
    position: int | MISSING
    permission_overwrites: list | MISSING
    name: str | None | MISSING
    topic: str | None | MISSING
    nsfw: bool | MISSING
    last_message_id: Snowflake | None | MISSING
    bitrate: int | MISSING
    user_limit: int | MISSING
    rate_limit_per_user: int | MISSING
    recipients: list[User] | MISSING
    icon: str | None | MISSING
    owner_id: Snowflake | MISSING
    application_id: Snowflake | MISSING
    managed: bool | MISSING
    parent_id: Snowflake | None | MISSING
    last_pin_timestamp: datetime | None | MISSING
    rtc_region: str | None | MISSING
    video_quality_mode: int | MISSING
    message_count: int | MISSING
    member_count: int | MISSING
    thread_metadata: Any | MISSING
    member: Any | MISSING
    default_auto_archive_duration: int | MISSING
    permissions: str | MISSING
    flags: int | MISSING
    total_message_sent: int | MISSING
    available_tags: list | MISSING
    applied_tags: list[Snowflake] | MISSING
    default_reaction_emoji: Any | None | MISSING
    default_thread_rate_limit_per_user: int | MISSING
    default_sort_order: int | None | MISSING
    default_forum_layout: int | MISSING
