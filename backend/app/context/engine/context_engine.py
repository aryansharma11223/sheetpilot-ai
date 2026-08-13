"""
===============================================================================
AEVON

Context Engine
===============================================================================

Purpose:
    Public orchestration boundary for context retrieval.

Architecture:

    ContextEngine
         |
         v
    ContextBuilder
         |
         +-- KnowledgeSource
         +-- RepositorySource
         +-- MemorySource

The Context Engine owns the context-building workflow while
individual Context Sources remain responsible for collecting
their own context.
===============================================================================
"""

from __future__ import annotations

from app.context.context_builder import ContextBuilder
from app.context.contracts import (
    ContextRequest,
    ContextResult,
)


class ContextEngine:
    """
    Public orchestration boundary for AEVON context retrieval.

    The Context Engine delegates source collection to ContextBuilder.
    It intentionally does not implement source-specific retrieval logic.
    """

    def __init__(self) -> None:
        self._builder = ContextBuilder()

    def run(
        self,
        request: ContextRequest,
    ) -> ContextResult:
        """
        Build execution context for the supplied request.
        """

        return self._builder.build(request)

    @property
    def builder(self) -> ContextBuilder:
        """
        Return the underlying context builder.
        """

        return self._builder

    @property
    def source_count(self) -> int:
        """
        Return the number of registered context sources.
        """

        return self._builder.source_count


__all__ = [
    "ContextEngine",
]
