"""
===============================================================================
SheetPilot AI

Cache Status
===============================================================================
"""

from enum import Enum


class CacheStatus(str, Enum):
    """
    Result of a cache lookup.
    """

    HIT = "hit"
    MISS = "miss"
    REBUILT = "rebuilt"
