"""
AEVON Kernel
============

Internal Kernel Lifecycle

This module provides the internal implementation of the
Kernel lifecycle contract.

Responsibilities:
- Coordinate Kernel lifecycle state transitions.
- Reuse the Core startup lifecycle primitives.
- Expose the current platform startup state.
- Enforce the Kernel lifecycle boundary.

The lifecycle implementation does NOT:
- Start the Kernel itself.
- Register components.
- Resolve dependencies.
- Dispatch events.
- Perform health monitoring.
- Execute business or intelligence logic.

Those responsibilities belong to their respective Kernel
subsystems.

Architecture:
    Core
        ↓
    StartupState / StartupContext / StartupManager
        ↓
    Kernel Lifecycle
        ↓
    Kernel / Bootstrap
"""

from __future__ import annotations

from app.core.startup import StartupManager, StartupState
from kernel.interfaces import KernelLifecycle


###############################################################################
# Lifecycle Manager
###############################################################################


class LifecycleManager(KernelLifecycle):
    """
    Internal implementation of the Kernel lifecycle contract.

    The Kernel lifecycle is deliberately built on top of the
    Core StartupManager rather than introducing a second,
    competing lifecycle state model.
    """

    def __init__(
        self,
        startup_manager: StartupManager,
    ) -> None:
        """
        Initialize the Kernel lifecycle coordinator.

        Args:
            startup_manager: Core lifecycle manager used as the
                authoritative source of startup state.
        """
        self._startup_manager = startup_manager

    @property
    def state(self) -> StartupState:
        """
        Return the current platform startup state.
        """
        return self._startup_manager.state

    @property
    def startup_manager(self) -> StartupManager:
        """
        Return the underlying Core startup manager.

        The Kernel owns orchestration, while Core remains the
        source of lifecycle primitives.
        """
        return self._startup_manager

    def initialize(self) -> None:
        """
        Move the platform into the initialization state.
        """
        self._startup_manager.initialize()

    def mark_ready(self) -> None:
        """
        Mark the platform as ready.

        Platform validation and dependency checks are expected
        to have succeeded before this method is called.
        """
        self._startup_manager.mark_ready()

    def start(self) -> None:
        """
        Mark the platform as running.
        """
        self._startup_manager.start()

    def stop(self) -> None:
        """
        Stop the platform lifecycle.

        Core owns the STOPPING → STOPPED transition.
        """
        self._startup_manager.stop()

    def fail(self) -> None:
        """
        Mark the platform lifecycle as failed.
        """
        self._startup_manager.fail()


###############################################################################
# Public API
###############################################################################

__all__ = [
    "LifecycleManager",
]
