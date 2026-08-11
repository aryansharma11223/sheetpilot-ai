from app.context import ContextEngine
from app.context.contracts import ContextRequest


def main():

    engine = ContextEngine()

    result = engine.run(
        ContextRequest(
            prompt="ARCHITECTURE",
        )
    )

    print("=" * 60)
    print("Context Engine Test")
    print("=" * 60)

    print(f"Sources : {result.source_count}")

    if result.sources:
        print(result.sources[0].title)
        print(result.sources[0].source_type.value)


if __name__ == "__main__":
    main()
