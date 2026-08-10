"""
===============================================================================
SheetPilot AI

INT-001 : File Contract
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class FileInfo(BaseModel):
    """Represents a single file in the repository."""

    id: str
    name: str
    extension: str
    relative_path: str
    absolute_path: Path

    size_bytes: int

    is_python: bool
    is_hidden: bool
