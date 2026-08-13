"""
AEVON Kernel
============

Kernel Bootstrap

This module provides the controlled entry point for constructing
and starting the AEVON Kernel.

Responsibilities:
- Collect the initial runtime context.
- Construct the Core StartupContext.
- Construct the Kernel.
- Coordinate the initial Kernel startup sequence.

Bootstrap does NOT:
- Implement lifecycle state transitions.
- Register Kernel components directly.
- Validate dependencies directly.
- Implement event routing.
- Implement health evaluation.
- Execute business or intelligence logic.

Those responsibilities belong to the Core and Kernel layers.

Architecture:

    Bootstrap
        ?
    StartupContext
        ?
    Kernel
        ?
    Kernel Startup Coordinator
        ?
    Kernel Subsystems
"""

from __future__ import annotations

import platform

from app.core.metadata import (
    PlatformMetadata,
    RuntimeMetadata,
)
from app.core.startup import StartupContext
from app.core.version import AEVON_VERSION
from kernel.kernel import Kernel


###############################################################################
# Bootstrap
###############################################################################


def create_startup_context() -> StartupContext:
    """
    Create the initial AEVON startup context.

    Runtime information is collected here because Bootstrap
    is responsible for preparing the environment required by
    the Kernel.

    Returns:
        A fully initialized StartupContext.
    """

    return StartupContext(
        platform=PlatformMetadata(
            name="AEVON",
            version=str(AEVON_VERSION),
        ),
        version=AEVON_VERSION,
        runtime=RuntimeMetadata(
            python_version=platform.python_version(),
            operating_system=platform.system(),
            environment="development",
        ),
    )


def create_kernel(
    context: StartupContext | None = None,
) -> Kernel:
    """
    Construct an AEVON Kernel.

    Args:
        context:
            Optional startup context. If omitted, Bootstrap creates
            the default runtime context.

    Returns:
        A constructed Kernel in the CREATED lifecycle state.
    """

    if context is None:
        context = create_startup_context()

    return Kernel(context)


def bootstrap_kernel(
    context: StartupContext | None = None,
) -> Kernel:
    """
    Construct and initialize the AEVON Kernel.

    The Kernel is returned after successful initialization and
    dependency validation.

    Args:
        context:
            Optional startup context. If omitted, Bootstrap creates
            the default runtime context.

    Returns:
        An initialized Kernel in the READY lifecycle state.

    Raises:
        ValueError:
            If Kernel dependency validation fails.
    """

    kernel = create_kernel(context)

    kernel.startup.initialize()

    return kernel


###############################################################################
# Public API
###############################################################################


__all__ = [
    "create_startup_context",
    "create_kernel",
    "bootstrap_kernel",
]
