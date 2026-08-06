from pathlib import Path

from app.intelligence.collector.repository_scanner import RepositoryScanner


def main():

    scanner = RepositoryScanner(Path("."))

    repository = scanner.collect()

    print("\nRepository Scan Complete\n")

    print(f"Root      : {repository.root}")
    print(f"Folders   : {repository.metadata.total_folders}")
    print(f"Files     : {repository.metadata.total_files}")
    print(f"Ignored   : {repository.metadata.ignored_items}")


if __name__ == "__main__":
    main()