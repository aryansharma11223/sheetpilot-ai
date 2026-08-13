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
- Isolate handler failures from other subscribers.
- Prevent mutation of the internal handler collection by callers.

The event bus does NOT:
- Implement business logic.
- Implement intelligence logic.
- Persist events.
- Queue events.
- Execute events asynchronously.
- Route events across processes or machines.
- Perform lifecycle management.

Those responsibilities belong to their respective
platform layers.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from typing import Any

from kernel.interfaces import EventHandler, KernelEventBus


###############################################################################
# Event Bus
###############################################################################


class EventBus(KernelEventBus):
    """
    In-process implementation of the Kernel event bus.

    Events are routed by their exact concrete Python type.

    Delivery is synchronous and deterministic:

        publish(event)
            |
            +--> handler 1
            +--> handler 2
            +--> handler 3

    A failure in one handler does not prevent other subscribed
    handlers from receiving the event.
    """

    def __init__(self) -> None:
        """
        Initialize an empty event bus.
        """

        self._handlers: dict[
            type[Any],
            list[EventHandler],
        ] = defaultdict(list)

    ###########################################################################
    # Subscription
    ###########################################################################

    def subscribe(
        self,
        event_type: type[Any],
        handler: EventHandler,
    ) -> None:
        """
        Subscribe a handler to an event type.

        Duplicate subscriptions of the same handler for the same
        event type are ignored.

        Args:
            event_type:
                Concrete event type to receive.

            handler:
                Callable receiving the published event.
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

        Missing event types and missing subscriptions are ignored.

        Args:
            event_type:
                Event type from which the handler should be removed.

            handler:
                Previously subscribed handler.
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

    ###########################################################################
    # Publication
    ###########################################################################

    def publish(self, event: Any) -> None:
        """
        Publish an event to all handlers registered for its exact type.

        Handler execution is synchronous and follows subscription order.

        A failure in one handler does not prevent subsequent handlers
        from receiving the event.

        The handler collection is snapshotted before delivery so that
        subscription changes performed during event handling do not
        modify the current delivery cycle.
        """

        event_type = type(event)

        handlers = tuple(
            self._handlers.get(event_type, ())
        )

        for handler in handlers:
            try:
                handler(event)
            except Exception:
                # Event isolation is intentional at the Kernel boundary.
                # One faulty subscriber must not prevent other subscribers
                # from receiving the same event.
                continue

    ###########################################################################
    # Inspection
    ###########################################################################

    def handlers_for(
        self,
        event_type: type[Any],
    ) -> Iterable[EventHandler]:
        """
        Return a read-only snapshot of handlers registered for an event type.

        This method is intended for infrastructure inspection and
        behavioral validation. The returned tuple cannot mutate the
        Event Bus's internal handler collection.
        """

        return tuple(
            self._handlers.get(event_type, ())
        )

    def has_handlers(
        self,
        event_type: type[Any],
    ) -> bool:
        """
        Return whether at least one handler is registered for an event type.
        """

        return bool(
            self._handlers.get(event_type)
        )


###############################################################################
# Public API
###############################################################################

__all__ = [
    "EventBus",
]
