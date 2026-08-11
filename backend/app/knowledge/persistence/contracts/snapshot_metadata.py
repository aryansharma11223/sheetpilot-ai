"""
===============================================================================
SheetPilot AI

Snapshot Metadata Contract
===============================================================================
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class SnapshotMetadata(BaseModel):
    """
    Metadata describing a repository snapshot.
    """

    created_at: datetime

    root_directory: str

    total_items: int

    version: str = "1.0"
