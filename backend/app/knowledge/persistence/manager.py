"""
===============================================================================
AEVON

Persistence Manager
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.knowledge.persistence.contracts import RepositorySnapshot
from app.knowledge.persistence.storage import (
    BaseStorage,
    JsonStorage,
)


class PersistenceManager:
    """
    Repository persistence manager.
    """

    def __init__(self) -> None:

        self._storage: BaseStorage = JsonStorage()

    @property
    def storage_name(self) -> str:
        return self._storage.name

    def save(
        self,
        snapshot: RepositorySnapshot,
        destination: Path,
    ) -> None:

        self._storage.save(
            snapshot,
            destination,
        )

    def load(
        self,
        source: Path,
    ) -> RepositorySnapshot:

        return self._storage.load(source)

    def exists(
        self,
        path: Path,
    ) -> bool:

        return path.exists()

    def delete(
        self,
        path: Path,
    ) -> None:

        if path.exists():
            path.unlink()
