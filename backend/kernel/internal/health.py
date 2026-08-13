"""
AEVON Kernel
============

Internal Kernel Health

This module provides the internal implementation of the
Kernel health inspection contract.

Responsibilities:
- Inspect the current Kernel lifecycle state.
- Determine whether the Kernel is healthy.
- Expose a structured health status.

The health implementation is read-only.
It does not control lifecycle, register components,
perform recovery, or execute business logic.
"""

from __future__ import annotations

from typing import Any

from app.core.startup import StartupManager, StartupState
from kernel.interfaces import KernelHealth


###############################################################################
# Health Inspector
###############################################################################


class HealthInspector(KernelHealth):
    """
    Read-only implementation of the Kernel health contract.

    The Core StartupManager remains the authoritative source
    for the Kernel lifecycle state.
    """

    def __init__(self, startup_manager: StartupManager) -> None:
        self._startup_manager = startup_manager

    def is_healthy(self) -> bool:
        """
        Return whether the Kernel is currently healthy.

        READY and RUNNING represent healthy Kernel states.
        All other lifecycle states are considered unhealthy
        at this foundation stage.
        """
        return self._startup_manager.state in (
            StartupState.READY,
            StartupState.RUNNING,
        )

    def status(self) -> dict[str, Any]:
        """
        Return the current structured Kernel health status.
        """
        state = self._startup_manager.state

        return {
            "healthy": state in (
                StartupState.READY,
                StartupState.RUNNING,
            ),
            "state": state.value,
        }


###############################################################################
# Public API
###############################################################################


__all__ = [
    "HealthInspector",
]
