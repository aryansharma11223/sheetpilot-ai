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
- Keep health inspection read-only and deterministic.

The health implementation does NOT:
- Control lifecycle.
- Start or stop the Kernel.
- Register components.
- Resolve dependencies.
- Perform recovery.
- Publish events.
- Execute business logic.
- Execute intelligence logic.

The Core StartupManager remains the authoritative source
for the Kernel lifecycle state.
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

    Health is currently derived exclusively from the authoritative
    Core lifecycle state.

    Healthy states:

        READY
        RUNNING

    All other lifecycle states are considered unhealthy at the
    current Kernel foundation stage.
    """

    _HEALTHY_STATES = frozenset(
        {
            StartupState.READY,
            StartupState.RUNNING,
        }
    )

    def __init__(
        self,
        startup_manager: StartupManager,
    ) -> None:
        """
        Initialize the health inspector.

        Args:
            startup_manager:
                Core startup manager that owns the authoritative
                lifecycle state.
        """

        self._startup_manager = startup_manager

    ###########################################################################
    # Health Evaluation
    ###########################################################################

    def is_healthy(self) -> bool:
        """
        Return whether the Kernel is currently healthy.

        READY and RUNNING represent healthy Kernel states.

        All other lifecycle states are considered unhealthy
        at this foundation stage.
        """

        return self._startup_manager.state in self._HEALTHY_STATES

    ###########################################################################
    # Health Status
    ###########################################################################

    def status(self) -> dict[str, Any]:
        """
        Return the current structured Kernel health status.

        The returned structure contains:

            healthy:
                Boolean health result.

            state:
                Canonical lifecycle state value.

        The status is derived from the same authoritative lifecycle
        state used by ``is_healthy()``.
        """

        state = self._startup_manager.state

        return {
            "healthy": state in self._HEALTHY_STATES,
            "state": state.value,
        }


###############################################################################
# Public API
###############################################################################


__all__ = [
    "HealthInspector",
]
