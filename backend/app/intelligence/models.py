from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from app.intelligence.indexes.repository_index import RepositoryIndex


@dataclass(slots=True)
class FileNode:
    """Represents a file inside the repository."""

    path: Path
    name: str
    extension: str
    size: int


@dataclass(slots=True)
class FolderNode:
    """Represents a folder inside the repository."""

    path: Path
    name: str


@dataclass(slots=True)
class RepositoryMetadata:
    """Repository level metadata."""

    scanned_at: datetime
    total_files: int = 0
    total_folders: int = 0
    ignored_items: int = 0


@dataclass(slots=True)
class RepositoryState:
    """Complete in-memory representation of the repository."""

    root: Path

    folders: list[FolderNode] = field(default_factory=list)

    files: list[FileNode] = field(default_factory=list)

    ignored: list[Path] = field(default_factory=list)

    metadata: RepositoryMetadata | None = None

    index: RepositoryIndex | None = None