"""
===============================================================================
SheetPilot AI

Module:
    Engineering Context

Version:
    0.1.0

Purpose:
    Represents the complete engineering context used for AI reasoning.
===============================================================================
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.agents.contracts import EngineerRequest
from app.intelligence.contracts import RepositorySnapshot


class EngineeringContext(BaseModel):
    """
    Complete engineering context supplied to the AI.
    """

    request: EngineerRequest

    repository: RepositorySnapshot

    created_at: datetime = Field(default_factory=datetime.utcnow)
