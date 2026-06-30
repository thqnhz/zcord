from __future__ import annotations

from typing_extensions import Sentinel

MISSING = Sentinel("MISSING")
"""
A special marker indicating that a value was not provided.

Notes:
    Unlike [`None`][], `MISSING` means the parameter **was omitted entirely**.
"""
