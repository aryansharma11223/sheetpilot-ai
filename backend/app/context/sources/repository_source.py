"""
Repository Context Source
"""

from __future__ import annotations

from app.context.contracts import (
    ContextRequest,
    ContextSource,
    ContextSourceType,
)

from .base_context_source import BaseContextSource


class RepositorySource(BaseContextSource):

    @property
    def name(self) -> str:
        return "Repository"

    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:

        return [
            ContextSource(
                id="repository-demo",
                title="Repository Source",
                source_type=ContextSourceType.REPOSITORY,
                content=f"Repository context for '{request.prompt}'",
                score=0.9,
            )
        ]
