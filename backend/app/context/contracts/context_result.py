"""
===============================================================================
AEVON

Module:
    Context Result

Purpose:
    Result returned by the Context Engine.
===============================================================================
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .context_request import ContextRequest
from .context_source import ContextSource


class ContextResult(BaseModel):
    """
    Result produced by the Context Engine.
    """

    request: ContextRequest

    sources: list[ContextSource] = Field(default_factory=list)

    duration_seconds: float = 0.0

    @property
    def source_count(self) -> int:
        """
        Number of retrieved sources.
        """
        return len(self.sources)
