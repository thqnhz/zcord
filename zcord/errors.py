from __future__ import annotations


class MutuallyExclusiveParamsError(Exception):
    """Parameters which mutually exclusive with each other have been passed."""
