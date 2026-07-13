from __future__ import annotations

from zcord.utils import from_payload


class ZcordModel:
    """
    Base class for all Discord API Models.
    """

    def __int__(self):
        if hasattr(self, "id"):
            return self.id

    @classmethod
    def _from_payload(cls, payload):
        return from_payload(cls, payload, **getattr(cls, "_transforms", {}))
