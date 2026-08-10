"""
===============================================================================
SheetPilot AI

Module:
    Core Verifier

Purpose:
    Verifies the health of the application's core infrastructure.
===============================================================================
"""

from __future__ import annotations

import time

from app.core.config import settings
from app.core.constants import APP_NAME
from app.core.paths import paths

from app.verification.contracts import (
    VerificationResult,
    VerificationStatus,
)

from .base_verifier import BaseVerifier


class CoreVerifier(BaseVerifier):
    """
    Verifies the Core subsystem.
    """

    @property
    def name(self) -> str:
        return "Core"

    def run(self) -> VerificationResult:

        start = time.perf_counter()

        messages: list[str] = []
        errors: list[str] = []

        try:
            # Configuration
            _ = settings
            messages.append("Configuration loaded.")

            # Paths
            _ = paths.project_root
            messages.append("Path Manager loaded.")

            # Constants
            _ = APP_NAME
            messages.append("Constants loaded.")

            status = VerificationStatus.PASS

        except Exception as ex:
            status = VerificationStatus.FAIL
            errors.append(str(ex))

        duration = time.perf_counter() - start

        return VerificationResult(
            subsystem=self.name,
            status=status,
            duration_seconds=duration,
            messages=messages,
            errors=errors,
        )
