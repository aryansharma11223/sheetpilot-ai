"""
===============================================================================
SheetPilot AI

Base Storage Provider
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from app.knowledge.persistence.contracts import RepositorySnapshot


class BaseStorage(ABC):
    """
    Base class for persistence providers.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Storage provider name.
        """

    @abstractmethod
    def save(
        self,
        snapshot: RepositorySnapshot,
        destination: Path,
    ) -> None:
        """
        Save snapshot.
        """

    @abstractmethod
    def load(
        self,
        source: Path,
    ) -> RepositorySnapshot:
        """
        Load snapshot.
        """
