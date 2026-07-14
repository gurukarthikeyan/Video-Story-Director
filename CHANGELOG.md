# Changelog

All notable changes to Video Story Director will be documented in this file.

The project follows Semantic Versioning (SemVer):

MAJOR.MINOR.PATCH

- MAJOR: Breaking architectural changes.
- MINOR: New functionality while maintaining compatibility.
- PATCH: Bug fixes, documentation improvements, and non-breaking refinements.

---

# [Unreleased]

## Planned

### Backends

- Wan Backend
- Veo Backend
- Backend capability profiles

### Evaluation

- Benchmark suite
- Evaluation framework
- Backend comparison methodology

### Tooling

- Module Contracts documentation
- Build system improvements
- Automated prompt assembly

---

# [1.1.0] - 2026-07-14

## Added

- Rendering Engine introduced as a dedicated architecture layer.
- Backend abstraction separating story planning from model-specific prompt generation.
- Backend directory structure for future AI video generation models.
- LTX Backend redesigned as a Rendering Specification translator.
- Architecture documentation rewritten.
- Design Philosophy documentation created.
- Story State Engine developer documentation added.
- Implementation Plan updated to reflect the new architecture.

## Changed

- Project renamed from **LTX Story Director** to **Video Story Director**.
- Architecture reorganized into six logical layers:
  - Foundation
  - Story Intelligence
  - Rendering
  - Backend
  - Validation
  - Output
- Prompt modules 01–11 reviewed and refined.
- Rendering responsibilities moved out of the backend.
- Documentation standardized across the repository.
- Repository structure simplified by replacing version-specific architecture documents with canonical documentation.

## Removed

- Architecture coupling between story planning and the LTX backend.
- Redundant version-specific architecture documentation.

---

# [1.0.0] - 2026-07-13

## Added

- Initial modular Story Director architecture.
- Identity and Core Principles modules.
- Request Analysis Engine.
- Character Engine.
- World Engine.
- Story State Engine.
- Scene Planner.
- Frame0 Engine.
- Validation Engine.
- Output Contract.
- Initial LTX backend.
- Build script for assembling prompt modules.
- Repository structure and documentation.

## Notes

Version 1.0 established the modular foundation of Video Story Director and provided the first complete implementation targeting LTX Video.