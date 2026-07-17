# Module 07 – Scene Planner

> **Version:** v1.2.0
>
> **Status:** Active
>
> **Module:** 07
>
> **Responsibility:** Narrative Planning

---

# Purpose

The Scene Planner is the narrative reasoning engine of Video Story Director.

Its responsibility is to transform story intent into a coherent, backend-independent **Scene Model** that captures everything required to render a scene consistently.

The Scene Planner does **not** write prompts.

It does **not** perform rendering.

It does **not** optimize for a specific video generation model.

Instead, it reasons about the story in the same way a film director reasons about a scene before filming begins.

The resulting Scene Model becomes the authoritative input for the Rendering Engine.

---

# Scope

The Scene Planner is responsible for answering one question:

> **What should happen in this scene?**

It is not responsible for determining how that understanding is expressed to a rendering backend.

Rendering remains the responsibility of Module 09 – Rendering Engine.

---

# Inputs

The Scene Planner receives:

* Story Understanding
* Character definitions
* World definitions
* Story State
* User objectives
* Previous scene context
* Project constraints

These inputs represent semantic understanding rather than rendering instructions.

---

# Outputs

The Scene Planner produces a complete **Scene Model**.

The Scene Model contains the planner's semantic understanding of the scene and serves as the contract between planning and rendering.

The Scene Model is backend independent.

It contains no rendering-specific parameters.

---

# Responsibilities

The Scene Planner is responsible for:

* Understanding narrative intent.
* Identifying story goals.
* Defining scene goals.
* Planning believable action sequences.
* Constructing the Scene Model.
* Maintaining narrative continuity.
* Managing pacing.
* Estimating action complexity.
* Preparing scenes for rendering.

The Scene Planner is **not** responsible for:

* Prompt wording.
* Rendering parameters.
* Backend optimization.
* Prompt Relay.
* MSR.
* IC-LoRA.
* Video generation.

Those responsibilities belong to the Rendering Engine.

---

# Planning Philosophy

Scene Planning follows the philosophy defined in:

> `docs/design/scene_planning_philosophy.md`

The planner reasons about stories rather than prompts.

Every planning decision should strengthen narrative clarity while remaining independent of rendering implementation.

---

# Core Planning Principles

## 1. Story Before Rendering

Story intent is the highest priority.

Rendering techniques may evolve.

Story understanding should remain stable.

The planner must never alter the intended story solely to accommodate a rendering backend.

---

## 2. Goals Before Actions

Every action exists to achieve a goal.

Planning begins by identifying narrative objectives before considering individual actions.

Actions without purpose should not exist.

---

## 3. Believability Before Complexity

A believable sequence of simple actions is preferable to an unrealistic sequence of complex actions.

The planner should favor coherent progression over unnecessary spectacle.

---

## 4. Continuity Before Novelty

Characters, environments, story state, and important objects should remain internally consistent.

Unexpected changes should occur only when explicitly required by the story.

---

## 5. Clarity Before Detail

The audience should easily understand what happens within the scene.

Additional detail should improve understanding rather than increase ambiguity.

---

# Story Goal vs Scene Goal

The planner distinguishes between story-level objectives and scene-level objectives.

## Story Goal

Represents the larger narrative objective.

Examples:

* Escape the prison.
* Rescue the child.
* Recover the artifact.
* Defeat the antagonist.

Story Goals may span multiple scenes.

---

## Scene Goal

Represents the immediate objective of the current scene.

Examples:

* Unlock the prison door.
* Retrieve the key.
* Cross the bridge.
* Repair the satellite.

Every planned scene should have one primary Scene Goal.

Scene Goals should directly contribute toward the Story Goal.

---

# Planning Strategy

The Scene Planner reasons progressively.

Rather than attempting to solve every aspect of the scene simultaneously, it incrementally builds understanding through successive refinement.

Each planning stage enriches the Scene Model while preserving consistency with previous decisions.

This approach improves narrative coherence, simplifies reasoning, and establishes a stable semantic foundation for rendering.

---

# Planning Workflow (Overview)

Every scene follows the same high-level reasoning sequence.

```text
Understand Story
        │
        ▼
Identify Story Goal
        │
        ▼
Identify Scene Goal
        │
        ▼
Construct Scene Model
        │
        ▼
Plan Action Graph
        │
        ▼
Validate Continuity
        │
        ▼
Estimate Action Budget
        │
        ▼
Prepare for Rendering
```

Subsequent sections describe each stage in greater detail.

---

# Progressive Scene Refinement

The Scene Planner constructs the Scene Model through **Progressive Scene Refinement (PSR)**.

Rather than attempting to solve every aspect of a scene simultaneously, the planner incrementally builds understanding through successive reasoning stages.

Each stage enriches the Scene Model while preserving consistency with previous planning decisions.

Planning therefore becomes an additive process rather than a replacement process.

A later refinement should never contradict an earlier decision without explicit justification.

---

# Progressive Planning Stages

