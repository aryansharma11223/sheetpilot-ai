from pathlib import Path

from app.intelligence.collector.repository_scanner import RepositoryScanner


def test_repository_scan():

    scanner = RepositoryScanner(Path("."))

    repository = scanner.collect()

    assert repository.metadata is not None

    assert repository.metadata.total_files > 0

    assert repository.metadata.total_folders > 0