"""
===============================================================================
SheetPilot AI

Verification Launcher

Usage:
    python -m scripts.verify_all
===============================================================================
"""

from app.verification import VerificationRunner


def main() -> None:
    runner = VerificationRunner()

    results = runner.run_all()

    print("=" * 60)
    print("SheetPilot Verification Report")
    print("=" * 60)

    passed = 0
    failed = 0

    for result in results:

        print(f"\n[{result.status.value}] {result.subsystem}")

        for message in result.messages:
            print(f"  ✓ {message}")

        for error in result.errors:
            print(f"  ✗ {error}")

        print(f"  Duration: {result.duration_seconds:.4f}s")

        if result.successful:
            passed += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print(f"Total Verifiers : {len(results)}")
    print(f"Passed          : {passed}")
    print(f"Failed          : {failed}")
    print("=" * 60)


if __name__ == "__main__":
    main()
