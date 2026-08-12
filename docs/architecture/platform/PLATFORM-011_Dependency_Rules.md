# AEVON Platform Dependency Rules

---

**Document:** PLATFORM-011

**Title:** Dependency Rules

**Version:** 1.0

**Status:** Active

**Owner:** Chief Architect

**Classification:** Platform Architecture

---

# Purpose

This document defines the dependency architecture of the AEVON Platform.

Its objective is to ensure that platform modules remain loosely coupled, independently maintainable, and free from circular dependencies throughout the lifetime of the project.

Every implementation shall comply with these dependency rules.

---

# Philosophy

Dependencies shall always flow in one direction.

Higher-level intelligence may depend on lower-level capabilities.

Lower-level capabilities must never depend on higher-level intelligence.

This principle preserves architectural integrity and enables independent evolution of each module.

---

# Dependency Hierarchy

The official dependency hierarchy of the platform is:

```text
Application
        │
        ▼
Kernel
        │
        ▼
Knowledge
        │
        ▼
Memory
        │
        ▼
Reasoning
        │
        ▼
Planning
        │
        ▼
Execution
```

A module may depend only on modules positioned above it in this hierarchy unless explicitly allowed by this document.

---

# Dependency Matrix

| Module | Allowed Dependencies |
|---------|----------------------|
| Application | Kernel |
| Kernel | Infrastructure only |
| Knowledge | Kernel |
| Memory | Kernel |
| Reasoning | Kernel, Knowledge, Memory |
| Planning | Kernel, Knowledge, Memory, Reasoning |
| Execution | Kernel, Knowledge, Memory, Reasoning, Planning |

No additional dependencies are permitted without architectural approval.

---

# Infrastructure Dependencies

Every module may depend upon shared platform infrastructure.

Examples include:

- Configuration
- Logging
- Path Management
- Event Bus
- Health Monitoring
- Service Registry

Infrastructure is considered platform-neutral and does not violate dependency direction.

---

# Forbidden Dependencies

The following dependency patterns are prohibited.

## Circular Dependencies

```text
Knowledge
      │
      ▼
Reasoning
      │
      ▼
Knowledge
```

Circular dependencies are forbidden.

---

## Reverse Dependencies

```text
Execution
      │
      ▼
Planning
```

Planning may support Execution.

Execution must not control Planning.

---

## Hidden Dependencies

Modules shall never depend on:

- Internal classes
- Private methods
- Undocumented behavior
- Implementation details

Only documented public interfaces may be consumed.

---

## Shared Storage

Modules shall never directly access another module's storage.

Example:

```text
Reasoning

↓

Memory Database
```

Forbidden.

All access must occur through the Memory Engine's public interface.

---

# Dependency Inversion

Whenever practical, dependencies shall point toward abstractions rather than concrete implementations.

Modules should depend on:

- Interfaces
- Contracts
- Events

Modules should avoid depending directly on implementation classes.

---

# Dependency Ownership

Each module owns:

- Its public interfaces
- Its internal implementation
- Its internal state
- Its persistence
- Its lifecycle

No other module may modify these directly.

---

# Acceptable Dependency Patterns

## Interface Dependency

```text
Reasoning
      │
      ▼
Knowledge Interface
```

Preferred.

---

## Event Dependency

```text
Execution

↓

TaskCompleted

↓

Event Bus

↓

Memory
```

Preferred.

---

## Infrastructure Dependency

```text
Planning

↓

Logging
```

Allowed.

---

# Unacceptable Dependency Patterns

## Internal Class Access

```text
Planning

↓

Reasoning.InternalAnalyzer
```

Forbidden.

---

## Shared Mutable Objects

```text
Knowledge

↓

Modify Memory Objects
```

Forbidden.

---

## Platform Shortcuts

```text
Desktop

↓

Execution Engine

↓

Memory Database
```

Forbidden.

Every interaction must follow documented interfaces.

---

# Dependency Validation

Every new dependency introduced into the platform shall satisfy the following questions.

1. Is the dependency documented?
2. Is the dependency necessary?
3. Can it be replaced with an event?
4. Can it depend on an interface instead?
5. Does it introduce a circular dependency?
6. Does it violate module ownership?

If any answer indicates a violation, the dependency shall be rejected.

---

# Architectural Constraints

The following rules are mandatory.

- Modules own their implementations.
- Modules own their persistence.
- Modules own their lifecycle.
- Dependencies remain one-directional.
- Events are preferred for notifications.
- Interfaces are preferred for synchronous interactions.
- Internal implementations remain private.

---

# Future Expansion

Future milestones may introduce:

- Plugin dependencies
- Dynamic dependency injection
- Remote service dependencies
- Distributed platform nodes
- Optional module dependencies
- Feature-based dependency loading

These capabilities shall extend the dependency model without violating the principles defined in this document.

---

# Success Criteria

The dependency architecture is considered complete when:

- Circular dependencies do not exist.
- Every dependency is documented.
- Modules remain independently testable.
- Internal implementations remain isolated.
- Interfaces remain stable.
- New modules integrate without breaking existing modules.

---

# Notes

The Dependency Rules define the structural integrity of the AEVON Platform.

Every future engineering decision involving imports, interfaces, services, or module relationships shall comply with this specification.

These rules are intended to preserve architectural consistency throughout the lifetime of the project.

---

**End of Document**
