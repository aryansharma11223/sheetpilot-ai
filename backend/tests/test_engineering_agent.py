from app.agents.contracts import EngineerRequest
from app.agents.engineering_agent import EngineeringAgent


def main():

    agent = EngineeringAgent()

    request = EngineerRequest(
        prompt="Add support for Excel import."
    )

    response = agent.handle_request(request)

    print()

    print("=" * 60)
    print("Engineering Agent")
    print("=" * 60)

    print(response.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
