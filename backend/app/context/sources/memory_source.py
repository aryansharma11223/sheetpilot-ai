"""
===============================================================================
AEVON

Memory Context Source
===============================================================================
"""

from __future__ import annotations

from app.context.contracts import (
    ContextRequest,
    ContextSource,
)

from .base_context_source import BaseContextSource


class MemorySource(BaseContextSource):
    """
    Retrieves relevant information from the AEVON memory subsystem.

    The persistent memory subsystem is not implemented yet.

    Until that subsystem exists, this source deliberately returns no results
    rather than exposing fabricated or placeholder memory.
    """

    @property
    def name(self) -> str:
        return "Memory"

    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:
        """
        Collect relevant memory context.

        Memory retrieval is currently unavailable because the persistent
        memory subsystem has not been implemented yet.
        """

        if not request.include_memory:
            return []

        return []


__all__ = [
    "MemorySource",
]
