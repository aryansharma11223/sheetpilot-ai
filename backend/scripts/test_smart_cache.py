from pathlib import Path

from app.knowledge.cache import CacheManager


def main() -> None:

    print("=" * 60)
    print("Smart Cache")
    print("=" * 60)

    cache = CacheManager()

    repository = cache.load_or_build(
        Path("../docs"),
    )

    print(f"Status      : {cache.status.value}")
    print(f"Items       : {repository.count}")
    print(f"Cache File  : {cache.cache_file}")

    if repository.count:
        print(
            f"First Item  : {repository.items[0].title}"
        )


if __name__ == "__main__":
    main()
