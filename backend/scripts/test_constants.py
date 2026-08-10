from app.core.constants import (
    AIProvider,
    APP_NAME,
    AUTHOR,
    CapabilityStatus,
    Environment,
    FileType,
    VERSION,
)

print("=" * 60)
print("SheetPilot Constants Test")
print("=" * 60)

print(APP_NAME)
print(VERSION)
print(AUTHOR)

print()

print(Environment.DEVELOPMENT)
print(Environment.PRODUCTION)

print()

print(AIProvider.OPENAI)
print(AIProvider.GEMINI)

print()

print(CapabilityStatus.ACTIVE)

print()

print(FileType.PYTHON)
print(FileType.JSON)
print(FileType.PDF)
