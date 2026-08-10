"""
===============================================================================
SheetPilot AI

Engineering Agent Test
===============================================================================
"""

from app.agents.contracts import EngineerRequest
from app.agents.engineering_agent import EngineeringAgent


def main():

    request = EngineerRequest(
        prompt="Add Excel import support."
    )

    agent = EngineeringAgent()

    response = agent.run(request)

    print("=" * 60)
    print("Engineering Agent v0.1")
    print("=" * 60)

    print(f"Request : {request.prompt}")
    print()

    print(response.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
