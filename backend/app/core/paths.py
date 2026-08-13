"""
===============================================================================

AEVON

Capability : CORE-003
Module     : Path Manager
Version    : 0.1.0
Status     : Development

Description
-----------
Centralized path management for the AEVON platform.

===============================================================================
"""

from __future__ import annotations

from functools import cached_property
from pathlib import Path


class PathManager:
    """Centralized project path manager."""

    def __init__(self) -> None:
        # backend/app/core/paths.py -> backend/
        self._backend_root = Path(__file__).resolve().parents[2]

        # backend/ -> project root
        self._project_root = self._backend_root.parent

    @property
    def project_root(self) -> Path:
        return self._project_root

    @property
    def backend(self) -> Path:
        return self._backend_root

    @property
    def app(self) -> Path:
        return self.backend / "app"

    @property
    def scripts(self) -> Path:
        return self.backend / "scripts"

    @property
    def docs(self) -> Path:
        return self.project_root / "docs"

    @cached_property
    def logs(self) -> Path:
        return self._ensure(self.backend / "logs")

    @cached_property
    def memory(self) -> Path:
        return self._ensure(self.backend / "memory")

    @cached_property
    def cache(self) -> Path:
        return self._ensure(self.backend / "cache")

    @cached_property
    def temp(self) -> Path:
        return self._ensure(self.backend / "temp")

    @cached_property
    def exports(self) -> Path:
        return self._ensure(self.backend / "exports")

    @cached_property
    def imports(self) -> Path:
        return self._ensure(self.backend / "imports")

    @property
    def tests(self) -> Path:
        return self.backend / "tests"

    @property
    def ai_context(self) -> Path:
        return self.project_root / "AI_CONTEXT"

    @staticmethod
    def _ensure(path: Path) -> Path:
        """Create directory if it does not already exist."""
        path.mkdir(parents=True, exist_ok=True)
        return path


paths = PathManager()
