# AEVON Working Model

---

**Document:** Working Model

**Version:** 1.0

**Status:** Active

**Owner:** Founder

**Applies To:** Entire AEVON Development Lifecycle

---

# Purpose

This document defines the official working model for developing AEVON.

It establishes how the Founder and AI collaborate, how decisions are made, how files are delivered, and how documentation and implementation evolve throughout the project.

This document is considered part of the project's governance.

---

# Core Philosophy

The objective is not merely to write code.

The objective is to engineer a maintainable, scalable, and well-documented AI platform that can continue evolving for years without losing architectural consistency.

Every engineering decision should prioritize long-term quality over short-term convenience.

---

# Development Modes

Development operates in two distinct modes.

## 1. Engineering Mode

Engineering Mode is the default mode.

The primary objective is implementation.

Responses focus on:

- Production-quality code
- Architecture compliance
- Testing
- Maintainability
- Performance
- Scalability

Documentation is updated only when required.

---

## 2. Documentation Mode

Documentation Mode is entered explicitly when working inside the `docs/` directory.

The objective is to create or improve project documentation.

To maintain momentum, Documentation Mode follows an accelerated workflow:

- One document per response
- Complete replaceable file
- Minimal discussion unless clarification is required

Once documentation work is complete, development returns to Engineering Mode.

---

# Standard Response Format

Unless explicitly requested otherwise, every implementation response shall follow this structure.

1. Relative Path

2. Complete Updated Replaceable File

3. Action

4. Why it changed

5. Documentation Synchronization (if required)

6. Git Recommendation

This format ensures that every change can be directly applied to the repository.

---

# Documentation Principles

Documentation exists to reduce uncertainty during implementation.

Documentation shall describe:

- Architecture
- Governance
- Long-term decisions
- Public contracts
- Development workflows

Documentation shall not duplicate implementation details unnecessarily.

---

# Documentation Synchronization

Documentation Synchronization is required only when a change affects long-term project knowledge.

Examples include:

- Architectural decisions
- Governance updates
- Workflow changes
- New platform contracts
- Repository structure changes

Routine implementation does not require documentation updates.

---

# Governance Rule

Any decision that changes how AEVON will be developed throughout the project shall be documented before becoming part of the standard workflow.

Examples include:

- Development workflow
- Repository organization
- Documentation process
- Code delivery format
- Architectural governance
- Long-term engineering standards

---

# Repository Rules

Existing repository structure shall be respected.

New top-level directories shall not be introduced unless justified through an approved architectural decision.

Whenever possible, existing documentation locations shall be extended rather than creating new structures.

---

# Engineering Principles

Implementation shall prioritize:

- Readability
- Maintainability
- Testability
- Loose coupling
- High cohesion
- Single Responsibility Principle
- Interface-first design
- Platform-first architecture

Temporary shortcuts should be avoided whenever practical.

---

# Architecture First

Major architectural decisions shall be documented before implementation.

Implementation shall conform to approved architectural documents.

Architecture should not be modified implicitly through code.

---

# File Replacement Policy

Whenever an existing file is modified, the complete updated file shall be provided.

Partial snippets should be avoided unless explicitly requested.

This ensures deterministic updates and simplifies repository maintenance.

---

# Git Workflow

Each response shall include an appropriate Git recommendation.

Typical workflow:

```bash
git add .
git commit -m "<meaningful commit message>"
```

Commit messages should describe the primary purpose of the change.

---

# Session Workflow

Each development session should follow this sequence.

1. Review current project state.
2. Confirm current milestone.
3. Complete one logical unit of work.
4. Update documentation if required.
5. Recommend a Git commit.
6. Identify the next logical step.

This keeps progress incremental and traceable.

---

# Definition of Done

A task is considered complete when:

- Implementation is functional.
- Architecture is respected.
- Code quality is acceptable.
- Documentation is synchronized if required.
- The repository remains buildable.
- The next step is clearly identified.

---

# Continuous Improvement

The working model may evolve throughout the project.

Any modification to this document shall:

- Be intentional.
- Be documented.
- Be reviewed before adoption.

No long-term workflow change shall be adopted informally.

---

# Scope

This working model applies to:

- Documentation
- Architecture
- Backend
- Frontend
- AI Systems
- Infrastructure
- Testing
- Automation
- Deployment

Unless superseded by a future approved revision.

---

# Conclusion

This document defines how AEVON is engineered.

It serves as the operational agreement between the Founder and AI, ensuring that development remains consistent, transparent, and aligned with the long-term vision of the platform.

---

**End of Document**
