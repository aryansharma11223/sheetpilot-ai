"""
===============================================================================
AEVON

Module:
    Base Indexer

Purpose:
    Defines the interface for all knowledge indexers.

Every knowledge indexer must inherit from BaseIndexer.

Examples:
    - MarkdownIndexer
    - PythonIndexer
    - JsonIndexer
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from app.knowledge.contracts import KnowledgeItem


class BaseIndexer(ABC):
    """
    Base class for every knowledge indexer.
    """

    @property
    @abstractmethod
    def supported_extensions(self) -> set[str]:
        """
        Returns the file extensions supported by this indexer.

        Example:
            {".md"}
            {".py"}
        """
        raise NotImplementedError

    def supports(self, path: Path) -> bool:
        """
        Returns True if this indexer can process the given file.
        """
        return path.suffix.lower() in self.supported_extensions

    @abstractmethod
    def index(self, path: Path) -> KnowledgeItem:
        """
        Convert a file into a KnowledgeItem.
        """
        raise NotImplementedError
