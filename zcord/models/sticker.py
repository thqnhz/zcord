from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord.enums import StickerFormatType, StickerType
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Sticker(ZcordModel):
    """
    Represent a Discord Sticker.

    Attributes:
        id:
            The ID of the sticker.
        pack_id:
            The ID of the pack the sticker is from.
        name:
            The name of the sticker.
        description:
            The description of the sticker.
        tags:
            The tags for autocomplete/suggestion for the sticker.
        type:
            The type of the sticker.
        format_type:
            The type of sticker format.
        available:
            Whether this guild sticker can be used.
        guild_id:
            The ID of the guild that owns this sticker.
        user:
            The user who uploaded this sticker.
        sort_value:
            The standard sticker sort order within its pack.
    """

    id: Snowflake
    name: str
    format_type: StickerFormatType
    tags: str | MISSING = MISSING
    type: StickerType | MISSING = MISSING
    pack_id: Snowflake | MISSING = MISSING
    description: str | None = None
    available: bool | MISSING = MISSING
    guild_id: Snowflake | MISSING = MISSING
    user: User | MISSING = MISSING
    sort_value: int | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": StickerType,
        "format_type": StickerFormatType,
        "pack_id": Snowflake,
        "guild_id": Snowflake,
        "user": User,
    }
