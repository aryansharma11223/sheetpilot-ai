from app.agents.contracts import EngineerRequest
from app.agents.stages import ObserverStage
from app.intelligence.context import EngineeringContext


def main():

    request = EngineerRequest(
        prompt="Add Google Drive integration."
    )

    observer = ObserverStage()

    snapshot = observer.run()

    context = EngineeringContext(
        request=request,
        repository=snapshot,
    )

    print("=" * 60)
    print("Engineering Context")
    print("=" * 60)

    print(context.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
