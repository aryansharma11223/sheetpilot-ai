"""
===============================================================================
AEVON

Knowledge Context Source
===============================================================================
"""

from __future__ import annotations

from app.context.contracts import (
    ContextRequest,
    ContextSource,
    ContextSourceType,
)
from app.core.paths import paths
from app.knowledge.cache import CacheManager
from app.knowledge.search import RepositorySearcher

from .base_context_source import BaseContextSource


class KnowledgeSource(BaseContextSource):
    """
    Retrieves relevant knowledge from the AEVON knowledge repository.
    """

    def __init__(self) -> None:
        self._cache = CacheManager()
        self._searcher = RepositorySearcher()

    @property
    def name(self) -> str:
        return "Knowledge"

    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:
        """
        Retrieve knowledge relevant to the request.
        """

        if not request.include_knowledge:
            return []

        repository = self._cache.load_or_build(
            paths.docs,
        )

        results = self._searcher.search(
            repository,
            request.prompt,
        )

        results = results[: request.max_items]

        return [
            ContextSource(
                id=result.item.id,
                title=result.item.title,
                source_type=ContextSourceType.KNOWLEDGE,
                path=result.item.path,
                content=result.item.content,
                score=result.score,
            )
            for result in results
        ]


__all__ = [
    "KnowledgeSource",
]
