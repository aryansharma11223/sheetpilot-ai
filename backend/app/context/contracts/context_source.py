"""
===============================================================================
AEVON

Module:
    Context Source

Purpose:
    Represents one piece of context retrieved by the Context Engine.
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field

from .context_source_type import ContextSourceType


class ContextSource(BaseModel):
    """
    One retrieved context item.
    """

    id: str

    title: str

    source_type: ContextSourceType

    path: Path | None = None

    content: str = ""

    score: float = 0.0

    metadata: dict[str, str] = Field(default_factory=dict)
