"""
AEVON Platform
==============

Application Entry Point

This module provides the top-level AEVON application entry point.

Responsibilities:
- Create the FastAPI application.
- Bootstrap the AEVON Kernel.
- Start the Kernel when the application starts.
- Stop the Kernel when the application shuts down.
- Expose application-level health information.

Architecture:

    FastAPI Application
            |
            v
    AEVON Kernel Bootstrap
            |
            v
        AEVON Kernel
            |
            +-- Lifecycle
            +-- Registry
            +-- Dependency Validator
            +-- Startup Coordinator
            +-- Event Bus
            +-- Health Inspector

This module does NOT:
- Implement Kernel lifecycle logic.
- Validate Kernel dependencies.
- Implement event routing.
- Implement health evaluation.
- Execute business or intelligence logic.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from kernel.bootstrap import create_kernel
from kernel.kernel import Kernel


###############################################################################
# Application State
###############################################################################


class Application:
    """
    Runtime container for the AEVON application.

    The application owns the Kernel instance while delegating
    all Kernel responsibilities to the Kernel itself.
    """

    def __init__(self) -> None:
        self._kernel: Kernel | None = None

    @property
    def kernel(self) -> Kernel:
        """
        Return the active Kernel.

        Raises:
            RuntimeError:
                If the Kernel has not been initialized.
        """

        if self._kernel is None:
            raise RuntimeError(
                "AEVON Kernel has not been initialized."
            )

        return self._kernel

    def initialize(self) -> None:
        """
        Construct and initialize the AEVON Kernel.

        The Kernel reaches READY only after its startup
        coordinator successfully completes dependency validation.
        """

        if self._kernel is not None:
            return

        kernel = create_kernel()

        kernel.initialize()

        self._kernel = kernel

    def start(self) -> None:
        """
        Start the initialized AEVON Kernel.
        """

        self.kernel.start()

    def stop(self) -> None:
        """
        Stop the AEVON Kernel if it is active.
        """

        if self._kernel is None:
            return

        self._kernel.stop()


###############################################################################
# Application Lifecycle
###############################################################################


application = Application()


@asynccontextmanager
async def lifespan(
    _: FastAPI,
) -> AsyncIterator[None]:
    """
    Manage the AEVON application lifecycle.

    Startup:
        Construct Kernel -> initialize Kernel -> READY
        -> start Kernel -> RUNNING

    Shutdown:
        Stop Kernel -> STOPPED
    """

    application.initialize()
    application.start()

    try:
        yield
    finally:
        application.stop()


###############################################################################
# FastAPI Application
###############################################################################


app = FastAPI(
    title="AEVON",
    version="0.1.0",
    lifespan=lifespan,
)


###############################################################################
# Routes
###############################################################################


@app.get("/")
def home() -> dict[str, str]:
    """
    Return the AEVON application identity.
    """

    return {
        "message": "Welcome to AEVON",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, object]:
    """
    Return Kernel-backed application health.
    """

    return application.kernel.health.status()


###############################################################################
# Public API
###############################################################################


__all__ = [
    "app",
    "application",
    "lifespan",
]
