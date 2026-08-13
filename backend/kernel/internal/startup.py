"""
AEVON Kernel
============

Internal Kernel Startup Coordinator

This module provides the internal implementation of the Kernel
startup coordination layer.

Responsibilities:
- Coordinate the Kernel startup sequence.
- Initialize the Kernel lifecycle.
- Validate registered component dependencies.
- Mark the platform ready only after validation succeeds.
- Start the Kernel after successful initialization.
- Stop the Kernel through the lifecycle boundary.
- Fail the startup lifecycle when coordination fails.

The startup coordinator does NOT:
- Define lifecycle states.
- Implement component registration.
- Implement dependency validation rules.
- Implement event subscription or dispatch.
- Perform health monitoring.
- Execute application or intelligence logic.

Those responsibilities belong to their respective Kernel
subsystems.
"""

from __future__ import annotations

from kernel.internal.dependency_validator import DependencyValidator
from kernel.internal.lifecycle import LifecycleManager
from kernel.internal.registry import ComponentRegistry


###############################################################################
# Startup Coordinator
###############################################################################


class StartupCoordinator:
    """
    Coordinates the Kernel startup lifecycle.

    The coordinator deliberately delegates responsibilities to the
    specialized Kernel subsystems instead of duplicating their logic.
    """

    def __init__(
        self,
        lifecycle: LifecycleManager,
        registry: ComponentRegistry,
        dependency_validator: DependencyValidator,
    ) -> None:
        """
        Initialize the startup coordinator.

        Args:
            lifecycle: Kernel lifecycle coordinator.
            registry: Kernel component registry.
            dependency_validator: Kernel dependency validator.
        """

        self._lifecycle = lifecycle
        self._registry = registry
        self._dependency_validator = dependency_validator

    @property
    def lifecycle(self) -> LifecycleManager:
        """
        Return the lifecycle coordinator.
        """

        return self._lifecycle

    @property
    def registry(self) -> ComponentRegistry:
        """
        Return the component registry.
        """

        return self._registry

    @property
    def dependency_validator(self) -> DependencyValidator:
        """
        Return the dependency validator.
        """

        return self._dependency_validator

    def initialize(self) -> None:
        """
        Initialize the Kernel startup lifecycle.

        Dependency validation is performed after entering the
        initialization state. The Kernel is marked ready only when
        dependency validation succeeds.

        Raises:
            ValueError: If dependency validation fails.
        """

        self._lifecycle.initialize()

        try:
            self._validate_dependencies()
            self._lifecycle.mark_ready()
        except Exception:
            self._lifecycle.fail()
            raise

    def start(self) -> None:
        """
        Start the Kernel after successful initialization.

        Raises:
            RuntimeError: If the Kernel is not ready.
        """

        if self._lifecycle.state.value != "ready":
            raise RuntimeError(
                "Kernel cannot start before it is ready."
            )

        self._lifecycle.start()

    def stop(self) -> None:
        """
        Stop the Kernel through the lifecycle boundary.
        """

        self._lifecycle.stop()

    def _validate_dependencies(self) -> None:
        """
        Validate dependencies declared by registered components.

        Every registered Kernel component is required to expose
        its dependencies through the formal KernelComponent
        dependency contract.
        """

        declarations = []

        for component in self._registry.all():
            declarations.extend(component.dependencies)

        self._dependency_validator.validate(declarations)


###############################################################################
# Public API
###############################################################################


__all__ = [
    "StartupCoordinator",
]
