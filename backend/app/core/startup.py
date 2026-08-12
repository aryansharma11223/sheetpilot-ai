"""
AEVON Platform
==============

Startup Lifecycle Framework

This module defines the startup lifecycle primitives used by AEVON.

Responsibilities:
- Represent startup states.
- Store startup context.
- Track startup lifecycle.

This module does NOT:
- Start the Kernel.
- Load modules.
- Register services.
- Manage runtime execution.

Those responsibilities belong to bootstrap and kernel layers.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

from app.core.metadata import PlatformMetadata, RuntimeMetadata
from app.core.version import SemanticVersion


###############################################################################
# Constants
###############################################################################

DEFAULT_STARTUP_ENVIRONMENT: Final[str] = "development"


###############################################################################
# Startup State
###############################################################################


class StartupState(str, Enum):
    """
    Represents AEVON startup lifecycle states.
    """

    CREATED = "created"
    INITIALIZING = "initializing"
    READY = "ready"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


###############################################################################
# Startup Context
###############################################################################


@dataclass(frozen=True, slots=True)
class StartupContext:
    """
    Immutable context available during startup.
    """

    platform: PlatformMetadata
    version: SemanticVersion
    runtime: RuntimeMetadata
    environment: str = DEFAULT_STARTUP_ENVIRONMENT

    def __post_init__(self) -> None:
        if not self.environment.strip():
            raise ValueError(
                "Startup environment cannot be empty."
            )


###############################################################################
# Startup Manager
###############################################################################


class StartupManager:
    """
    Controls startup lifecycle state transitions.
    """

    def __init__(
        self,
        context: StartupContext,
    ) -> None:

        self.context = context
        self._state = StartupState.CREATED

    @property
    def state(self) -> StartupState:
        """
        Current startup state.
        """

        return self._state

    def initialize(self) -> None:
        """
        Move startup lifecycle into initialization.
        """

        self._transition(
            StartupState.INITIALIZING
        )

    def mark_ready(self) -> None:
        """
        Mark platform as ready.
        """

        self._transition(
            StartupState.READY
        )

    def start(self) -> None:
        """
        Mark platform as running.
        """

        self._transition(
            StartupState.RUNNING
        )

    def stop(self) -> None:
        """
        Stop platform startup lifecycle.
        """

        self._transition(
            StartupState.STOPPING
        )

        self._transition(
            StartupState.STOPPED
        )

    def fail(self) -> None:
        """
        Mark startup as failed.
        """

        self._transition(
            StartupState.FAILED
        )

    def _transition(
        self,
        state: StartupState,
    ) -> None:
        """
        Update lifecycle state.
        """

        self._state = state


###############################################################################
# Public API
###############################################################################

__all__ = [
    "StartupState",
    "StartupContext",
    "StartupManager",
]
