"""Zcord - Functional programming discord API wrapper"""

from importlib.metadata import version

from .bot import Bot
from .enums import (
    ChannelType,
    ExplicitContentFilterLevel,
    MessageNotificationLevel,
    MessageType,
    MFALevel,
    VerificationLevel,
)
from .missing import MISSING
from .models import (
    Channel,
    Embed,
    EmbedAuthor,
    EmbedField,
    EmbedFooter,
    EmbedImage,
    EmbedProvider,
    EmbedVideo,
    Guild,
    Message,
    Reaction,
    ReactionCountDetails,
    Role,
    RoleColors,
    RoleTags,
    Snowflake,
    User,
)

__version__ = version("zcord")

__all__ = [
    "MISSING",
    "Bot",
    "Channel",
    "ChannelType",
    "Embed",
    "EmbedAuthor",
    "EmbedField",
    "EmbedFooter",
    "EmbedImage",
    "EmbedProvider",
    "EmbedVideo",
    "ExplicitContentFilterLevel",
    "Guild",
    "MFALevel",
    "Message",
    "MessageNotificationLevel",
    "MessageType",
    "Reaction",
    "ReactionCountDetails",
    "Role",
    "RoleColors",
    "RoleTags",
    "Snowflake",
    "User",
    "VerificationLevel",
]
