"""
===============================================================================
SheetPilot AI

Knowledge Cache Manager
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.core import PathManager
from app.knowledge.builders import RepositoryBuilder
from app.knowledge.contracts import KnowledgeRepository
from app.knowledge.persistence.manager import PersistenceManager
from app.knowledge.persistence.mappers import RepositorySnapshotMapper

from .contracts import CacheStatus


class CacheManager:
    """
    Handles loading, rebuilding and caching the knowledge repository.
    """

    def __init__(self) -> None:

        self._persistence = PersistenceManager()
        self._builder = RepositoryBuilder()
        self._mapper = RepositorySnapshotMapper()

        self._status = CacheStatus.MISS

    @property
    def cache_file(self) -> Path:
        return PathManager.knowledge_cache()

    @property
    def status(self) -> CacheStatus:
        return self._status

    def exists(self) -> bool:
        return self._persistence.exists(self.cache_file)

    def delete(self) -> None:
        self._persistence.delete(self.cache_file)

    def load(self) -> KnowledgeRepository:
        """
        Load the repository from cache.
        """

        snapshot = self._persistence.load(
            self.cache_file,
        )

        repository = self._mapper.from_snapshot(
            snapshot,
        )

        self._status = CacheStatus.HIT

        return repository

    def save(
        self,
        repository: KnowledgeRepository,
        root_directory: Path,
    ) -> None:
        """
        Save the repository to cache.
        """

        snapshot = self._mapper.to_snapshot(
            repository,
            root_directory,
        )

        self._persistence.save(
            snapshot,
            self.cache_file,
        )

    def rebuild(
        self,
        docs_path: Path,
    ) -> KnowledgeRepository:
        """
        Build and cache a fresh repository.
        """

        repository = self._builder.build(
            docs_path,
        )

        self.save(
            repository,
            docs_path,
        )

        self._status = CacheStatus.REBUILT

        return repository

    def load_or_build(
        self,
        docs_path: Path,
    ) -> KnowledgeRepository:
        """
        Load an existing repository or rebuild it.
        """

        if self.exists():
            return self.load()

        return self.rebuild(
            docs_path,
        )
