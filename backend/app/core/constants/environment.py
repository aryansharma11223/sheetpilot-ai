"""
===============================================================================
AEVON

CORE-004 : Environment Constants
===============================================================================
"""

from enum import Enum


class Environment(str, Enum):
    """Supported runtime environments."""

    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"
