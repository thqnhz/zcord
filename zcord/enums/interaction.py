from __future__ import annotations

from enum import IntEnum


class InteractionType(IntEnum):
    """
    | Name | Value |
    |------|-------|
    | `PING` | `1` |
    | `APPLICATION_COMMAND` | `2` |
    | `MESSAGE_COMPONENT` | `3` |
    | `APPLICATION_COMMAND_AUTOCOMPLETE` | `4` |
    | `MODAL_SUBMIT` | `5` |
    """

    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICAITON_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class InteractionContextType(IntEnum):
    """
    | Name | Value | Description |
    |------|-------|-------------|
    | `GUILD` | `0` | Interaction can be used within servers. |
    | `BOT_DM` | `1` | Interaction can be used within DMs with the app's bot. |
    | `PRIVATE_CHANNEL` | `2` | Interaction can be used within Group DMs and \
                                DMs other than the app's bot. |
    """

    GUILD = 0
    BOT_DM = 1
    PRIVATE_CHANNEL = 2
