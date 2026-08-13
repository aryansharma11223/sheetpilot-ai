"""
===============================================================================
AEVON

INT-001 : Repository Contract
===============================================================================
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.intelligence.contracts.dependency import DependencyInfo
from app.intelligence.contracts.file import FileInfo
from app.intelligence.contracts.folder import FolderInfo


class RepositoryStatistics(BaseModel):
    """Repository statistics."""

    total_files: int = 0
    total_folders: int = 0
    python_files: int = 0


class RepositorySnapshot(BaseModel):
    """Complete repository snapshot."""

    root: str

    folders: list[FolderInfo] = Field(default_factory=list)

    files: list[FileInfo] = Field(default_factory=list)

    dependencies: list[DependencyInfo] = Field(default_factory=list)

    statistics: RepositoryStatistics = Field(default_factory=RepositoryStatistics)

    scanned_at: datetime = Field(default_factory=datetime.utcnow)
