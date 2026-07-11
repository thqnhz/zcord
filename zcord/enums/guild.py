from __future__ import annotations

from enum import IntEnum


class VerificationLevel(IntEnum):
    """
    Guild verification level.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `NONE` | `0` | Unrestricted. |
    | `LOW` | `1` | Must have verified email on account. |
    | `MEDIUM` | `2` | Must be registered on Discord for longer than 5 \
    minutes. |
    | `HIGH` | `3` | Must be a member of the server for longer than 10 \
    minutes. |
    | `VERY_HIGH` | `4` | Must have a verified phone number. |
    """

    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class MessageNotificationLevel(IntEnum):
    """
    The default message notification level of the guild.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `ALL_MESSAGES` | `0` | Members will receive \
    notifications for all messages. |
    | `ONLY_MENTIONS` | `1` | Members will only receive notifications for \
    messages that mentions them. |
    """

    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class ExplicitContentFilterLevel(IntEnum):
    """
    The explicit content filtering level of the guild.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `DISABLED` | `0` | Media content will not be scanned. |
    | `MEMBERS_WITHOUT_ROLES` | `1` | Media content sent by members without \
    roles will be scanned. |
    | `ALL_MEMBERS` | `2` | Media content sent by all members will be scanned. |
    """

    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class MFALevel(IntEnum):
    """
    The MFA level of the guild.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `NONE` | `0` | No MFA requirement for moderation actions. |
    | `ELEVATED` | `1` | The guild has MFA requirement for moderation actions. |
    """

    NONE = 0
    ELEVATED = 1
