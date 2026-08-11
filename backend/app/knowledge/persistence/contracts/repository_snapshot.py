"""
===============================================================================
SheetPilot AI

Repository Snapshot Contract
===============================================================================
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from app.knowledge.contracts import KnowledgeItem

from .snapshot_metadata import SnapshotMetadata


class RepositorySnapshot(BaseModel):
    """
    Serializable snapshot of the Knowledge Repository.
    """

    metadata: SnapshotMetadata

    items: list[KnowledgeItem] = Field(default_factory=list)

    @property
    def item_count(self) -> int:
        """
        Number of indexed knowledge items.
        """
        return len(self.items)
