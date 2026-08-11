"""
Knowledge Context Source
"""

from __future__ import annotations

from app.context.contracts import (
    ContextRequest,
    ContextSource,
    ContextSourceType,
)

from .base_context_source import BaseContextSource


class KnowledgeSource(BaseContextSource):

    @property
    def name(self) -> str:
        return "Knowledge"

    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:

        return [
            ContextSource(
                id="knowledge-demo",
                title="Knowledge Source",
                source_type=ContextSourceType.KNOWLEDGE,
                content=f"Knowledge context for '{request.prompt}'",
                score=1.0,
            )
        ]
