# Contributing

Thank you for your interest in Video Story Director.

The project follows a modular architecture.

Every module has a clearly defined responsibility.

Before making changes, please understand the architecture described in:

- docs/Architecture.md
- docs/Design_Philosophy.md

---

# Design Principles

Contributions should follow these principles:

- Single Responsibility
- Separation of Concerns
- Backend Independence
- Story-First Design
- Maintainability
- Consistency

---

# Module Guidelines

Prompt modules should:

- perform one responsibility
- clearly define inputs and outputs
- avoid duplicating logic from other modules
- remain backend-independent unless they are backend modules

---

# Backend Development

New AI video models should be implemented as separate backends.

Backends may optimize prompt wording but must never modify:

- story planning
- character identity
- world state
- rendering specification

---

# Documentation

Architecture changes should be reflected in:

- Architecture.md
- Design_Philosophy.md
- Module_Contracts.md

Documentation should remain synchronized with implementation.

---

# Pull Requests

Pull requests should:

- describe the motivation
- explain architectural impact
- preserve existing module contracts
- avoid unnecessary redesign

The project favors incremental evolution over large architectural rewrites.