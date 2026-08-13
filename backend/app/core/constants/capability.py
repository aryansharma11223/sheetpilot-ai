"""
===============================================================================
AEVON

CORE-004 : Capability Constants
===============================================================================
"""

from enum import Enum


class CapabilityStatus(str, Enum):
    """Capability lifecycle."""

    ACTIVE = "active"
    DISABLED = "disabled"
    EXPERIMENTAL = "experimental"
    DEPRECATED = "deprecated"
