from __future__ import annotations

import dataclasses
from typing import Any

from zcord.missing import MISSING


def _apply_transform(transform, value):
    if hasattr(transform, "_from_payload"):
        return transform._from_payload(value)
    return transform(value)


def from_payload(cls, payload: dict | MISSING, **transforms) -> Any:
    if payload is MISSING:
        return MISSING
    kwargs = {}
    for f in dataclasses.fields(cls):
        value = payload.get(f.name, f.default)
        if (
            f.name in transforms
            and value is not None
            and value is not f.default
        ):
            t = transforms[f.name]
            if isinstance(value, list):
                value = [_apply_transform(t, v) for v in value]
            else:
                value = _apply_transform(t, value)
        kwargs[f.name] = value
    return cls(**kwargs)


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
