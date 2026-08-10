from __future__ import annotations

from collections import defaultdict

from app.intelligence.models import FileNode


class RepositoryIndex:
    """
    Provides fast lookup for repository files.
    """

    def __init__(self) -> None:

        self._by_name: dict[str, FileNode] = {}

        self._by_extension: dict[str, list[FileNode]] = defaultdict(list)

        self._by_folder: dict[str, list[FileNode]] = defaultdict(list)

    def add_file(self, file: FileNode) -> None:

        self._by_name[file.name] = file

        self._by_extension[file.extension].append(file)

        self._by_folder[file.path.parent.name].append(file)

    def find_file(self, name: str) -> FileNode | None:

        return self._by_name.get(name)

    def find_extension(self, extension: str) -> list[FileNode]:

        return self._by_extension.get(extension.lower(), [])

    def find_folder(self, folder: str) -> list[FileNode]:

        return self._by_folder.get(folder, [])