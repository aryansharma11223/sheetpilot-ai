"""
===============================================================================
SheetPilot AI

Module:
    Knowledge Indexer

Purpose:
    Discovers documentation and builds a KnowledgeRepository.
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.knowledge.contracts import KnowledgeRepository
from app.knowledge.indexers import BaseIndexer, MarkdownIndexer


class KnowledgeIndexer:
    """
    Coordinates all registered knowledge indexers.
    """

    def __init__(self) -> None:
        self._indexers: list[BaseIndexer] = []
        self.register(MarkdownIndexer())

    def register(self, indexer: BaseIndexer) -> None:
        """
        Register a knowledge indexer.
        """
        self._indexers.append(indexer)

    @property
    def indexer_count(self) -> int:
        return len(self._indexers)

    def index_directory(self, directory: Path) -> KnowledgeRepository:
        """
        Scan a directory recursively and build a KnowledgeRepository.
        """

        repository = KnowledgeRepository()

        if not directory.exists():
            return repository

        for file_path in directory.rglob("*"):

            if not file_path.is_file():
                continue

            for indexer in self._indexers:

                if not indexer.supports(file_path):
                    continue

                repository.add(indexer.index(file_path))
                break

        return repository
