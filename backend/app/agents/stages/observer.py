"""
===============================================================================
SheetPilot AI

Module:
    Observer Stage

Version:
    0.1.0

Purpose:
    Observe the repository and return a RepositorySnapshot.
===============================================================================
"""

from __future__ import annotations

from app.intelligence.collector.repository_scanner import RepositoryScanner
from app.intelligence.contracts import RepositorySnapshot


class ObserverStage:
    """
    First stage of the Engineering Agent.

    Responsibility:
        Observe the repository.

    Future responsibilities:
        - Git status
        - Cached scans
        - Change detection
        - Project context loading
    """

    def __init__(self) -> None:
        self._scanner = RepositoryScanner()

    def run(self) -> RepositorySnapshot:
        """
        Observe the repository and return its snapshot.
        """
        return self._scanner.scan()
