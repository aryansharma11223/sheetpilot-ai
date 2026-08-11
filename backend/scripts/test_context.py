"""
Context Engine Test
"""

from app.context.context_builder import ContextBuilder
from app.context.contracts import ContextRequest


def main() -> None:

    builder = ContextBuilder()

    request = ContextRequest(
        prompt="Add Excel import support"
    )

    result = builder.build(request)

    print("=" * 60)
    print("Context Engine Test")
    print("=" * 60)

    print(f"Registered Sources : {builder.source_count}")
    print(f"Collected Sources  : {result.source_count}")

    print()

    for source in result.sources:
        print(
            f"[{source.source_type.value}] "
            f"{source.title} "
            f"(Score={source.score})"
        )


if __name__ == "__main__":
    main()
