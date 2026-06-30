"""Zcord - Functional programming discord API wrapper"""

from importlib.metadata import version

from .bot import Bot
from .types import Channel, ChannelType, Message, Role, Snowflake, User

__version__ = version("zcord")

__all__ = [
    "Bot",
    "Channel",
    "ChannelType",
    "Message",
    "Role",
    "Snowflake",
    "User",
]
