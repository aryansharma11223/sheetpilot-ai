"""
===============================================================================
AEVON

Context Engine
===============================================================================

Purpose
-------
Build execution context for an engineering request.

The Context Engine delegates context collection to ContextBuilder.
It does not contain source-specific retrieval logic.

Architecture

    ContextRequest
          │
          ▼
    ContextEngine
          │
          ▼
    ContextBuilder
      ┌───┼───────────────┐
      ▼   ▼               ▼
 Knowledge Repository   Memory
 Source    Source       Source
          │
          ▼
     ContextResult
===============================================================================
"""

from __future__ import annotations

from app.context.builders import ContextBuilder
from app.context.contracts import (
    ContextRequest,
    ContextResult,
)


class ContextEngine:
    """
    Public orchestration entry point for context construction.

    The engine delegates source collection to ContextBuilder and
    returns the resulting ContextResult.
    """

    def __init__(self) -> None:
        self._builder = ContextBuilder()

    @property
    def builder(self) -> ContextBuilder:
        """
        Return the underlying context builder.
        """
        return self._builder

    def run(
        self,
        request: ContextRequest,
    ) -> ContextResult:
        """
        Build execution context for the supplied request.
        """
        return self._builder.build(request)


__all__ = [
    "ContextEngine",
]
