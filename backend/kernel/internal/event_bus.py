"""
AEVON Kernel
============

Internal Kernel Event Bus

This module provides the internal implementation of the
Kernel event bus contract.

Responsibilities:
- Register event handlers.
- Remove event handlers.
- Publish events to matching handlers.
- Keep event delivery deterministic and in-process.

The event bus contains no business or intelligence logic.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from kernel.interfaces import EventHandler, KernelEventBus


###############################################################################
# Event Bus
###############################################################################


class EventBus(KernelEventBus):
    """
    In-process implementation of the Kernel event bus.

    Events are routed by their concrete Python type.
    """

    def __init__(self) -> None:
        self._handlers: dict[type[Any], list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_type: type[Any],
        handler: EventHandler,
    ) -> None:
        """
        Subscribe a handler to an event type.

        Duplicate subscriptions of the same handler for the same
        event type are ignored.
        """
        handlers = self._handlers[event_type]

        if handler not in handlers:
            handlers.append(handler)

    def unsubscribe(
        self,
        event_type: type[Any],
        handler: EventHandler,
    ) -> None:
        """
        Remove a handler from an event type.

        Missing subscriptions are ignored.
        """
        handlers = self._handlers.get(event_type)

        if not handlers:
            return

        try:
            handlers.remove(handler)
        except ValueError:
            return

        if not handlers:
            del self._handlers[event_type]

    def publish(self, event: Any) -> None:
        """
        Publish an event to all handlers registered for its exact type.

        A failure in one handler does not prevent subsequent handlers
        from receiving the event.
        """
        event_type = type(event)
        handlers = tuple(self._handlers.get(event_type, ()))

        for handler in handlers:
            try:
                handler(event)
            except Exception:
                continue


###############################################################################
# Public API
###############################################################################

__all__ = [
    "EventBus",
]
