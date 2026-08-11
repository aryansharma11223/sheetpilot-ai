"""
===============================================================================
SheetPilot AI

Context Builder
===============================================================================
"""

from __future__ import annotations

import time

from app.context.contracts import (
    ContextRequest,
    ContextResult,
)

from app.context.sources import (
    BaseContextSource,
    KnowledgeSource,
    RepositorySource,
    MemorySource,
)


class ContextBuilder:

    def __init__(self) -> None:

        self._sources: list[BaseContextSource] = []

        self.register(KnowledgeSource())
        self.register(RepositorySource())
        self.register(MemorySource())

    def register(
        self,
        source: BaseContextSource,
    ) -> None:

        self._sources.append(source)

    @property
    def source_count(self) -> int:
        return len(self._sources)

    def build(
        self,
        request: ContextRequest,
    ) -> ContextResult:

        start = time.perf_counter()

        sources = []

        for source in self._sources:
            sources.extend(source.collect(request))

        duration = time.perf_counter() - start

        return ContextResult(
            request=request,
            sources=sources,
            duration_seconds=duration,
        )
