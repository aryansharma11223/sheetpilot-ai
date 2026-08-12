# AEVON

# GENESIS-004

# 02_Repository_Standards.md

---

**Document ID:** G004-002

**Program:** PROGRAM-001 — GENESIS

**Document Title:** Repository Standards

**Version:** 1.0

**Status:** Draft

**Owner:** Chief Architect

**Classification:** Repository Engineering Standard

**Parent Document:** G004-000 — Engineering Standards

---

# Purpose

This document defines the standards governing the structure, organization, naming, lifecycle, and management of the AEVON source repository.

The repository is the permanent home of AEVON's source code, documentation, engineering knowledge, automation, templates, architecture, and operational assets.

A consistent repository structure enables:

- Faster onboarding
- Better discoverability
- Easier automation
- Reduced maintenance
- Predictable project growth
- AI-assisted engineering

These standards apply to every repository associated with the AEVON platform.

---

# Objectives

The Repository Standards shall:

- Establish a predictable folder hierarchy.
- Define naming conventions.
- Standardize document locations.
- Prevent structural duplication.
- Support automation.
- Improve repository navigation.
- Enable long-term scalability.

---

# Repository Design Principles

The repository shall follow these principles:

- One responsibility per folder.
- Predictable folder names.
- Stable paths.
- Minimal nesting.
- Explicit ownership.
- Automation-friendly layout.
- Documentation alongside implementation.

---

# Standard Repository Layout

```text
AEVON/
│
├── GENESIS/
├── FORGE/
├── ATLAS/
├── ORBIT/
│
├── docs/
├── architecture/
├── standards/
├── adr/
├── templates/
├── prompts/
├── knowledge/
├── engines/
├── services/
├── runtime/
├── plugins/
├── sdk/
├── api/
├── tools/
├── automation/
├── testing/
├── deployment/
├── scripts/
├── assets/
├── examples/
├── experiments/
│
├── MASTER_REGISTRY.md
├── README.md
├── CHANGELOG.md
├── LICENSE
└── CONTRIBUTING.md
```

---

# Repository Rules

## STD-001 — Repository Root

The repository root shall contain only high-level folders and essential project files.

The root must never become a general storage location.

---

## STD-002 — Single Responsibility

Each top-level folder shall have one clearly defined purpose.

Examples:

- `engines/` contains Engineering Engines only.
- `services/` contains Platform Services only.
- `plugins/` contains Plugins only.

Mixed responsibilities are prohibited.

---

## STD-003 — Stable Folder Names

Folder names shall remain stable over time.

Renaming major folders requires:

- Architecture review
- ADR
- Migration plan

---

## STD-004 — Folder Naming Convention

Folders shall use:

- lowercase
- hyphen-separated words

Examples:

```text
knowledge-base
runtime
platform-services
engineering-engines
```

Avoid:

```text
KnowledgeBase
Knowledge_Base
MyFolder
folder1
```

---

## STD-005 — File Naming Convention

Markdown files:

```text
Pascal_Case.md
```

Examples:

```text
Engineering_Principles.md
Repository_Standards.md
Runtime_Model.md
```

Source code shall follow language-specific conventions defined in Software Standards.

---

## STD-006 — Reserved Directories

The following directory names are reserved:

```text
architecture
automation
knowledge
runtime
engines
services
plugins
templates
testing
deployment
docs
api
sdk
assets
```

Reserved names shall not be repurposed.

---

## STD-007 — Documentation Placement

Documentation shall remain close to the implementation it describes whenever practical.

Examples:

```text
engines/

PlanningEngine/

README.md

Architecture.md

Implementation/
```

Avoid separating implementation and documentation unnecessarily.

---

## STD-008 — No Duplicate Documents

Every engineering document shall have one authoritative location.

Duplicate copies are prohibited.

Cross references shall be used instead.

---

## STD-009 — Program Organization

Each program shall exist in an independent directory.

Example:

```text
GENESIS/
FORGE/
ATLAS/
ORBIT/
```

Programs shall never overlap.

---

## STD-010 — Template Repository

Reusable engineering templates shall be stored exclusively under:

```text
templates/
```

Examples:

- ADR Template
- Engine Template
- Plugin Template
- Document Template
- API Template

---

# Document Standards

---

## STD-011 — Metadata

Every engineering document shall begin with standardized metadata.

Required fields include:

- Document ID
- Title
- Version
- Status
- Owner
- Parent
- Classification

---

## STD-012 — Version Control

Every document shall maintain version history through Git.

Version numbers shall follow Semantic Versioning where applicable.

---

## STD-013 — Status Values

Allowed document statuses:

- Draft
- In Review
- Approved
- Feature Complete
- Released
- Deprecated
- Archived

No custom status values shall be introduced.

---

## STD-014 — Cross References

Documents shall reference related documents rather than duplicate information.

Cross references shall use Document IDs whenever practical.

---

## STD-015 — MASTER_REGISTRY

Every permanent engineering artifact shall be registered in:

```text
MASTER_REGISTRY.md
```

Registration is mandatory before release.

---

# Repository Ownership

Every major directory shall have a defined owner.

Examples:

| Directory | Owner |
|-----------|-------|
| architecture | Chief Architect |
| runtime | Platform Team |
| engines | Engineering Team |
| knowledge | Knowledge Team |
| automation | FORGE Team |

Ownership ensures accountability.

---

# Repository Automation

The repository shall support automated:

- Structure validation
- Naming validation
- Metadata validation
- Duplicate detection
- Link validation
- Registry synchronization
- Documentation generation

---

# Repository Evolution

Repository evolution shall occur through controlled governance.

Major structural changes require:

- Architecture review
- ADR
- Migration plan
- Repository update
- Documentation update

---

# Compliance Checklist

Every repository shall satisfy the following:

- Standard folder hierarchy
- Approved naming
- Registered artifacts
- Valid metadata
- No duplicate documents
- Stable structure
- Traceable ownership
- Automated validation support

---

# Summary

The Repository Standards establish the structural foundation of the AEVON engineering ecosystem.

By standardizing repository organization, naming, ownership, documentation, and governance, these standards ensure that the repository remains scalable, discoverable, automation-ready, and maintainable throughout the lifecycle of the platform.

---

**End of Document**

**Next Document**

`03_Documentation_Standards.md`
