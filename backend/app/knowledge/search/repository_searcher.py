"""
===============================================================================
AEVON

Repository Searcher
===============================================================================

Purpose
-------
Performs deterministic relevance-based searches over the knowledge repository.

Search strategy
---------------
1. Exact ID match
2. Exact title match
3. Exact path-stem match
4. Token overlap across:
   - ID
   - title
   - path
   - tags
   - summary
   - content

The searcher remains deterministic and does not depend on an external
embedding model or AI provider.
===============================================================================
"""

from __future__ import annotations

import re

from app.knowledge.contracts import (
    KnowledgeItem,
    KnowledgeRepository,
)

from .search_result import SearchResult


class RepositorySearcher:
    """
    Performs deterministic relevance searches over the knowledge repository.
    """

    _TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_]+")

    def search(
        self,
        repository: KnowledgeRepository,
        query: str,
    ) -> list[SearchResult]:
        """
        Search the knowledge repository using deterministic relevance scoring.

        Exact identity matches receive the highest score.

        Natural-language queries are handled using token overlap against
        searchable KnowledgeItem fields.
        """

        query = query.strip().lower()

        if not query:
            return []

        # ---------------------------------------------------------------------
        # Exact identity matching
        # ---------------------------------------------------------------------

        exact_results: list[SearchResult] = []

        for item in repository.items:
            if (
                query == item.id.lower()
                or query == item.title.lower()
                or query == item.path.stem.lower()
            ):
                exact_results.append(
                    SearchResult(
                        item=item,
                        score=1.0,
                    )
                )

        if exact_results:
            return exact_results

        # ---------------------------------------------------------------------
        # Token-based relevance search
        # ---------------------------------------------------------------------

        query_tokens = self._tokenize(query)

        if not query_tokens:
            return []

        results: list[SearchResult] = []

        for item in repository.items:
            score = self._score_item(
                item=item,
                query_tokens=query_tokens,
            )

            if score <= 0.0:
                continue

            results.append(
                SearchResult(
                    item=item,
                    score=score,
                )
            )

        results.sort(
            key=lambda result: (
                -result.score,
                result.item.title.lower(),
            )
        )

        return results

    # =========================================================================
    # Scoring
    # =========================================================================

    def _score_item(
        self,
        item: KnowledgeItem,
        query_tokens: set[str],
    ) -> float:
        """
        Calculate deterministic relevance score for a KnowledgeItem.
        """

        field_scores = (
            (
                self._tokenize(item.id),
                1.0,
            ),
            (
                self._tokenize(item.title),
                1.0,
            ),
            (
                self._tokenize(item.path.stem),
                0.9,
            ),
            (
                self._tokenize(" ".join(item.tags)),
                0.8,
            ),
            (
                self._tokenize(item.summary),
                0.7,
            ),
            (
                self._tokenize(item.content),
                0.4,
            ),
        )

        best_score = 0.0

        for field_tokens, weight in field_scores:
            if not field_tokens:
                continue

            overlap = query_tokens.intersection(field_tokens)

            if not overlap:
                continue

            coverage = len(overlap) / len(query_tokens)

            score = coverage * weight

            if score > best_score:
                best_score = score

        return round(
            min(best_score, 0.99),
            4,
        )

    # =========================================================================
    # Tokenization
    # =========================================================================

    @classmethod
    def _tokenize(
        cls,
        value: str,
    ) -> set[str]:
        """
        Convert text into normalized search tokens.
        """

        return {
            token
            for token in cls._TOKEN_PATTERN.findall(
                value.lower()
            )
            if len(token) > 1
        }


__all__ = [
    "RepositorySearcher",
]
