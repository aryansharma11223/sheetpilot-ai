"""
===============================================================================
SheetPilot AI

INT-001 : Folder Contract
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class FolderInfo(BaseModel):
    """Represents a folder inside the repository."""

    name: str
    relative_path: str
    absolute_path: Path
