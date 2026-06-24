from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Self

from zcord.utils import _MISSING

from .snowflake import Snowflake


@dataclass
class User:
    """Represent a Discord User"""

    id: Snowflake
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: bool | _MISSING
    system: bool | _MISSING
    mfa_enabled: bool | _MISSING
    banner: str | None | _MISSING
    accent_color: int | None | _MISSING
    locale: str | _MISSING
    verified: bool | _MISSING
    email: str | None | _MISSING
    flags: int | _MISSING
    premium_type: int | _MISSING
    public_flags: int | _MISSING
    avatar_decoration_data: Any | None | _MISSING
    collectibles: Any | None | _MISSING
    primary_guild: Any | None | _MISSING

    @classmethod
    def _from_payload(cls, payload: dict) -> Self:
        id = Snowflake(payload.get("id", -1))
        username: str = payload.get("username", "")
        discriminator: str = payload.get("discriminator", "0")
        global_name: str | None = payload.get("global_name")
        avatar: str | None = payload.get("avatar")
        bot: bool = payload.get("bot", _MISSING)
        system: bool = payload.get("system", _MISSING)
        mfa_enabled: bool = payload.get("mfa_enabled", _MISSING)
        banner: str | None = payload.get("banner", _MISSING)
        accent_color: int | None = payload.get("accent_color", _MISSING)
        locale: str = payload.get("locale", _MISSING)
        verified: bool = payload.get("verified", _MISSING)
        email: str | None = payload.get("email", _MISSING)
        flags: int = payload.get("flags", _MISSING)
        premium_type: int = payload.get("premium_type", _MISSING)
        public_flags: int = payload.get("public_flags", _MISSING)
        avatar_decoration_data: Any | None = payload.get(
            "avatar_decoration_data", _MISSING
        )
        collectibles: Any | None = payload.get("collectibles", _MISSING)
        primary_guild: Any | None = payload.get("primary_guild", _MISSING)
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
