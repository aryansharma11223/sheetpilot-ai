from app.intelligence.collector.repository_scanner import RepositoryScanner

scanner = RepositoryScanner()

snapshot = scanner.scan()

print("=" * 60)
print("Repository Scanner")
print("=" * 60)

print(f"Root           : {snapshot.root}")
print(f"Folders        : {snapshot.statistics.total_folders}")
print(f"Files          : {snapshot.statistics.total_files}")
print(f"Python Files   : {snapshot.statistics.python_files}")
print(f"Dependencies   : {len(snapshot.dependencies)}")
print(f"Scanned At     : {snapshot.scanned_at}")

print()

print("First 10 Files")

for file in snapshot.files[:10]:
    print(
        f"{file.id:<45} {file.extension:<8} {file.size_bytes:>8} bytes"
    )
