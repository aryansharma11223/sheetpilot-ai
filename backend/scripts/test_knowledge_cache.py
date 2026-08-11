from datetime import datetime

from app.knowledge.cache import CacheManager
from app.knowledge.contracts import (
    KnowledgeCategory,
    KnowledgeItem,
)
from app.knowledge.persistence.contracts import (
    RepositorySnapshot,
    SnapshotMetadata,
)
from app.knowledge.persistence.manager import PersistenceManager


def main() -> None:

    cache = CacheManager()
    persistence = PersistenceManager()

    if cache.exists():
        cache.delete()

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

    persistence.save(
        snapshot,
        cache.cache_file,
    )

    print("=" * 60)
    print("Knowledge Cache Test")
    print("=" * 60)

    print(f"Cache Exists : {cache.exists()}")
    print(f"Cache File   : {cache.cache_file}")

    loaded = persistence.load(
        cache.cache_file
    )

    print(f"Items Loaded : {loaded.item_count}")

    cache.delete()

    print(f"After Delete : {cache.exists()}")


if __name__ == "__main__":
    main()
