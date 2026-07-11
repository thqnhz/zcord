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
    Guild,
    Message,
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
    "ExplicitContentFilterLevel",
    "Guild",
    "MFALevel",
    "Message",
    "MessageNotificationLevel",
    "MessageType",
    "Role",
    "RoleColors",
    "RoleTags",
    "Snowflake",
    "User",
    "VerificationLevel",
]
