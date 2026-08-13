"""
AEVON Kernel
============

Internal Dependency Validator

This module provides the internal implementation of the Kernel
dependency validation contract.

Responsibilities:
- Validate Kernel dependency declarations.
- Enforce documented dependency requirements.
- Enforce necessary dependency requirements.
- Reject dependencies that should be replaced by events.
- Reject dependencies that bypass interfaces.
- Reject invalid ownership relationships.
- Detect circular dependencies.

The dependency validator does NOT:
- Resolve dependencies.
- Instantiate components.
- Register components.
- Start or stop components.
- Perform runtime orchestration.
- Execute intelligence logic.

Those responsibilities belong to their respective Kernel
subsystems.
"""

from __future__ import annotations

from collections.abc import Iterable

from kernel.interfaces import (
    DependencyDeclaration,
    KernelDependencyValidator,
)


###############################################################################
# Dependency Validator
###############################################################################


class DependencyValidator(KernelDependencyValidator):
    """
    Internal implementation of Kernel dependency validation.

    Validation is deterministic and read-only. The validator examines
    dependency declarations and raises ValueError when the declarations
    violate Kernel dependency rules.
    """

    def validate(
        self,
        dependencies: Iterable[DependencyDeclaration],
    ) -> None:
        """
        Validate Kernel dependency declarations.

        Validation rules:
        - A dependency must be documented.
        - A dependency must be necessary.
        - A dependency should not be replaced by an event.
        - A dependency should use an interface boundary.
        - A dependency must respect ownership boundaries.
        - Circular dependencies are rejected.

        Raises:
            ValueError: If one or more dependency rules are violated.
        """

        declarations = tuple(dependencies)
        violations: list[str] = []

        for dependency in declarations:
            violations.extend(
                self._validate_declaration(dependency)
            )

        violations.extend(
            self._find_circular_dependencies(declarations)
        )

        if violations:
            raise ValueError(
                "Kernel dependency validation failed:\n- "
                + "\n- ".join(violations)
            )

    @staticmethod
    def _validate_declaration(
        dependency: DependencyDeclaration,
    ) -> list[str]:
        """
        Validate the individual rules of one dependency declaration.
        """

        violations: list[str] = []

        source = dependency.source
        target = dependency.target

        if not source.strip():
            violations.append(
                "Dependency source cannot be empty."
            )

        if not target.strip():
            violations.append(
                "Dependency target cannot be empty."
            )

        if source == target:
            violations.append(
                f"Self-dependency is not allowed: {source}"
            )

        if not dependency.documented:
            violations.append(
                f"Dependency is not documented: {source} -> {target}"
            )

        if not dependency.necessary:
            violations.append(
                f"Dependency is not necessary: {source} -> {target}"
            )

        if dependency.event_possible:
            violations.append(
                f"Dependency should be replaced by an event: "
                f"{source} -> {target}"
            )

        if not dependency.interface_based:
            violations.append(
                f"Dependency does not use an interface boundary: "
                f"{source} -> {target}"
            )

        if not dependency.ownership_valid:
            violations.append(
                f"Dependency violates ownership boundaries: "
                f"{source} -> {target}"
            )

        return violations

    @staticmethod
    def _find_circular_dependencies(
        dependencies: Iterable[DependencyDeclaration],
    ) -> list[str]:
        """
        Detect circular dependency paths.

        The graph is represented using source and target identifiers.
        A depth-first traversal is used to identify cycles.
        """

        graph: dict[str, set[str]] = {}

        for dependency in dependencies:
            graph.setdefault(dependency.source, set()).add(
                dependency.target
            )
            graph.setdefault(dependency.target, set())

        cycles: list[str] = []
        visited: set[str] = set()
        active: set[str] = set()
        path: list[str] = []

        def visit(node: str) -> None:
            if node in active:
                try:
                    start = path.index(node)
                except ValueError:
                    start = 0

                cycle = path[start:] + [node]
                cycles.append(" -> ".join(cycle))
                return

            if node in visited:
                return

            visited.add(node)
            active.add(node)
            path.append(node)

            for target in sorted(graph.get(node, ())):
                visit(target)

            path.pop()
            active.remove(node)

        for node in sorted(graph):
            visit(node)

        unique_cycles = list(dict.fromkeys(cycles))

        return [
            f"Circular dependency detected: {cycle}"
            for cycle in unique_cycles
        ]


###############################################################################
# Public API
###############################################################################


__all__ = [
    "DependencyValidator",
]
