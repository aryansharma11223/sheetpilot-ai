"""
===============================================================================
AEVON

Repository Context Source
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.context.contracts import (
    ContextRequest,
    ContextSource,
    ContextSourceType,
)

from .base_context_source import BaseContextSource


class RepositorySource(BaseContextSource):
    """
    Retrieves relevant source files from the AEVON repository.
    """

    _EXCLUDED_DIRECTORIES = {
        ".git",
        ".venv",
        "__pycache__",
        ".aevon",
        "node_modules",
        "dist",
        "build",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
    }

    _SUPPORTED_EXTENSIONS = {
        ".py",
        ".qml",
        ".js",
        ".ts",
        ".json",
        ".toml",
        ".yaml",
        ".yml",
    }

    @property
    def name(self) -> str:
        return "Repository"

    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:
        """
        Collect repository files relevant to the request.
        """

        if not request.include_repository:
            return []

        project_root = Path.cwd()

        query_terms = {
            term.lower()
            for term in request.prompt.split()
            if len(term) >= 3
        }

        sources: list[ContextSource] = []

        for path in project_root.rglob("*"):
            if not path.is_file():
                continue

            if path.suffix.lower() not in self._SUPPORTED_EXTENSIONS:
                continue

            relative_path = path.relative_to(project_root)

            parts = {
                part.lower()
                for part in relative_path.parts
            }

            if parts & self._EXCLUDED_DIRECTORIES:
                continue

            path_text = str(relative_path).lower()

            try:
                content = path.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )
            except OSError:
                continue

            content_lower = content.lower()

            matches = sum(
                1
                for term in query_terms
                if term in path_text
                or term in content_lower
            )

            if matches == 0:
                continue

            score = min(
                0.95,
                0.50 + (matches * 0.10),
            )

            sources.append(
                ContextSource(
                    id=str(relative_path),
                    title=path.name,
                    source_type=ContextSourceType.REPOSITORY,
                    path=relative_path,
                    content=content,
                    score=score,
                )
            )

        sources.sort(
            key=lambda source: source.score,
            reverse=True,
        )

        return sources[: request.max_items]


__all__ = [
    "RepositorySource",
]
