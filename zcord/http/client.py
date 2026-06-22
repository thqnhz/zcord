from __future__ import annotations

import aiohttp
import orjson


class HTTPClient:
    BASE_URL = "https://discord.com/api/v10"

    def __init__(self, token: str) -> None:
        self._token = token
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self) -> HTTPClient:
        self._session = aiohttp.ClientSession(
            headers={"Authorization": f"Bot {self._token}"}
        )
        return self

    async def __aexit__(self, *args) -> None:
        if self._session:
            await self._session.close()

    async def request(
        self, method: str, endpoint: str, *, json: dict | list | None = None
    ) -> dict | list:
        assert self._session, "Use 'async with client:' context manager"
        async with self._session.request(
            method, self.BASE_URL + endpoint, json=json
        ) as resp:
            return orjson.loads(await resp.read())
