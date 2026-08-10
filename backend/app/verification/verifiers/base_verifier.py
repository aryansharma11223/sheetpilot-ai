"""
===============================================================================
SheetPilot AI

Module:
    Base Verifier

Purpose:
    Defines the interface for all subsystem verifiers.
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.verification.contracts import VerificationResult


class BaseVerifier(ABC):
    """
    Base class for every subsystem verifier.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable subsystem name.
        """
        raise NotImplementedError

    @abstractmethod
    def run(self) -> VerificationResult:
        """
        Execute the verification and return the result.
        """
        raise NotImplementedError
