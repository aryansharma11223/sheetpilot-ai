"""
AEVON Kernel
============

Kernel Interfaces

This module defines the contracts used by the AEVON Kernel.

Responsibilities:
- Define the lifecycle contract for Kernel components.
- Define the component registry contract.
- Define the event bus contract.
- Define the health inspection contract.

This module contains interfaces only.
Concrete implementations belong to the Kernel internal layer.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Iterable

from app.core.metadata import ComponentMetadata
from app.core.startup import StartupState


###############################################################################
# Kernel Component
###############################################################################


class KernelComponent(ABC):
    """
    Base contract for a component managed by the AEVON Kernel.
    """

    @property
    @abstractmethod
    def metadata(self) -> ComponentMetadata:
        """Return component metadata."""
        raise NotImplementedError

    @property
    @abstractmethod
    def state(self) -> StartupState:
        """Return the current component lifecycle state."""
        raise NotImplementedError

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the component."""
        raise NotImplementedError

    @abstractmethod
    def start(self) -> None:
        """Start the component."""
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """Stop the component."""
        raise NotImplementedError


###############################################################################
# Kernel Registry
###############################################################################


class KernelRegistry(ABC):
    """
    Contract for registering and resolving Kernel components.
    """

    @abstractmethod
    def register(self, component: KernelComponent) -> None:
        """Register a Kernel component."""
        raise NotImplementedError

    @abstractmethod
    def unregister(self, identifier: str) -> None:
        """Remove a registered component."""
        raise NotImplementedError

    @abstractmethod
    def get(self, identifier: str) -> KernelComponent | None:
        """Return a component by identifier."""
        raise NotImplementedError

    @abstractmethod
    def contains(self, identifier: str) -> bool:
        """Return whether a component is registered."""
        raise NotImplementedError

    @abstractmethod
    def all(self) -> Iterable[KernelComponent]:
        """Return all registered components."""
        raise NotImplementedError


###############################################################################
# Kernel Lifecycle
###############################################################################


class KernelLifecycle(ABC):
    """
    Contract for controlling Kernel lifecycle.
    """

    @property
    @abstractmethod
    def state(self) -> StartupState:
        """Return the current Kernel state."""
        raise NotImplementedError

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the Kernel."""
        raise NotImplementedError

    @abstractmethod
    def start(self) -> None:
        """Start the Kernel."""
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """Stop the Kernel."""
        raise NotImplementedError


###############################################################################
# Kernel Event Bus
###############################################################################


EventHandler = Callable[[Any], None]


class KernelEventBus(ABC):
    """
    Contract for Kernel event publication and subscription.
    """

    @abstractmethod
    def subscribe(
        self,
        event_type: type[Any],
        handler: EventHandler,
    ) -> None:
        """Subscribe a handler to an event type."""
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(
        self,
        event_type: type[Any],
        handler: EventHandler,
    ) -> None:
        """Remove a handler from an event type."""
        raise NotImplementedError

    @abstractmethod
    def publish(self, event: Any) -> None:
        """Publish an event to subscribed handlers."""
        raise NotImplementedError


###############################################################################
# Kernel Health
###############################################################################


class KernelHealth(ABC):
    """
    Contract for inspecting Kernel health.
    """

    @abstractmethod
    def is_healthy(self) -> bool:
        """Return whether the Kernel is healthy."""
        raise NotImplementedError

    @abstractmethod
    def status(self) -> dict[str, Any]:
        """Return a structured health status."""
        raise NotImplementedError


###############################################################################
# Public API
###############################################################################


__all__ = [
    "EventHandler",
    "KernelComponent",
    "KernelRegistry",
    "KernelLifecycle",
    "KernelEventBus",
    "KernelHealth",
]
