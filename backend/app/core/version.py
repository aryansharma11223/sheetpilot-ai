"""
AEVON Platform
==============

Core Version Framework

This module defines immutable version and release models used throughout
the AEVON platform.

Responsibilities:
- Represent semantic versions.
- Represent build metadata.
- Represent release information.

This module does NOT:
- Read Git information.
- Inspect the environment.
- Detect installed packages.
- Perform release operations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


###############################################################################
# Constants
###############################################################################

VERSION_SEPARATOR: Final[str] = "."


###############################################################################
# Semantic Version
###############################################################################


@dataclass(frozen=True, slots=True, order=True)
class SemanticVersion:
    """
    Immutable semantic version.

    Format:

        MAJOR.MINOR.PATCH

    Example:

        0.1.0
    """

    major: int
    minor: int
    patch: int

    def __post_init__(self) -> None:
        """
        Validate version numbers.
        """

        values = {
            "major": self.major,
            "minor": self.minor,
            "patch": self.patch,
        }

        for name, value in values.items():
            if value < 0:
                raise ValueError(
                    f"{name} version component cannot be negative."
                )

    @property
    def value(self) -> str:
        """
        Return canonical version string.
        """

        return (
            f"{self.major}"
            f"{VERSION_SEPARATOR}"
            f"{self.minor}"
            f"{VERSION_SEPARATOR}"
            f"{self.patch}"
        )

    def __str__(self) -> str:
        return self.value


###############################################################################
# Build Information
###############################################################################


@dataclass(frozen=True, slots=True)
class BuildInfo:
    """
    Metadata describing a specific build artifact.
    """

    build_number: str
    commit_hash: str | None = None
    build_timestamp: str | None = None

    def __post_init__(self) -> None:
        if not self.build_number.strip():
            raise ValueError(
                "Build number cannot be empty."
            )


###############################################################################
# Release Information
###############################################################################


@dataclass(frozen=True, slots=True)
class ReleaseInfo:
    """
    Metadata describing an AEVON release.
    """

    version: SemanticVersion
    name: str
    build: BuildInfo | None = None
    description: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError(
                "Release name cannot be empty."
            )


###############################################################################
# Current Platform Version
###############################################################################

AEVON_VERSION = SemanticVersion(
    major=0,
    minor=1,
    patch=0,
)


###############################################################################
# Public API
###############################################################################

__all__ = [
    "SemanticVersion",
    "BuildInfo",
    "ReleaseInfo",
    "AEVON_VERSION",
]
