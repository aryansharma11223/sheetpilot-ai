from __future__ import annotations

from datetime import datetime
from pathlib import Path

from app.intelligence.config import (
    IGNORE_FILES,
    IGNORE_FOLDERS,
)
from app.intelligence.models import (
    FileNode,
    FolderNode,
    RepositoryMetadata,
    RepositoryState,
)


class RepositoryScanner:
    """
    Scans the repository and creates an in-memory RepositoryState.
    """

    def __init__(self, root: Path):

        self.root = root.resolve()

    def collect(self) -> RepositoryState:

        repository = RepositoryState(root=self.root)

        for item in self.root.rglob("*"):

            if self._should_ignore(item):

                repository.ignored.append(item)

                continue

            if item.is_dir():

                repository.folders.append(
                    FolderNode(
                        path=item,
                        name=item.name,
                    )
                )

                continue

            repository.files.append(
                FileNode(
                    path=item,
                    name=item.name,
                    extension=item.suffix.lower(),
                    size=item.stat().st_size,
                )
            )

        repository.metadata = RepositoryMetadata(
            scanned_at=datetime.now(),
            total_files=len(repository.files),
            total_folders=len(repository.folders),
            ignored_items=len(repository.ignored),
        )

        return repository

    def _should_ignore(self, item: Path) -> bool:

        if item.name in IGNORE_FILES:
            return True

        return any(part in IGNORE_FOLDERS for part in item.parts)