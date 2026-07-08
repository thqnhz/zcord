from __future__ import annotations

import dataclasses
from typing import Any

from typing_extensions import Sentinel

MISSING = Sentinel("MISSING")
"""
A special marker indicating that a value was not provided.

Notes:
    Unlike [`None`][], `MISSING` means the parameter **was omitted entirely**.
"""


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
            if isinstance(value, list):
                li = []
                for v in value:
                    v = transforms[f.name](v)
                    li.append(v)
                value = li
            else:
                value = transforms[f.name](value)
        kwargs[f.name] = value
    return cls(**kwargs)
