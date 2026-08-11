"""
Memory Context Source
"""

from __future__ import annotations

from app.context.contracts import (
    ContextRequest,
    ContextSource,
    ContextSourceType,
)

from .base_context_source import BaseContextSource


class MemorySource(BaseContextSource):

    @property
    def name(self) -> str:
        return "Memory"

    def collect(
        self,
        request: ContextRequest,
    ) -> list[ContextSource]:

        return [
            ContextSource(
                id="memory-demo",
                title="Memory Source",
                source_type=ContextSourceType.MEMORY,
                content=f"Memory context for '{request.prompt}'",
                score=0.8,
            )
        ]
