from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Self

from zcord.missing import MISSING
from zcord.utils import from_payload


@dataclass(frozen=True, slots=True)
class ReactionCountDetails:
    """
    Contain a breakdown of normal and super reaction counts for the associated \
    emoji.

    Attributes:
        burst:
            Count of super reactions.
        normal:
            Count of normal reactions.
    """

    burst: int
    normal: int

    @classmethod
    def _from_payload(cls, payload: dict | MISSING) -> Self | MISSING:
        return from_payload(cls, payload)


@dataclass(frozen=True, slots=True)
class Reaction:
    """
    Represent a Discord reaction.

    Attributes:
        count:
            Total number of times this emoji has been used to react.
        count_details:
            Reaction count details.
        me:
            Whether the bot reacted using this emoji.
        me_burst:
            Whether the bot super-reacted using this emoji.
        emoji:
            Emoji info.
        burst_colors:
            A list of colors used for super reaction.
    """

    count: int
    count_details: ReactionCountDetails
    me: bool
    me_burst: bool
    emoji: Any
    burst_colors: list[int]

    @classmethod
    def _from_payload(cls, payload: dict | MISSING) -> Self | MISSING:
        return from_payload(
            cls, payload, count_details=ReactionCountDetails._from_payload
        )
