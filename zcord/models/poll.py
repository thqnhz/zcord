from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import ZcordModel


@dataclass(frozen=True, slots=True)
class PollMedia(ZcordModel):
    """
    Attributes:
        text:
            The text of the field.

            **Notes**: 300 characters max for question, and 55 max for answer.
        emoji:
            The emoji of the field.
    """

    text: str | MISSING = MISSING
    emoji: Any | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class PollAnswer(ZcordModel):
    """
    Attributes:
        answer_id:
            The ID of the answer.
        poll_media:
            The data of the answer.
    """

    answer_id: int
    poll_media: PollMedia

    _transforms: ClassVar[dict] = {
        "poll_media": PollMedia,
    }


@dataclass(frozen=True, slots=True)
class PollAnswerCount(ZcordModel):
    """
    Represents the number of votes for a single answer.

    Attributes:
        id:
            The ID of the answer.
        count:
            The number of votes for the answer.
        me_voted:
            Whether the bot voted for this answer.
    """

    id: int
    count: int
    me_voted: bool


@dataclass(frozen=True, slots=True)
class PollResults(ZcordModel):
    """
    Attributes:
        is_finalized:
            Whether the votes have been precisely counted.
        answer_counts:
            A list of number of votes for each answer.

    Notes:
        https://docs.discord.com/developers/resources/poll#poll-results-object
    """

    is_finalized: bool
    answer_counts: list[PollAnswerCount]

    _transforms: ClassVar[dict] = {
        "answer_counts": PollAnswerCount,
    }


@dataclass(frozen=True, slots=True)
class Poll(ZcordModel):
    """
    Represents a Discord poll.

    Attributes:
        question:
            The question of the poll.
        answers:
            A list of answers for the poll.
        expiry:
            The time when the poll ends.
        allow_multiselect:
            Whether a user can select multiple answers.
        layout_type:
            The layout type of the poll.
        results:
            The results of the poll.
    """

    question: PollMedia
    answers: list[PollAnswer]
    allow_multiselect: bool
    layout_type: int
    expiry: datetime | None = None
    results: PollResults | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "question": PollMedia,
        "expiry": datetime.fromisoformat,
        "answers": PollAnswer,
        "results": PollResults,
    }
