"""
===============================================================================
AEVON Platform

Module:
    Kernel Verifier

Purpose:
    Verifies the public AEVON Kernel foundation.

The verifier exercises the Kernel through its public orchestration
interfaces and confirms:

- Kernel construction.
- Kernel initialization.
- Dependency validation during initialization.
- Kernel start.
- Kernel health.
- Kernel event bus availability.
- Kernel registry availability.
- Kernel dependency validator availability.
- Kernel shutdown.
- Lifecycle state transitions.
- Bootstrap behavior.

The verifier does not inspect private Kernel implementation details.
===============================================================================
"""

from __future__ import annotations

import time

from app.core.startup import StartupState
from app.verification.contracts import (
    VerificationResult,
    VerificationStatus,
)
from kernel.bootstrap import (
    bootstrap_kernel,
    create_kernel,
    create_startup_context,
)

from .base_verifier import BaseVerifier


class KernelVerifier(BaseVerifier):
    """
    Verifies the AEVON Kernel subsystem.
    """

    @property
    def name(self) -> str:
        return "Kernel"

    def run(self) -> VerificationResult:
        start = time.perf_counter()

        messages: list[str] = []
        errors: list[str] = []

        try:
            # -----------------------------------------------------------------
            # Startup Context
            # -----------------------------------------------------------------

            context = create_startup_context()

            if context.platform.name != "AEVON":
                raise AssertionError(
                    "Kernel startup context platform name is invalid."
                )

            if str(context.version) != "0.1.0":
                raise AssertionError(
                    "Kernel startup context version is invalid."
                )

            if not context.runtime.python_version:
                raise AssertionError(
                    "Kernel runtime Python version is missing."
                )

            if not context.runtime.operating_system:
                raise AssertionError(
                    "Kernel runtime operating system is missing."
                )

            messages.append("Startup context created.")

            # -----------------------------------------------------------------
            # Kernel Construction
            # -----------------------------------------------------------------

            kernel = create_kernel(context)

            if kernel.lifecycle.state != StartupState.CREATED:
                raise AssertionError(
                    "Kernel did not begin in CREATED state."
                )

            messages.append("Kernel constructed in CREATED state.")

            # -----------------------------------------------------------------
            # Public Subsystem Exposure
            # -----------------------------------------------------------------

            if kernel.registry is None:
                raise AssertionError(
                    "Kernel registry is unavailable."
                )

            if kernel.dependency_validator is None:
                raise AssertionError(
                    "Kernel dependency validator is unavailable."
                )

            if kernel.startup is None:
                raise AssertionError(
                    "Kernel startup coordinator is unavailable."
                )

            if kernel.event_bus is None:
                raise AssertionError(
                    "Kernel event bus is unavailable."
                )

            if kernel.health is None:
                raise AssertionError(
                    "Kernel health inspector is unavailable."
                )

            messages.append("Kernel subsystems exposed successfully.")

            # -----------------------------------------------------------------
            # Initialization
            # -----------------------------------------------------------------

            kernel.initialize()

            if kernel.lifecycle.state != StartupState.READY:
                raise AssertionError(
                    "Kernel did not reach READY state after initialization."
                )

            messages.append(
                "Kernel initialized and dependency validation passed."
            )

            # -----------------------------------------------------------------
            # Health Before Start
            # -----------------------------------------------------------------

            health_before_start = kernel.health.status()

            if health_before_start["healthy"] is not True:
                raise AssertionError(
                    "Kernel should be healthy in READY state."
                )

            if health_before_start["state"] != StartupState.READY.value:
                raise AssertionError(
                    "Kernel health state does not match READY state."
                )

            messages.append("Kernel health inspection passed in READY state.")

            # -----------------------------------------------------------------
            # Start
            # -----------------------------------------------------------------

            kernel.start()

            if kernel.lifecycle.state != StartupState.RUNNING:
                raise AssertionError(
                    "Kernel did not reach RUNNING state after start."
                )

            messages.append("Kernel started successfully.")

            # -----------------------------------------------------------------
            # Health While Running
            # -----------------------------------------------------------------

            health_running = kernel.health.status()

            if health_running["healthy"] is not True:
                raise AssertionError(
                    "Kernel should be healthy in RUNNING state."
                )

            if health_running["state"] != StartupState.RUNNING.value:
                raise AssertionError(
                    "Kernel health state does not match RUNNING state."
                )

            if not kernel.health.is_healthy():
                raise AssertionError(
                    "Kernel health inspector reported an unhealthy running Kernel."
                )

            messages.append("Kernel health inspection passed in RUNNING state.")

            # -----------------------------------------------------------------
            # Event Bus
            # -----------------------------------------------------------------

            received: list[object] = []

            def handler(event: object) -> None:
                received.append(event)

            event = object()

            kernel.event_bus.subscribe(type(event), handler)
            kernel.event_bus.publish(event)
            kernel.event_bus.unsubscribe(type(event), handler)

            if received != [event]:
                raise AssertionError(
                    "Kernel event bus failed public publish/subscribe behavior."
                )

            messages.append("Kernel event bus integration passed.")

            # -----------------------------------------------------------------
            # Shutdown
            # -----------------------------------------------------------------

            kernel.stop()

            if kernel.lifecycle.state != StartupState.STOPPED:
                raise AssertionError(
                    "Kernel did not reach STOPPED state after shutdown."
                )

            messages.append("Kernel stopped successfully.")

            # -----------------------------------------------------------------
            # Bootstrap
            # -----------------------------------------------------------------

            bootstrapped_kernel = bootstrap_kernel()

            if (
                bootstrapped_kernel.lifecycle.state
                != StartupState.READY
            ):
                raise AssertionError(
                    "Kernel bootstrap did not produce READY state."
                )

            if bootstrapped_kernel.lifecycle.state == StartupState.RUNNING:
                raise AssertionError(
                    "Kernel bootstrap must not start the Kernel automatically."
                )

            messages.append(
                "Kernel bootstrap integration passed."
            )

            status = VerificationStatus.PASS

        except Exception as ex:
            status = VerificationStatus.FAIL
            errors.append(str(ex))

        duration = time.perf_counter() - start

        return VerificationResult(
            subsystem=self.name,
            status=status,
            duration_seconds=duration,
            messages=messages,
            errors=errors,
        )


__all__ = [
    "KernelVerifier",
]
