"""
===============================================================================
SheetPilot AI

Base Context Source
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.context.contracts import (
    ContextRequest,
    ContextSource,
)


class BaseContextSource(ABC):
    """
    Base class for every Context Source.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human readable source name."""

    @abstractmethod
    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:
        """
        Collect relevant context.
        """
