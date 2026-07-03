from __future__ import annotations

from typing import Self

from zcord.http import HTTPClient


class Bot:
    """
    Represent the bot client
    """

    def __init__(self, token: str) -> None:
        """
        Params:
            token: The bot token.
        """
        self._token = token
        self._http: HTTPClient | None = None

    @property
    def http(self) -> HTTPClient:
        if self._http is None:
            self._http = HTTPClient(self._token)
        return self._http

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        if self._http is not None:
            await self._http.close()
            self._http = None
