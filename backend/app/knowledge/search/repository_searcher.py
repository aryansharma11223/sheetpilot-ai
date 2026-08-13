"""
===============================================================================
AEVON

Repository Searcher
===============================================================================
"""

from __future__ import annotations

from app.knowledge.contracts import (
    KnowledgeItem,
    KnowledgeRepository,
)

from .search_result import SearchResult


class RepositorySearcher:
    """
    Performs deterministic searches over the knowledge repository.
    """

    def search(
        self,
        repository: KnowledgeRepository,
        query: str,
    ) -> list[SearchResult]:

        query = query.strip().lower()

        results: list[SearchResult] = []

        for item in repository.items:
            if (
                query == item.id.lower()
                or query == item.title.lower()
                or query == item.path.stem.lower()
            ):
                results.append(
                    SearchResult(
                        item=item,
                        score=1.0,
                    )
                )

        return results
