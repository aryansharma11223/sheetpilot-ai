"""
===============================================================================
SheetPilot AI

Engineer Request Contract
===============================================================================
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class EngineerRequest(BaseModel):
    """A request submitted to the Engineering Agent."""

    prompt: str

    session_id: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
