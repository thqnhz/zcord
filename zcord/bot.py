from __future__ import annotations

from zcord.http import HTTPClient


class Bot:
    def __init__(self, token: str) -> None:
        self.http = HTTPClient(token)
