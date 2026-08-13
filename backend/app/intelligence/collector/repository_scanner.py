"""
===============================================================================
AEVON

INT-001 : Repository Scanner
===============================================================================

Responsibility:
    Discover the repository structure and return a RepositorySnapshot.

This scanner DOES NOT:
    - Analyze dependencies
    - Detect technologies
    - Read file contents
    - Generate documentation

Those responsibilities belong to other Intelligence modules.
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from app.core.paths import paths
from app.intelligence.contracts import (
    FileInfo,
    FolderInfo,
    RepositorySnapshot,
)


class RepositoryScanner:
    """Scans the repository and returns a RepositorySnapshot."""

    IGNORE_DIRS = {
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".idea",
        ".vscode",
        "node_modules",
        "dist",
        "build",
    }

    IGNORE_FILES = {
        ".DS_Store",
    }

    def __init__(self, root: Path | None = None):
        self.root = Path(root) if root else paths.project_root

    def scan(self) -> RepositorySnapshot:
        snapshot = RepositorySnapshot(root=str(self.root))

        for item in self.root.rglob("*"):
            if self._should_ignore(item):
                continue

            relative_path = item.relative_to(self.root)

            if item.is_dir():
                snapshot.folders.append(
                    FolderInfo(
                        name=item.name,
                        relative_path=str(relative_path),
                        absolute_path=item,
                    )
                )

            elif item.is_file():
                extension = item.suffix.lower()

                snapshot.files.append(
                    FileInfo(
                        id=self._generate_file_id(relative_path),
                        name=item.name,
                        extension=extension,
                        relative_path=str(relative_path),
                        absolute_path=item,
                        size_bytes=item.stat().st_size,
                        is_python=extension == ".py",
                        is_hidden=item.name.startswith("."),
                    )
                )

        snapshot.statistics.total_files = len(snapshot.files)
        snapshot.statistics.total_folders = len(snapshot.folders)

        snapshot.statistics.python_files = sum(
            file.is_python for file in snapshot.files
        )

        return snapshot

    def _should_ignore(self, path: Path) -> bool:
        """Return True if this path should be ignored."""

        for part in path.parts:
            if part in self.IGNORE_DIRS:
                return True

        if path.name in self.IGNORE_FILES:
            return True

        return False

    def _generate_file_id(self, relative_path: Path) -> str:
        """
        Generate a stable identifier.

        Example:
            backend/app/core/logger.py

        becomes

            backend.app.core.logger
        """

        return str(relative_path.with_suffix("")).replace("\\", ".").replace("/", ".")
