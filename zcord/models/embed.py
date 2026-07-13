from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import ZcordModel


@dataclass(frozen=True, slots=True)
class EmbedFooter(ZcordModel):
    """
    Contain embed's footer info.

    Attributes:
        text:
            Footer text.
        icon_url:
            URL of footer icon.
        proxy_icon_url:
            A proxied URL of footer icon.
    """

    text: str
    icon: str | MISSING = MISSING
    proxy_icon_url: str | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class EmbedImage(ZcordModel):
    """
    Contain embed's image info.

    Attributes:
        url:
            Source URL of the image.
        proxy_url:
            A proxied URL of the image.
        height:
            The image's height.
        width:
            The image's width.
        content_type:
            The image's media type.
        placeholder:
            Thumbhash placeholder of the image.
        placeholder_version:
            Version of the placeholder.
        description:
            Alt text of the image.
        flags:
            Embed media flags combined as a bitfield.
    """

    url: str
    proxy_url: str | MISSING = MISSING
    height: int | MISSING = MISSING
    width: int | MISSING = MISSING
    content_type: str | MISSING = MISSING
    placeholder: str | MISSING = MISSING
    placeholder_version: int | MISSING = MISSING
    description: str | MISSING = MISSING
    flags: int | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class EmbedVideo(ZcordModel):
    """
    Contain embed's video info.

    Attributes:
        url:
            Source URL of the video.
        proxy_url:
            A proxied URL of the video.
        height:
            The video's height.
        width:
            The video's width.
        content_type:
            The video's media type.
        placeholder:
            Thumbhash placeholder of the video.
        placeholder_version:
            Version of the placeholder.
        description:
            Alt text of the video.
        flags:
            Embed media flags combined as a bitfield.
    """

    url: str | MISSING = MISSING
    proxy_url: str | MISSING = MISSING
    height: int | MISSING = MISSING
    width: int | MISSING = MISSING
    content_type: str | MISSING = MISSING
    placeholder: str | MISSING = MISSING
    placeholder_version: int | MISSING = MISSING
    description: str | MISSING = MISSING
    flags: int | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class EmbedProvider(ZcordModel):
    """
    Contain embed's provider info.

    Attributes:
        name:
            Name of the provider.
        url:
            URL of the provider.
    """

    name: str | MISSING = MISSING
    url: str | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class EmbedAuthor(ZcordModel):
    """
    Contain embed's author info.

    Attributes:
        name:
            The name of the author.
        url:
            The URL of the author.
        icon_url:
            The URL of the author icon.
        proxy_icon_url:
            A proxied url of the author icon.
    """

    name: str
    url: str | MISSING = MISSING
    icon_url: str | MISSING = MISSING
    proxy_icon_url: str | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class EmbedField(ZcordModel):
    """
    Contain embed's field info.

    Attributes:
        name:
            The name of the field.
        value:
            The value of the field.
        inline:
            Whether or not this field should display inline.
    """

    name: str
    value: str
    inline: bool | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class Embed(ZcordModel):
    """
    Represent a Discord embed.

    Attributes:
        title:
            Title of the embed.
        type:
            Type of the embed.
        description:
            Description of the embed.
        url:
            URL of the embed.
        timestamp:
            Timestamp of the embed.
        color:
            Color of the embed.
        footer:
            Embed's footer info.
        image:
            Embed's image info.
        thumbnail:
            Embed's thumbnail info.
        video:
            Embed's video info.
        provider:
            Embed's provider info.
        author:
            Embed's author info.
        fields:
            Embed's field info.
        flags:
            Embed's flags combined as a bitfield.
    """

    title: str | MISSING = MISSING
    type: str | MISSING = MISSING
    description: str | MISSING = MISSING
    url: str | MISSING = MISSING
    timestamp: datetime | MISSING = MISSING
    color: int | MISSING = MISSING
    footer: EmbedFooter | MISSING = MISSING
    image: EmbedImage | MISSING = MISSING
    thumbnail: EmbedImage | MISSING = MISSING
    video: EmbedVideo | MISSING = MISSING
    provider: EmbedProvider | MISSING = MISSING
    author: EmbedAuthor | MISSING = MISSING
    fields: list[EmbedField] | MISSING = MISSING
    flags: int | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "timestamp": datetime.fromisoformat,
        "footer": EmbedFooter,
        "image": EmbedImage,
        "thumbnail": EmbedImage,
        "video": EmbedVideo,
        "provider": EmbedProvider,
        "author": EmbedAuthor,
        "fields": EmbedField,
    }
