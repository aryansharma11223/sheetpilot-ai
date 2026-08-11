from app.core import PathManager


def main() -> None:

    print("=" * 60)
    print("Path Manager Test")
    print("=" * 60)

    print(f"Workspace : {PathManager.workspace()}")
    print(f"Knowledge : {PathManager.knowledge_directory()}")
    print(f"Cache File: {PathManager.knowledge_cache()}")
    print(f"Logs      : {PathManager.logs_directory()}")
    print(f"Memory    : {PathManager.memory_directory()}")
    print(f"Sessions  : {PathManager.sessions_directory()}")


if __name__ == "__main__":
    main()
