"""
===============================================================================
AEVON

Module:
    Markdown Indexer

Purpose:
    Converts Markdown documents into KnowledgeItem objects.
===============================================================================
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from app.knowledge.contracts import (
    KnowledgeCategory,
    KnowledgeItem,
)

from .base_indexer import BaseIndexer


class MarkdownIndexer(BaseIndexer):
    """
    Indexer for Markdown documents.
    """

    @property
    def supported_extensions(self) -> set[str]:
        return {".md"}

    def index(self, path: Path) -> KnowledgeItem:
        """
        Convert a Markdown file into a KnowledgeItem.
        """

        content = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        return KnowledgeItem(
            id=path.stem,
            title=path.stem.replace("_", " "),
            category=KnowledgeCategory.GENERAL,
            path=path,
            content=content,
            last_modified=datetime.fromtimestamp(path.stat().st_mtime),
        )
