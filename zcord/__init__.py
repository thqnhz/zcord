"""Zcord - Functional programming discord API wrapper"""

from importlib.metadata import version

from .bot import Bot
from .types import (
    Channel,
    ChannelType,
    Guild,
    Message,
    MessageType,
    Role,
    RoleColors,
    Snowflake,
    User,
)
from .utils import MISSING

__version__ = version("zcord")

__all__ = [
    "MISSING",
    "Bot",
    "Channel",
    "ChannelType",
    "Guild",
    "Message",
    "MessageType",
    "Role",
    "RoleColors",
    "Snowflake",
    "User",
]
