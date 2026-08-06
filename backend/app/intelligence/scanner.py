from pathlib import Path

from .config import IGNORE_FILES, IGNORE_FOLDERS
from .models import (
    FileNode,
    FolderNode,
    RepositorySnapshot,
)


class RepositoryScanner:
    """
    Scans the repository and creates an in-memory snapshot.
    """

    def __init__(self, root: Path):

        self.root = root.resolve()

    def scan(self) -> RepositorySnapshot:

        snapshot = RepositorySnapshot(root=self.root)

        for item in self.root.rglob("*"):

            if any(part in IGNORE_FOLDERS for part in item.parts):
                snapshot.ignored.append(item)
                continue

            if item.name in IGNORE_FILES:
                snapshot.ignored.append(item)
                continue

            if item.is_dir():

                snapshot.folders.append(
                    FolderNode(
                        path=item,
                        name=item.name,
                    )
                )

            else:

                snapshot.files.append(
                    FileNode(
                        path=item,
                        name=item.name,
                        extension=item.suffix.lower(),
                        size=item.stat().st_size,
                    )
                )

        return snapshot