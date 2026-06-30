from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Self

from zcord.utils import MISSING

from .snowflake import Snowflake


@dataclass(frozen=True)
class User:
    """
    Represent a Discord User

    Attributes:
        id: The user's ID.
        username: The user's username.
        discriminator: The user's Discord tag.
        global_name: The user's display name if it is set.
        avatar: The user's avatar hash.
        bot: Whether the user is a bot.
        system: Whether the user is an **Official Discord System** user.
        mfa_enabled: Where the user has multi factor authentication enabled.
        banner: The user's banner hash.
        accent_color: The user's banner color encoded as an [`int`][].
        locale: The user's chosen language option.
        verified: Whether the email on this account is verified.
        email: The user's email.
        flags: The user's account flags.
        premium_type: The type of Nitro subscription of the user.
        public_flags: The user's public account flags.
        avatar_decoration_data: The user's avatar decoration data.
        collectibles: The user's collectibles data.
        primary_guild: The user's primary guild.

    Notes:
        Except bots, `User.discriminator` will be `0`.
    """

    id: Snowflake
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: bool | MISSING
    system: bool | MISSING
    mfa_enabled: bool | MISSING
    banner: str | None | MISSING
    accent_color: int | None | MISSING
    locale: str | MISSING
    verified: bool | MISSING
    email: str | None | MISSING
    flags: int | MISSING
    premium_type: int | MISSING
    public_flags: int | MISSING
    avatar_decoration_data: Any | None | MISSING
    collectibles: Any | None | MISSING
    primary_guild: Any | None | MISSING

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        id = Snowflake(payload.get("id", -1))
        username: str = payload.get("username", "")
        discriminator: str = payload.get("discriminator", "0")
        global_name: str | None = payload.get("global_name")
        avatar: str | None = payload.get("avatar")
        bot: bool = payload.get("bot", MISSING)
        system: bool = payload.get("system", MISSING)
        mfa_enabled: bool = payload.get("mfa_enabled", MISSING)
        banner: str | None = payload.get("banner", MISSING)
        accent_color: int | None = payload.get("accent_color", MISSING)
        locale: str = payload.get("locale", MISSING)
        verified: bool = payload.get("verified", MISSING)
        email: str | None = payload.get("email", MISSING)
        flags: int = payload.get("flags", MISSING)
        premium_type: int = payload.get("premium_type", MISSING)
        public_flags: int = payload.get("public_flags", MISSING)
        avatar_decoration_data: Any | None = payload.get(
            "avatar_decoration_data", MISSING
        )
        collectibles: Any | None = payload.get("collectibles", MISSING)
        primary_guild: Any | None = payload.get("primary_guild", MISSING)
        return cls(
            id=id,
            username=username,
            discriminator=discriminator,
            global_name=global_name,
            avatar=avatar,
            bot=bot,
            system=system,
            mfa_enabled=mfa_enabled,
            banner=banner,
            accent_color=accent_color,
            locale=locale,
            verified=verified,
            email=email,
            flags=flags,
            premium_type=premium_type,
            public_flags=public_flags,
            avatar_decoration_data=avatar_decoration_data,
            collectibles=collectibles,
            primary_guild=primary_guild,
        )
