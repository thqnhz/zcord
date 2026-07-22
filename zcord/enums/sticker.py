from __future__ import annotations

from enum import IntEnum


class StickerType(IntEnum):
    """
    | Type | Value | Description |
    |------|-------|-------------|
    | `STANDARD` | `1` | An official sticker in a pack. |
    | `GUILD` | `2` | A [`Sticker`][zcord.Sticker] uploaded to a guild. |
    """

    STANDARD = 1
    GUILD = 2


class StickerFormatType(IntEnum):
    """
    | Type | Value |
    |------|-------|
    | `PNG` | `1` |
    | `APNG` | `2` |
    | `LOTTIE` | `3` |
    | `GIF` | `4` |
    """

    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4
