"""
AEVON Kernel
============

Kernel Orchestration

This module provides the public Kernel orchestration object.

Responsibilities:
- Compose the Kernel's internal subsystems.
- Provide a single public entry point to Kernel infrastructure.
- Provide high-level lifecycle operations.
- Expose lifecycle, registry, dependency validation,
  startup, event, and health capabilities.
- Keep subsystem ownership centralized.

The Kernel does NOT:
- Implement lifecycle state transitions directly.
- Implement dependency validation directly.
- Implement event routing directly.
- Implement health evaluation directly.
- Execute business or intelligence logic.

Those responsibilities belong to the respective
Kernel internal subsystems.

Architecture:

    AEVON Kernel
         |
         +-- LifecycleManager
         +-- ComponentRegistry
         +-- DependencyValidator
         +-- StartupCoordinator
         +-- EventBus
         +-- HealthInspector
"""

from __future__ import annotations

from app.core.startup import StartupContext, StartupManager
from kernel.internal.dependency_validator import DependencyValidator
from kernel.internal.event_bus import EventBus
from kernel.internal.health import HealthInspector
from kernel.internal.lifecycle import LifecycleManager
from kernel.internal.registry import ComponentRegistry
from kernel.internal.startup import StartupCoordinator


###############################################################################
# Kernel
###############################################################################


class Kernel:
    """
    Central orchestration facade for the AEVON Kernel.

    The Kernel owns and composes the internal infrastructure
    required to initialize, validate, start, monitor, and stop
    the platform.

    Individual responsibilities remain delegated to their
    dedicated internal implementations.
    """

    def __init__(self, context: StartupContext) -> None:
        """
        Create a Kernel instance.

        Args:
            context:
                Core startup context describing the AEVON runtime.
        """

        # Core lifecycle authority.
        self._startup_manager = StartupManager(context)

        # Kernel lifecycle boundary.
        self._lifecycle = LifecycleManager(
            self._startup_manager
        )

        # Component ownership and lookup.
        self._registry = ComponentRegistry()

        # Dependency validation.
        self._dependency_validator = DependencyValidator()

        # Internal event delivery.
        self._event_bus = EventBus()

        # Read-only health inspection.
        self._health = HealthInspector(
            self._startup_manager
        )

        # Startup orchestration.
        self._startup = StartupCoordinator(
            lifecycle=self._lifecycle,
            registry=self._registry,
            dependency_validator=self._dependency_validator,
        )

    ###########################################################################
    # High-Level Lifecycle
    ###########################################################################

    def initialize(self) -> None:
        """
        Initialize the Kernel.

        Startup coordination is delegated to the internal
        StartupCoordinator.

        The Kernel reaches READY only after successful dependency
        validation.
        """

        self._startup.initialize()

    def start(self) -> None:
        """
        Start the Kernel.

        The Kernel must already be READY before it can start.
        """

        self._startup.start()

    def stop(self) -> None:
        """
        Stop the Kernel.

        Lifecycle transition handling remains delegated to the
        internal lifecycle subsystem.
        """

        self._startup.stop()

    ###########################################################################
    # Lifecycle
    ###########################################################################

    @property
    def lifecycle(self) -> LifecycleManager:
        """
        Return the Kernel lifecycle manager.
        """

        return self._lifecycle

    ###########################################################################
    # Registry
    ###########################################################################

    @property
    def registry(self) -> ComponentRegistry:
        """
        Return the Kernel component registry.
        """

        return self._registry

    ###########################################################################
    # Dependency Validation
    ###########################################################################

    @property
    def dependency_validator(self) -> DependencyValidator:
        """
        Return the Kernel dependency validator.
        """

        return self._dependency_validator

    ###########################################################################
    # Startup
    ###########################################################################

    @property
    def startup(self) -> StartupCoordinator:
        """
        Return the Kernel startup coordinator.
        """

        return self._startup

    ###########################################################################
    # Events
    ###########################################################################

    @property
    def event_bus(self) -> EventBus:
        """
        Return the Kernel event bus.
        """

        return self._event_bus

    ###########################################################################
    # Health
    ###########################################################################

    @property
    def health(self) -> HealthInspector:
        """
        Return the Kernel health inspector.
        """

        return self._health


###############################################################################
# Public API
###############################################################################


__all__ = [
    "Kernel",
]
