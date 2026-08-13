"""
===============================================================================
AEVON

Module:
    Verification Result

Purpose:
    Standard contract returned by every verifier.
===============================================================================
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class VerificationStatus(str, Enum):
    """
    Possible verification outcomes.
    """

    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"
    SKIPPED = "SKIPPED"


class VerificationResult(BaseModel):
    """
    Result returned by a verifier.
    """

    subsystem: str

    status: VerificationStatus

    duration_seconds: float = 0.0

    messages: list[str] = Field(default_factory=list)

    errors: list[str] = Field(default_factory=list)

    @property
    def successful(self) -> bool:
        """
        True when verification passed.
        """
        return self.status == VerificationStatus.PASS
