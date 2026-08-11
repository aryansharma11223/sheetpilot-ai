from datetime import datetime

from app.knowledge.contracts import (
    KnowledgeCategory,
    KnowledgeItem,
)

from app.knowledge.persistence.contracts import (
    RepositorySnapshot,
    SnapshotMetadata,
)


def main() -> None:

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

    print("=" * 60)
    print("Knowledge Persistence Test")
    print("=" * 60)

    print(f"Version     : {snapshot.metadata.version}")
    print(f"Root        : {snapshot.metadata.root_directory}")
    print(f"Items       : {snapshot.item_count}")
    print(f"First Item  : {snapshot.items[0].title}")


if __name__ == "__main__":
    main()
