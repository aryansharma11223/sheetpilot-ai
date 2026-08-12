"""
AEVON Platform
==============

Core Exception Framework

Provides the structured exception model used throughout AEVON.

Responsibilities:
- Define platform error codes.
- Provide structured exceptions.
- Provide domain-level exception boundaries.

This module does NOT handle:
- Logging
- Telemetry
- Recovery workflows
- User notifications
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Final, Mapping
import json


###############################################################################
# Constants
###############################################################################

ERROR_CODE_PADDING: Final[int] = 3
ERROR_CODE_SEPARATOR: Final[str] = "-"


###############################################################################
# Error Code
###############################################################################


@dataclass(frozen=True, slots=True)
class ErrorCode:
    """
    Immutable platform error identifier.

    Format:
        DOMAIN-NNN

    Example:
        CORE-001
    """

    domain: str
    number: int

    def __post_init__(self) -> None:
        domain = self.domain.strip().upper()

        if not domain:
            raise ValueError("Error code domain cannot be empty.")

        if self.number < 0:
            raise ValueError(
                "Error code number must be greater than or equal to zero."
            )

        object.__setattr__(self, "domain", domain)

    @property
    def code(self) -> str:
        """Return formatted error code."""

        return (
            f"{self.domain}"
            f"{ERROR_CODE_SEPARATOR}"
            f"{self.number:0{ERROR_CODE_PADDING}d}"
        )

    def __str__(self) -> str:
        return self.code


###############################################################################
# Base Exception
###############################################################################


class AevonError(Exception):
    """
    Root exception for the AEVON platform.
    """

    def __init__(
        self,
        *,
        error_code: ErrorCode,
        message: str,
        details: Mapping[str, Any] | None = None,
        cause: Exception | None = None,
        suggestion: str | None = None,
        recoverable: bool = False,
    ) -> None:

        super().__init__(message)

        self.error_code = error_code
        self.message = message

        self.details = MappingProxyType(
            dict(details or {})
        )

        self.cause = cause
        self.__cause__ = cause

        self.suggestion = suggestion
        self.recoverable = recoverable

    def to_dict(self) -> dict[str, Any]:
        """
        Convert exception information into a serializable structure.
        """

        return {
            "error_code": self.error_code.code,
            "message": self.message,
            "details": dict(self.details),
            "suggestion": self.suggestion,
            "recoverable": self.recoverable,
            "cause": repr(self.cause) if self.cause else None,
        }

    def to_json(self) -> str:
        """
        Convert exception information into JSON.
        """

        return json.dumps(
            self.to_dict(),
            ensure_ascii=False,
        )

    @property
    def has_details(self) -> bool:
        return bool(self.details)

    @property
    def has_cause(self) -> bool:
        return self.cause is not None

    @property
    def is_recoverable(self) -> bool:
        return self.recoverable

    def __str__(self) -> str:
        return (
            f"[{self.error_code.code}] "
            f"{self.message}"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"error_code={self.error_code.code!r}, "
            f"message={self.message!r})"
        )


###############################################################################
# Platform Exception Domains
###############################################################################


class CoreError(AevonError):
    """Core platform failure."""


class KernelError(AevonError):
    """Kernel subsystem failure."""


class KnowledgeError(AevonError):
    """Knowledge subsystem failure."""


class MemorySubsystemError(AevonError):
    """Memory subsystem failure."""


class EngineError(AevonError):
    """Generic intelligence engine failure."""


class InfrastructureError(AevonError):
    """Infrastructure and runtime failure."""


class ConnectorError(AevonError):
    """External connector failure."""


class PluginError(AevonError):
    """Plugin subsystem failure."""


class ValidationError(AevonError):
    """Input or schema validation failure."""


class ConfigurationError(CoreError):
    """Configuration related failure."""


class SecurityError(InfrastructureError):
    """Security related failure."""


###############################################################################
# Public API
###############################################################################


__all__ = [
    "ErrorCode",
    "AevonError",
    "CoreError",
    "KernelError",
    "KnowledgeError",
    "MemorySubsystemError",
    "EngineError",
    "InfrastructureError",
    "ConnectorError",
    "PluginError",
    "ValidationError",
    "ConfigurationError",
    "SecurityError",
]
