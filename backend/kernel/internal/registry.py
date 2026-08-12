"""
AEVON Kernel
============

Internal Component Registry

This module provides the internal implementation of the Kernel
component registry.

Responsibilities:
- Register Kernel components.
- Resolve registered components.
- Remove registered components.
- Determine whether components are registered.
- Expose registered components safely.

The registry is an internal Kernel implementation and should not
contain Kernel orchestration logic.
"""

from __future__ import annotations

from typing import Iterable

from kernel.interfaces import KernelComponent, KernelRegistry


###############################################################################
# Component Registry
###############################################################################


class ComponentRegistry(KernelRegistry):
    """
    In-memory registry for Kernel components.

    Components are indexed by their canonical metadata identifier,
    such as ``aeon.kernel``.
    """

    def __init__(self) -> None:
        self._components: dict[str, KernelComponent] = {}

    def register(self, component: KernelComponent) -> None:
        """
        Register a Kernel component.

        Raises:
            ValueError: If a component with the same identifier
                is already registered.
        """

        identifier = component.metadata.identifier.value

        if identifier in self._components:
            raise ValueError(
                f"Kernel component is already registered: {identifier}"
            )

        self._components[identifier] = component

    def unregister(self, identifier: str) -> None:
        """
        Remove a registered Kernel component.

        Raises:
            KeyError: If the identifier is not registered.
        """

        if identifier not in self._components:
            raise KeyError(
                f"Kernel component is not registered: {identifier}"
            )

        del self._components[identifier]

    def get(self, identifier: str) -> KernelComponent | None:
        """
        Return a registered component by identifier.

        Returns:
            The registered component, or ``None`` when not found.
        """

        return self._components.get(identifier)

    def contains(self, identifier: str) -> bool:
        """
        Return whether a component is registered.
        """

        return identifier in self._components

    def all(self) -> Iterable[KernelComponent]:
        """
        Return all registered components.

        A tuple is returned so callers cannot mutate the
        registry's internal collection.
        """

        return tuple(self._components.values())


###############################################################################
# Public API
###############################################################################


__all__ = [
    "ComponentRegistry",
]
