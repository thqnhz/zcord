from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Self

from zcord.utils import _MISSING

from .snowflake import Snowflake


@dataclass
class RoleTags:
    type null = Literal[True]
    bot_id: Snowflake | _MISSING
    integration_id: Snowflake | _MISSING
    premium_subscriber: null | _MISSING
    subscription_listing_id: Snowflake | _MISSING
    available_for_purchase: null | _MISSING
    guild_connections: null | _MISSING

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        bot_id = payload.get("bot_id", _MISSING)
        if bot_id is not _MISSING:
            bot_id = Snowflake(bot_id)
        integration_id = payload.get("integration_id", _MISSING)
        if integration_id is not _MISSING:
            integration_id = Snowflake(integration_id)
        premium_subscriber = payload.get("premium_subscriber", _MISSING)
        subscription_listing_id = payload.get(
            "subscription_listing_id", _MISSING
        )
        if subscription_listing_id is not _MISSING:
            subscription_listing_id = Snowflake(subscription_listing_id)
        available_for_purchase = payload.get("available_for_purchase", _MISSING)
        guild_connections = payload.get("guild_connections", _MISSING)
        return cls(
            bot_id=bot_id,
            integration_id=integration_id,
            premium_subscriber=premium_subscriber,
            subscription_listing_id=subscription_listing_id,
            available_for_purchase=available_for_purchase,
            guild_connections=guild_connections,
        )


@dataclass
class RoleColors:
    primary_color: int
    secondary_color: int | None
    tertiary_color: int | None

    @classmethod
    def default(cls) -> Self:
        return cls(primary_color=0, secondary_color=None, tertiary_color=None)

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        return cls(
            primary_color=payload.get("primary_color", 0),
            secondary_color=payload.get("secondary_color"),
            tertiary_color=payload.get("tertiary_color"),
        )


@dataclass
class Role:
    """Represent a Discord Role"""

    id: Snowflake
    name: str
    colors: RoleColors
    hoist: bool
    icon: str | None | _MISSING
    unicode_emoji: str | None | _MISSING
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: RoleTags | _MISSING
    flags: int

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        id = Snowflake(payload.get("id", -1))
        name: str = payload.get("name", "")
        colors = payload.get("colors")
        if colors is not None and colors is not _MISSING:
            colors = RoleColors._from_payload(colors)
        else:
            colors = RoleColors.default()
        hoist: bool = payload.get("hoist", False)
        icon: str = payload.get("icon", _MISSING)
        unicode_emoji: str | None = payload.get("unicode_emoji", _MISSING)
        position: int = payload.get("position", -1)
        permissions: str = payload.get("permissions", "")
        managed: bool = payload.get("managed", False)
        mentionable: bool = payload.get("mentionable", False)
        tags = payload.get("tags", _MISSING)
        if tags is not _MISSING:
            tags = RoleTags._from_payload(tags)
        flags: int = payload.get("flags", -1)
        return cls(
            id=id,
            name=name,
            colors=colors,
            hoist=hoist,
            icon=icon,
            unicode_emoji=unicode_emoji,
            position=position,
            permissions=permissions,
            managed=managed,
            mentionable=mentionable,
            tags=tags,
            flags=flags,
        )
