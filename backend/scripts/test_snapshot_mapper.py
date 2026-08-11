from pathlib import Path

from app.knowledge.builders import RepositoryBuilder
from app.knowledge.persistence.mappers import RepositorySnapshotMapper


def main() -> None:

    print("=" * 60)
    print("Snapshot Mapper Test")
    print("=" * 60)

    builder = RepositoryBuilder()
    mapper = RepositorySnapshotMapper()

    repository = builder.build(Path("../docs"))

    snapshot = mapper.to_snapshot(
        repository,
        Path("../docs"),
    )

    print(f"Snapshot Items : {snapshot.item_count}")
    print(f"Metadata Items : {snapshot.metadata.total_items}")

    restored = mapper.from_snapshot(snapshot)

    print(f"Restored Items : {restored.count}")


if __name__ == "__main__":
    main()