The planner follows the conceptual reasoning sequence below.

```text
Story Understanding
        │
        ▼
Story Goal
        │
        ▼
Scene Goal
        │
        ▼
Scene Model Foundation
        │
        ▼
Action Graph
        │
        ▼
Camera Intent
        │
        ▼
Continuity Validation
        │
        ▼
Action Budget
        │
        ▼
Viewer Outcome
        │
        ▼
Scene Model Complete
```

Each stage contributes semantic knowledge to the Scene Model.

No stage performs rendering.

---

# Scene Model Construction

The Scene Model is constructed progressively rather than generated in a single step.

The planner continuously enriches the model until every important aspect of the scene has been reasoned about.

Typical planning includes:

* Story context
* Scene goals
* Characters
* Environment
* Story state
* Important objects
* Action graph
* Camera intent
* Constraints
* Viewer outcome

The Scene Model should represent understanding rather than description.

---

# Story Context

Planning begins by understanding the narrative context surrounding the scene.

Questions include:

* Where does this scene occur within the story?
* What happened previously?
* What changes after this scene?
* Why does this scene exist?

Without narrative context, individual actions lose meaning.

---

# Scene Goal

Every planned scene should have a clearly identifiable objective.

The Scene Goal provides direction for all subsequent planning decisions.

Examples include:

* Unlock the door.
* Repair the satellite.
* Introduce a character.
* Escape the room.
* Reveal important information.

A scene may contain many actions but should generally pursue a single primary goal.

---

# Character Understanding

Characters should be planned before actions.

The planner should identify:

* Primary character
* Supporting characters
* Character roles
* Relationships
* Motivations
* Current story state

Actions should emerge naturally from character intent.

---

# Environment Understanding

The environment provides the context in which actions occur.

Planning should consider:

* Location
* Time
* Weather
* Lighting
* Atmosphere
* Physical limitations

Environmental consistency should be maintained throughout the scene unless the story explicitly requires change.

---

# Story State

The planner maintains an understanding of the current state of the narrative world.

Examples include:

* Character positions
* Object locations
* Completed objectives
* Pending objectives
* Current relationships
* Environmental conditions

Story State provides continuity between scenes.

---

# Action Graph

The planner represents actions as a logical dependency graph rather than a simple chronological list.

Each action should naturally enable the next.

Example:

```text
Inspect
        │
        ▼
Approach
        │
        ▼
Retrieve Tool
        │
        ▼
Repair
        │
        ▼
Verify
```

Dependencies are more important than chronology.

A coherent Action Graph naturally produces believable pacing.

---

# Action Planning

Actions should satisfy the following characteristics:

* Purposeful
* Believable
* Physically achievable
* Narratively meaningful
* Consistent with character intent

Actions should avoid unnecessary complexity whenever a simpler sequence communicates the same story.

---

# Action Budget

Every scene has limited temporal capacity.

The planner estimates an Action Budget based on available scene duration.

The Action Budget is a planning heuristic rather than a fixed numerical limit.

Its purpose is to encourage realistic pacing.

Example considerations include:

* Scene duration
* Number of significant actions
* Character count
* Environmental complexity
* Required viewer comprehension

The planner should avoid exceeding the practical Action Budget of the scene.

---

# Cognitive Load

Current AI video generation models possess finite reasoning capacity.

The planner should avoid unnecessarily increasing cognitive load.

Factors that increase cognitive load include:

* Multiple simultaneous actions
* Large numbers of interacting characters
* Rapid environmental changes
* Frequent camera changes
* Numerous important objects
* Competing visual priorities

Reducing cognitive load generally improves rendering reliability while preserving story clarity.

---

# Viewer Outcome

Every scene should conclude with a clearly defined Viewer Outcome.

The Viewer Outcome answers one question:

> **What should the audience understand when the scene ends?**

Examples include:

* The repair succeeded.
* The escape failed.
* The friendship strengthened.
* The danger increased.
* The mystery deepened.

Every major planning decision should support the intended Viewer Outcome.

---

# Camera Intent

The planner defines narrative camera intent rather than camera mechanics.

Camera Intent communicates what deserves the audience's attention.

Examples include:

* Observe interaction
* Reveal information
* Emphasize emotion
* Follow movement
* Highlight an important object

The Rendering Engine later determines how this intent is expressed for the selected rendering pipeline.

---

# Constraints

The planner identifies conditions that must remain true throughout the scene.

Examples include:

* Character identity
* Story continuity
* Locked objects
* Environmental consistency
* Required visual elements

Constraints preserve narrative coherence while allowing rendering flexibility.

---

# Continuity Validation

Before completing the Scene Model, the planner validates internal consistency.

Validation includes:

* Character continuity
* Story state continuity
* Environmental consistency
* Object consistency
* Goal consistency
* Action consistency

The planner should resolve contradictions before handing the Scene Model to the Rendering Engine.

---

# Scene Model Completion

