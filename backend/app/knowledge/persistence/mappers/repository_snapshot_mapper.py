"""
===============================================================================
AEVON

Repository Snapshot Mapper
===============================================================================
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from app.knowledge.contracts import KnowledgeRepository
from app.knowledge.persistence.contracts import (
    RepositorySnapshot,
    SnapshotMetadata,
)


class RepositorySnapshotMapper:
    """
    Converts between KnowledgeRepository and RepositorySnapshot.
    """

    def to_snapshot(
        self,
        repository: KnowledgeRepository,
        root_directory: Path,
    ) -> RepositorySnapshot:

        metadata = SnapshotMetadata(
            created_at=datetime.now(),
            root_directory=str(root_directory),
            total_items=repository.count,
        )

        return RepositorySnapshot(
            metadata=metadata,
            items=repository.items,
        )

    def from_snapshot(
        self,
        snapshot: RepositorySnapshot,
    ) -> KnowledgeRepository:

        repository = KnowledgeRepository()

        for item in snapshot.items:
            repository.add(item)

        return repository
