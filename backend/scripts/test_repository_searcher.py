from pathlib import Path

from app.knowledge.builders import RepositoryBuilder
from app.knowledge.search import RepositorySearcher


def main():

    builder = RepositoryBuilder()

    repository = builder.build(
        Path("../docs")
    )

    searcher = RepositorySearcher()

    results = searcher.search(
        repository,
        "ARCHITECTURE",
    )

    print("=" * 60)
    print("Repository Search Test")
    print("=" * 60)

    print(f"Results : {len(results)}")

    if results:
        print(results[0].item.title)


if __name__ == "__main__":
    main()
