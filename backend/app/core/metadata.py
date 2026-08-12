"""
AEVON Platform
==============

Core Metadata Framework

This module defines immutable metadata models used throughout AEVON.

Responsibilities:
- Define platform identity.
- Define component identity.
- Define module metadata.
- Define runtime metadata.

This module does NOT:
- Collect runtime information.
- Read configuration.
- Access environment variables.
- Perform validation against external systems.

It only represents metadata.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


###############################################################################
# Constants
###############################################################################

METADATA_SEPARATOR: Final[str] = "."


###############################################################################
# Metadata Identifier
###############################################################################


@dataclass(frozen=True, slots=True)
class MetadataId:
    """
    Immutable AEVON metadata identifier.

    Format:

        namespace.component

    Example:

        aeon.kernel
    """

    namespace: str
    component: str

    def __post_init__(self) -> None:
        namespace = self.namespace.strip().lower()
        component = self.component.strip().lower()

        if not namespace:
            raise ValueError("Metadata namespace cannot be empty.")

        if not component:
            raise ValueError("Metadata component cannot be empty.")

        object.__setattr__(self, "namespace", namespace)
        object.__setattr__(self, "component", component)

    @property
    def value(self) -> str:
        """
        Return canonical metadata identifier.
        """

        return (
            f"{self.namespace}"
            f"{METADATA_SEPARATOR}"
            f"{self.component}"
        )

    def __str__(self) -> str:
        return self.value


def create_metadata_id(
    namespace: str,
    component: str,
) -> MetadataId:
    """
    Create a metadata identifier.

    Example:

        create_metadata_id(
            "aeon",
            "kernel",
        )

    Returns:

        aeon.kernel
    """

    return MetadataId(
        namespace=namespace,
        component=component,
    )


###############################################################################
# Component Metadata
###############################################################################


@dataclass(frozen=True, slots=True)
class ComponentMetadata:
    """
    Generic metadata representation for any AEVON component.
    """

    identifier: MetadataId
    name: str
    version: str
    description: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Component name cannot be empty.")

        if not self.version.strip():
            raise ValueError("Component version cannot be empty.")


###############################################################################
# Module Metadata
###############################################################################


@dataclass(frozen=True, slots=True)
class ModuleMetadata(ComponentMetadata):
    """
    Metadata representation for a platform module.

    Examples:

        aeon.kernel
        aeon.memory
        aeon.knowledge
    """

    author: str = ""
    enabled: bool = True


###############################################################################
# Platform Metadata
###############################################################################


@dataclass(frozen=True, slots=True)
class PlatformMetadata:
    """
    Metadata describing the AEVON platform itself.
    """

    name: str
    version: str
    description: str = ""

    namespace: str = "aeon"

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Platform name cannot be empty.")

        if not self.version.strip():
            raise ValueError("Platform version cannot be empty.")


###############################################################################
# Runtime Metadata
###############################################################################


@dataclass(frozen=True, slots=True)
class RuntimeMetadata:
    """
    Metadata describing the runtime environment.
    """

    python_version: str
    operating_system: str
    environment: str

    def __post_init__(self) -> None:
        if not self.python_version.strip():
            raise ValueError(
                "Python version cannot be empty."
            )

        if not self.operating_system.strip():
            raise ValueError(
                "Operating system cannot be empty."
            )

        if not self.environment.strip():
            raise ValueError(
                "Runtime environment cannot be empty."
            )


###############################################################################
# Public API
###############################################################################


__all__ = [
    "MetadataId",
    "create_metadata_id",
    "ComponentMetadata",
    "ModuleMetadata",
    "PlatformMetadata",
    "RuntimeMetadata",
]
