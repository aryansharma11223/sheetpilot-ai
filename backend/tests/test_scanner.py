from pathlib import Path

from app.intelligence.scanner import RepositoryScanner


def test_scan():

    scanner = RepositoryScanner(Path("."))

    snapshot = scanner.scan()

    assert len(snapshot.files) > 0

    assert len(snapshot.folders) > 0