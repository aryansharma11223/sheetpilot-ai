from app.intelligence.contracts import RepositorySnapshot

snapshot = RepositorySnapshot(root="D:/SheetPilot AI")

print(snapshot)

print()

print(snapshot.model_dump_json(indent=4))
