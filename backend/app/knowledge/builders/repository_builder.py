"""
===============================================================================
SheetPilot AI

Repository Builder
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.knowledge.contracts import KnowledgeRepository
from app.knowledge.knowledge_indexer import KnowledgeIndexer


class RepositoryBuilder:
    """
    Builds a KnowledgeRepository from a knowledge source.
    """

    def __init__(self) -> None:
        self._indexer = KnowledgeIndexer()

    def build(
        self,
        docs_path: Path,
    ) -> KnowledgeRepository:
        """
        Build a repository from the supplied directory.
        """
        return self._indexer.index_directory(docs_path)
