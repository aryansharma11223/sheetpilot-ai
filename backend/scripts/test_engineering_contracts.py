from app.agents.contracts import (
    EngineerRequest,
    EngineerResponse,
)


def main():

    request = EngineerRequest(
        prompt="Create login page"
    )

    response = EngineerResponse(
        success=True,
        message="Contracts working."
    )

    print("=" * 60)
    print("Engineer Request")
    print("=" * 60)
    print(request.model_dump_json(indent=4))

    print()

    print("=" * 60)
    print("Engineer Response")
    print("=" * 60)
    print(response.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
