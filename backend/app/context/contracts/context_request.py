"""
===============================================================================
AEVON

Module:
    Context Request

Purpose:
    Represents a request to build execution context.
===============================================================================
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ContextRequest(BaseModel):
    """
    Input to the Context Engine.
    """

    prompt: str

    max_items: int = 10

    include_knowledge: bool = True

    include_repository: bool = True

    include_memory: bool = True

    tags: list[str] = Field(default_factory=list)
