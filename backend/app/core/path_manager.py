"""
===============================================================================
AEVON

Path Manager
===============================================================================
"""

from __future__ import annotations

from pathlib import Path


class PathManager:
    """
    Central location for all AEVON paths.
    """

    _WORKSPACE = Path(".AEVON")

    @classmethod
    def workspace(cls) -> Path:
        """
        Root AEVON workspace.
        """
        cls._WORKSPACE.mkdir(
            parents=True,
            exist_ok=True,
        )
        return cls._WORKSPACE

    @classmethod
    def knowledge_directory(cls) -> Path:
        """
        Workspace knowledge directory.
        """
        path = cls.workspace() / "knowledge"
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    @classmethod
    def knowledge_cache(cls) -> Path:
        """
        Knowledge repository cache file.
        """
        return cls.knowledge_directory() / "repository.json"

    @classmethod
    def cache_directory(cls) -> Path:
        path = cls.workspace() / "cache"
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    @classmethod
    def logs_directory(cls) -> Path:
        path = cls.workspace() / "logs"
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    @classmethod
    def memory_directory(cls) -> Path:
        path = cls.workspace() / "memory"
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    @classmethod
    def sessions_directory(cls) -> Path:
        path = cls.workspace() / "sessions"
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path
