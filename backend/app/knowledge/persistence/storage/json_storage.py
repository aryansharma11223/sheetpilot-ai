"""
===============================================================================
AEVON

JSON Storage Provider
===============================================================================
"""

from __future__ import annotations

import json
from pathlib import Path

from app.knowledge.persistence.contracts import RepositorySnapshot

from .base_storage import BaseStorage


class JsonStorage(BaseStorage):
    @property
    def name(self) -> str:
        return "JSON"

    def save(
        self,
        snapshot: RepositorySnapshot,
        destination: Path,
    ) -> None:

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination.write_text(
            json.dumps(
                snapshot.model_dump(mode="json"),
                indent=4,
            ),
            encoding="utf-8",
        )

    def load(
        self,
        source: Path,
    ) -> RepositorySnapshot:

        data = json.loads(
            source.read_text(
                encoding="utf-8",
            )
        )

        return RepositorySnapshot.model_validate(data)
