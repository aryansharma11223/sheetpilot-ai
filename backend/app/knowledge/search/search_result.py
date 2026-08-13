"""
===============================================================================
AEVON

Repository Search Result
===============================================================================
"""

from __future__ import annotations

from pydantic import BaseModel

from app.knowledge.contracts import KnowledgeItem


class SearchResult(BaseModel):
    """
    Represents one repository search result.
    """

    item: KnowledgeItem

    score: float = 1.0
