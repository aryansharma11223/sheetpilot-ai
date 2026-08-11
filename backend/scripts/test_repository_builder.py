from pathlib import Path

from app.knowledge.builders import RepositoryBuilder


def main() -> None:

    print("=" * 60)
    print("Repository Builder Test")
    print("=" * 60)

    builder = RepositoryBuilder()

    repository = builder.build(
        Path("../docs")
    )

    print(f"Repository Items : {repository.count}")

    if repository.count:
        print(f"First Item       : {repository.items[0].title}")


if __name__ == "__main__":
    main()
