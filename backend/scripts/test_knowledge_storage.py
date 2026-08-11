from datetime import datetime
from pathlib import Path

from app.knowledge.contracts import (
    KnowledgeCategory,
    KnowledgeItem,
)

from app.knowledge.persistence.contracts import (
    RepositorySnapshot,
    SnapshotMetadata,
)

from app.knowledge.persistence.manager import (
    PersistenceManager,
)


def main() -> None:

    manager = PersistenceManager()

    metadata = SnapshotMetadata(
        created_at=datetime.now(),
        root_directory="docs",
        total_items=1,
    )

    item = KnowledgeItem(
        id="ADR-0001",
        title="System Architecture",
        category=KnowledgeCategory.ARCHITECTURE,
        path="docs/architecture/ADR-0001.md",
        last_modified=datetime.now(),
    )

    snapshot = RepositorySnapshot(
        metadata=metadata,
        items=[item],
    )

    file = Path("temp/knowledge_snapshot.json")

    manager.save(
        snapshot,
        file,
    )

    loaded = manager.load(file)

    print("=" * 60)
    print("Knowledge Storage Test")
    print("=" * 60)

    print(f"Storage     : {manager.storage_name}")
    print(f"Items       : {loaded.item_count}")
    print(f"First Item  : {loaded.items[0].title}")
    print(f"Version     : {loaded.metadata.version}")


if __name__ == "__main__":
    main()
