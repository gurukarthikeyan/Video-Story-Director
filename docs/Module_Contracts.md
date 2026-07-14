# ============================================================================
# Video Story Director - Module Contracts
# ============================================================================

# Purpose

Every module owns a specific artifact.

Modules communicate only through these artifacts.

A module may consume the output of previous modules but must not modify artifacts owned by other modules.

---

| Module | Input | Output | Owns | Must Not Modify |
|---------|-------|--------|------|-----------------|
| 01 Identity | None | Identity | System Role | Everything |
| 02 Core Principles | Identity | Design Constraints | Reasoning Rules | Identity |
| 03 Request Analysis | User Request | Planning Context | Request Interpretation | Character Identity |
| 04 Character Engine | Planning Context | Character Definitions | Character Identity | Story Logic |
| 05 World Engine | Character Definitions | World Definition | Environment | Character Identity |
| 06 Story State Engine | World Definition | Story State | Runtime Continuity | Character Definitions |
| 07 Scene Planner | Story State | Scene Plan | Scene Sequence | Story State |
| 08 Frame0 Engine | Scene Plan | Frame0 Specification | Visual Anchor | Story Logic |
| 09 Rendering Engine | Frame0 + Scene Plan | Rendering Specification | Rendering Strategy | Story Planning |
| Backend | Rendering Specification | Backend Prompt | Prompt Translation | Story Planning |
| 10 Validation Engine | Backend Prompt | Validated Prompt | Quality Assurance | Story Planning |
| 11 Output Contract | Validated Prompt | Final Response | Presentation | Prompt Content |

---

# Dependency Rules

Modules may depend only on upstream modules.

Dependencies always flow in one direction.

User Request

↓

Planning Context

↓

Character Definitions

↓

World Definition

↓

Story State

↓

Scene Plan

↓

Frame0 Specification

↓

Rendering Specification

↓

Backend Prompt

↓

Validated Prompt

↓

Final Response

Circular dependencies are not permitted.

---

# Ownership Rules

Every artifact has exactly one owner.

Only the owning module may create or modify that artifact.

Other modules may consume it but should not reinterpret or rewrite it.

This preserves clear responsibilities and predictable behavior throughout the pipeline.

---

# Architectural Principle

The architecture follows a pipeline model.

Each module performs one transformation before passing its output to the next stage.

This keeps the framework modular, maintainable, extensible, and backend-independent.