A Scene Model is considered complete when it contains sufficient semantic understanding for rendering.

Completion does not require prompt wording.

Completion requires narrative understanding.

Once validated, the completed Scene Model becomes the authoritative semantic representation of the planned scene and is passed to Module 09 – Rendering Engine.

---

# Internal Planning Rules

The following rules govern every planning decision made by the Scene Planner.

These rules are intended to preserve architectural consistency rather than define implementation details.

---

## Rule 1 — Preserve Story Intent

The planner shall preserve the user's intended story.

Rendering limitations must never alter narrative intent.

When simplification becomes necessary, the planner should simplify execution while preserving meaning.

---

## Rule 2 — Build Before Refining

Planning should proceed from high-level understanding toward increasing semantic detail.

The planner should never optimize actions before understanding the purpose of the scene.

---

## Rule 3 — One Scene, One Primary Goal

Each scene should pursue one dominant Scene Goal.

Secondary actions should support the primary objective rather than compete with it.

---

## Rule 4 — Actions Require Purpose

Every significant action should contribute toward:

* advancing the story,
* achieving the Scene Goal,
* revealing information,
* developing a character, or
* improving audience understanding.

Actions without narrative value should be removed.

---

## Rule 5 — Maintain Narrative Continuity

Characters, environments, objects, and story state should remain internally consistent.

Unexpected changes require explicit narrative justification.

---

## Rule 6 — Respect Action Budget

The planner should avoid exceeding the practical complexity of the scene.

When necessary, simplify action sequences before simplifying story intent.

---

## Rule 7 — Minimize Cognitive Load

The planner should avoid unnecessary simultaneous complexity.

Preference should be given to sequential, readable progression over competing visual events.

---

## Rule 8 — Preserve Viewer Understanding

Every planning decision should improve the audience's ability to understand the intended story outcome.

---

# Planner Validation

Before a Scene Model is considered complete, the planner should validate the following questions.

## Narrative Validation

* Is the Story Goal understood?
* Is the Scene Goal clearly defined?
* Does every action support the Scene Goal?
* Is the Viewer Outcome clearly identifiable?

---

## Character Validation

* Are all required characters present?
* Are character identities consistent?
* Are character motivations understandable?
* Are relationships preserved?

---

## Environment Validation

* Is the environment consistent?
* Does the environment support the planned actions?
* Are environmental constraints respected?

---

## Action Validation

* Does the Action Graph contain logical dependencies?
* Are actions believable?
* Are actions physically achievable?
* Does the Action Budget appear realistic?

---

## Continuity Validation

* Is Story State preserved?
* Are objects consistent?
* Are important constraints maintained?
* Are there contradictions between planning stages?

---

## Rendering Readiness

The planner does **not** validate rendering implementation.

Instead, it verifies that the Scene Model contains sufficient semantic understanding for the Rendering Engine to perform its responsibilities.

---

# Output Contract

The Scene Planner produces exactly one primary artifact:

> **Scene Model**

The Scene Model contains semantic understanding rather than rendering instructions.

Typical information includes:

* Story Context
* Story Goal
* Scene Goal
* Characters
* Environment
* Story State
* Objects
* Action Graph
* Camera Intent
* Constraints
* Viewer Outcome
* Rendering Hints

The Scene Model intentionally excludes:

* Prompt wording
* Backend parameters
* Prompt Relay configuration
* Identity consistency techniques
* Rendering implementation details

These belong to the Rendering Engine.

---

# Handoff to Module 09

Once the Scene Model has been validated, ownership transfers to:

> **Module 09 – Rendering Engine**

The Rendering Engine enriches the Scene Model by producing a Rendering Specification suitable for the reference rendering pipeline.

The planner does not participate in backend-specific rendering decisions.

---

# Relationship to Other Modules

The Scene Planner collaborates closely with:

* Module 03 – Request Analysis
* Module 04 – Character Engine
* Module 05 – World Engine
* Module 06 – Story State Engine
* Module 09 – Rendering Engine
* Module 10 – Validation Engine

Each module owns a distinct responsibility.

The Scene Planner integrates their semantic understanding but does not replace their individual responsibilities.

---

# Architectural Summary

The Scene Planner serves as the narrative reasoning layer of Video Story Director.

It transforms story intent into a backend-independent Scene Model through progressive semantic reasoning.

The planner focuses exclusively on understanding **what** should happen.

The Rendering Engine is responsible for determining **how** that understanding is expressed through the selected rendering pipeline.

Maintaining this separation enables rendering technologies to evolve without altering the planner's narrative intelligence.

---

# Future Evolution

Future versions of the Scene Planner may incorporate additional reasoning strategies, planning heuristics, or empirical improvements.

Such enhancements should strengthen semantic understanding while preserving the architectural principles defined by this module.

The Scene Model should remain the canonical planning artifact throughout the evolution of Video Story Director.

---

# Guiding Principle

> **Think like a director.
> Reason like a planner.
> Render through abstraction.**
