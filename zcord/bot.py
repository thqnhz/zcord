from __future__ import annotations

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
        self.http = HTTPClient(token)
