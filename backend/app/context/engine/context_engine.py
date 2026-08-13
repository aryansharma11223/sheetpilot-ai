"""
===============================================================================
AEVON

Context Engine
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.context.contracts import (
    ContextRequest,
    ContextResult,
    ContextSource,
    ContextSourceType,
)
from app.knowledge.cache import CacheManager
from app.knowledge.search import RepositorySearcher


class ContextEngine:
    """
    Retrieves relevant context from the knowledge repository.
    """

    def __init__(self) -> None:

        self._cache = CacheManager()
        self._searcher = RepositorySearcher()

    def run(
        self,
        request: ContextRequest,
    ) -> ContextResult:

        repository = self._cache.load_or_build(
            Path("../docs"),
        )

        search_results = self._searcher.search(
            repository,
            request.prompt,
        )

        sources: list[ContextSource] = []

        for result in search_results:
            item = result.item

            sources.append(
                ContextSource(
                    id=item.id,
                    title=item.title,
                    source_type=ContextSourceType.KNOWLEDGE,
                    path=item.path,
                    content=item.content,
                    score=result.score,
                )
            )

        return ContextResult(
            request=request,
            sources=sources,
        )
