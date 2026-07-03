from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Self

from zcord.utils import MISSING

from .snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class RoleTags:
    type null = Literal[True]
    bot_id: Snowflake | MISSING
    integration_id: Snowflake | MISSING
    premium_subscriber: null | MISSING
    subscription_listing_id: Snowflake | MISSING
    available_for_purchase: null | MISSING
    guild_connections: null | MISSING

    @classmethod
    def _from_payload(cls, payload: dict | MISSING) -> Self | MISSING:
        if payload is MISSING:
            return MISSING
        bot_id = Snowflake(payload.get("bot_id", MISSING))
        integration_id = Snowflake(payload.get("integration_id", MISSING))
        premium_subscriber = payload.get("premium_subscriber", MISSING)
        subscription_listing_id = payload.get(
            "subscription_listing_id", MISSING
        )
        if subscription_listing_id is not MISSING:
            subscription_listing_id = Snowflake(subscription_listing_id)
        available_for_purchase = payload.get("available_for_purchase", MISSING)
        guild_connections = payload.get("guild_connections", MISSING)
        return cls(
            bot_id=bot_id,
            integration_id=integration_id,
            premium_subscriber=premium_subscriber,
            subscription_listing_id=subscription_listing_id,
            available_for_purchase=available_for_purchase,
            guild_connections=guild_connections,
        )


@dataclass(frozen=True, slots=True)
class RoleColors:
    """
    Contain the colors of the role.

    Attributes:
        primary_color: The primary color of the role.
        secondary_color: The secondary color of the role (gradient color).
        tertiary_color: The tertiary color of the role (holographic style).
    """

    primary_color: int
    secondary_color: int | None
    tertiary_color: int | None

    @classmethod
    def default(cls) -> Self:
        """
        Non color role has the default `primary_color` of `0` and `None`
        for other fields.
        """
        return cls(primary_color=0, secondary_color=None, tertiary_color=None)

    @classmethod
    def _from_payload(cls, payload: dict | None) -> Self:
        if payload is None:
            return cls.default()
        return cls(
            primary_color=payload.get("primary_color", 0),
            secondary_color=payload.get("secondary_color"),
            tertiary_color=payload.get("tertiary_color"),
        )


@dataclass(frozen=True, slots=True)
class Role:
    """
    Represent a Discord role.

    Attributes:
        id:
            The role's ID.
        name:
            The role's name.
        colors:
            The role's colors.
        hoist:
            Whether the option for "Display role members separately from online
            members" is enabled.
        icon:
            The role's icon hash.
        unicode_emoji:
            The role's unicode emoji.
        position:
            Position of the role.
        permissions:
            The role's permissions bit set.
        managed:
            Whether the role is managed by an integration.
        mentionable:
            Whether the role is mentionable.
        tags:
            The tags of the role.
        flags:
            The role's flags combined as a bitfield.
    """

    id: Snowflake
    name: str
    colors: RoleColors
    hoist: bool
    icon: str | None | MISSING
    unicode_emoji: str | None | MISSING
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: RoleTags | MISSING
    flags: int

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        id = Snowflake(payload.get("id", -1))
        name: str = payload.get("name", "")
        colors = RoleColors._from_payload(payload.get("colors"))
        hoist: bool = payload.get("hoist", False)
        icon: str = payload.get("icon", MISSING)
        unicode_emoji: str | None = payload.get("unicode_emoji", MISSING)
        position: int = payload.get("position", -1)
        permissions: str = payload.get("permissions", "")
        managed: bool = payload.get("managed", False)
        mentionable: bool = payload.get("mentionable", False)
        tags = payload.get("tags", MISSING)
        if tags is not MISSING:
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
