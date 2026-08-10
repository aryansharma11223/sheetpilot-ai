"""
===============================================================================
SheetPilot AI

Module:
    Verification Runner

Purpose:
    Coordinates all registered subsystem verifiers.
===============================================================================
"""

from __future__ import annotations

from app.verification.contracts import VerificationResult
from app.verification.verifiers import (
    BaseVerifier,
    CoreVerifier,
    KnowledgeVerifier,
)


class VerificationRunner:
    """
    Coordinates execution of all subsystem verifiers.
    """

    def __init__(self) -> None:
        self._verifiers: list[BaseVerifier] = []

        self.register(CoreVerifier())
        self.register(KnowledgeVerifier())

    def register(self, verifier: BaseVerifier) -> None:
        """
        Register a verifier.
        """
        self._verifiers.append(verifier)

    @property
    def verifier_count(self) -> int:
        """
        Number of registered verifiers.
        """
        return len(self._verifiers)

    def run_all(self) -> list[VerificationResult]:
        """
        Execute all registered verifiers.
        """
        return [verifier.run() for verifier in self._verifiers]
