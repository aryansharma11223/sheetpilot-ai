# ADR-0001 — SheetPilot System Architecture

Status: Accepted

Date: 2026-08-10

---

# Vision

SheetPilot is an AI Software Engineer.

It understands software projects, reasons about them, proposes improvements, implements approved changes, verifies the implementation, documents the outcome, and continuously learns.

The system must always require human approval before modifying source code.

---

# Core Philosophy

Observe → Understand → Build Context → Reason → Plan → Approve → Execute → Verify → Document → Learn

Reasoning always comes before execution.

---

# Architectural Principles

1. Single Responsibility
2. Contract First Design
3. Context Before Intelligence
4. Human Approval Required
5. Modular Architecture
6. Replaceability
7. Testability
8. Documentation Driven Development

---

# High-Level Architecture

Engineering Agent

↓

Observer Stage

↓

Context Engine

↓

Reasoning Engine

↓

Planner Stage

↓

Human Approval

↓

Builder Stage

↓

Reviewer Stage

↓

Documentation Stage

↓

Learning Stage

---

# System Layers

Core

Shared infrastructure.

Examples:

- Configuration
- Logging
- Paths
- Constants

---

Intelligence

Responsible for understanding and reasoning.

Examples:

- Observer
- Context
- Planner
- Learning

---

Knowledge

Stores engineering knowledge.

Examples:

- Engineering Standards
- Architecture
- Decisions
- Patterns
- Rules

---

Execution

Responsible for changing the repository.

Examples:

- Builder
- Reviewer
- Testing
- Documentation
- Git

---

UI

Everything the user interacts with.

---

# Engineering Standards

Every stage exposes exactly one public method:

run()

Every stage communicates using contracts.

No stage passes arbitrary dictionaries.

---

# Human Approval

No source-code modification may occur without explicit approval.

The AI may suggest improvements autonomously.

Implementation always requires approval.

---

# Long-Term Goal

Create an AI Software Engineer that continuously improves while remaining transparent, explainable, and human-controlled.
