"""
===============================================================================
SheetPilot AI

Module:
    Knowledge Repository

Version:
    0.1.0

Purpose:
    Stores and manages engineering knowledge items.
===============================================================================
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .knowledge_item import KnowledgeCategory, KnowledgeItem


class KnowledgeRepository(BaseModel):
    """
    Collection of engineering knowledge.
    """

    items: list[KnowledgeItem] = Field(default_factory=list)

    def add(self, item: KnowledgeItem) -> None:
        """Add a knowledge item."""
        self.items.append(item)

    def all(self) -> list[KnowledgeItem]:
        """Return all knowledge items."""
        return self.items

    def by_category(
        self,
        category: KnowledgeCategory,
    ) -> list[KnowledgeItem]:
        """Return all knowledge items of a category."""
        return [
            item
            for item in self.items
            if item.category == category
        ]

    @property
    def count(self) -> int:
        """Total number of knowledge items."""
        return len(self.items)
