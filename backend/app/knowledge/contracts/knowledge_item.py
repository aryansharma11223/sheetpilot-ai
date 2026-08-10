"""
===============================================================================
SheetPilot AI

Module:
    Knowledge Item

Version:
    0.1.0

Purpose:
    Represents a single piece of engineering knowledge loaded from the project's
    documentation.

Engineering Standard:
    Contract First Design
===============================================================================
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field


class KnowledgeCategory(str, Enum):
    """
    Categories of engineering knowledge.
    """

    ARCHITECTURE = "architecture"
    ENGINEERING_STANDARD = "engineering_standard"
    ADR = "adr"
    ROADMAP = "roadmap"
    CHANGELOG = "changelog"
    TASK = "task"
    PATTERN = "pattern"
    LESSON = "lesson"
    GENERAL = "general"


class KnowledgeItem(BaseModel):
    """
    Represents a single engineering knowledge document.
    """

    id: str

    title: str

    category: KnowledgeCategory = KnowledgeCategory.GENERAL

    path: Path

    content: str = ""

    last_modified: datetime

    tags: list[str] = Field(default_factory=list)

    summary: str = ""

    def __str__(self) -> str:
        return f"{self.category.value}: {self.title}"
