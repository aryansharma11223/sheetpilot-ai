from pathlib import Path

from app.intelligence.collector.repository_scanner import RepositoryScanner


def main() -> None:

    scanner = RepositoryScanner(Path("."))

    repository = scanner.collect()

    print("\n" + "=" * 60)
    print("          AEVON - REPOSITORY SCANNER")
    print("=" * 60)

    print(f"Repository Root : {repository.root}")
    print(f"Folders         : {repository.metadata.total_folders}")
    print(f"Files           : {repository.metadata.total_files}")
    print(f"Ignored         : {repository.metadata.ignored_items}")

    print("\n" + "-" * 60)
    print("INDEX TESTS")
    print("-" * 60)

    readme = repository.index.find_file("README.md")

    if readme:
        print(f"README.md       : {readme.path}")
    else:
        print("README.md       : Not Found")

    python_files = repository.index.find_extension(".py")

    print(f"Python Files    : {len(python_files)}")

    markdown_files = repository.index.find_extension(".md")

    print(f"Markdown Files  : {len(markdown_files)}")

    backend_files = repository.index.find_folder("backend")

    print(f"Backend Files   : {len(backend_files)}")

    print("=" * 60)


if __name__ == "__main__":
    main()
