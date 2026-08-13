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

from __future__ import annotations

from app.agents.contracts import (
    EngineerRequest,
    EngineerResponse,
)
from app.agents.stages import ObserverStage


class EngineeringAgent:
    """
    Main orchestrator for AEVON.

    Current Workflow

        Request
            ↓
        Observer Stage
            ↓
        Response

    Future

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

        self._observer = ObserverStage()

    def run(
        self,
        request: EngineerRequest,
    ) -> EngineerResponse:
        """
        Execute the engineering workflow.

        Version 0.1:
            Observe the repository.
        """

        snapshot = self._observer.run()

        return EngineerResponse(
            success=True,
            message="Repository observed successfully.",
            repository_scanned=True,
            total_files=snapshot.statistics.total_files,
            total_folders=snapshot.statistics.total_folders,
        )
