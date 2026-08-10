"""
===============================================================================
SheetPilot AI

INT-001 : Dependency Contract
===============================================================================
"""

from pydantic import BaseModel


class DependencyInfo(BaseModel):
    """Represents one dependency relationship."""

    source: str
    target: str
    dependency_type: str
