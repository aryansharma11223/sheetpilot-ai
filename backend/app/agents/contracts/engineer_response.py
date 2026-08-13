"""
===============================================================================
AEVON

Engineer Response Contract
===============================================================================
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class EngineerResponse(BaseModel):
    """Response returned by the Engineering Agent."""

    success: bool = False

    message: str = ""

    repository_scanned: bool = False

    context_built: bool = False

    context_sources: int = 0

    plan_created: bool = False

    execution_completed: bool = False

    total_files: int = 0

    total_folders: int = 0

    relevant_files: list[str] = Field(default_factory=list)
