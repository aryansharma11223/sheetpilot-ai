"""
===============================================================================
AEVON

Module:
    Engineering Agent

Version:
    0.1.0

Purpose:
    Main entry point for all engineering workflows.

Engineering Standard:
    ES-008 - Stage Interface Standard
===============================================================================
"""

from app.agents.contracts import (
    EngineerRequest,
    EngineerResponse,
)
from app.agents.stages import ObserverStage
from app.context.contracts import ContextRequest
from app.context.engine.context_engine import ContextEngine


class EngineeringAgent:
    """
    Main orchestrator for AEVON.

    Current Workflow

        Request
            ↓
        Context Engine
            ↓
        Observer Stage
            ↓
        Response

    Future

        Context
            ↓
        Observer
            ↓
        Planner
            ↓
        Builder
            ↓
        Reviewer
            ↓
        Documenter
            ↓
        Learner
    """

    def __init__(self) -> None:

        self._context_engine = ContextEngine()
        self._observer = ObserverStage()

    def run(
        self,
        request: EngineerRequest,
    ) -> EngineerResponse:
        """
        Execute the engineering workflow.

        Version 0.1:
            Build context and observe the repository.
        """

        context_request = ContextRequest(
            prompt=request.prompt,
        )

        context = self._context_engine.run(
            context_request,
        )

        snapshot = self._observer.run()

        return EngineerResponse(
            success=True,
            message="Engineering context built and repository observed successfully.",
            repository_scanned=True,
            context_built=True,
            context_sources=context.source_count,
            total_files=snapshot.statistics.total_files,
            total_folders=snapshot.statistics.total_folders,
        )

    @property
    def context_engine(self) -> ContextEngine:
        """
        Return the Context Engine used by the agent.
        """

        return self._context_engine

    @property
    def observer(self) -> ObserverStage:
        """
        Return the repository observer.
        """

        return self._observer


__all__ = [
    "EngineeringAgent",
]
