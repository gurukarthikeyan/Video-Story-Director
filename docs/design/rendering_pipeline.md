# Rendering Pipeline

> **Status:** Draft (v1.2.0)
>
> **Applies to:** Video Story Director v1.2.x
>
> **Current Reference Backend:** LTX 2.3

---

# Purpose

This document defines the rendering pipeline used by Video Story Director.

The rendering pipeline is responsible for transforming an approved story plan into a backend-specific rendering request while preserving story intent, character identity, temporal consistency, and visual continuity.

This document describes the architectural responsibilities of each stage in the pipeline. It intentionally does not specify implementation details.

---

# Design Goals

The rendering pipeline is designed around the following principles:

* Preserve story intent throughout rendering.
* Separate story reasoning from rendering implementation.
* Maintain character identity across all generated frames.
* Maximize temporal prompt adherence.
* Support optional conditioning techniques without coupling them to story planning.
* Remain extensible for future rendering technologies.

---

# Reference Rendering Pipeline

```text
User Request
        │
        ▼
Story Understanding
        │
        ▼
Scene Planning
        │
        ▼
Rendering Specification
        │
        ▼
Prompt Relay
        │
        ▼
MSR Identity Consistency
        │
        ▼
Optional IC-LoRA Conditioning
        │
        ▼
LTX Rendering Backend
        │
        ▼
Generated Video
```

This pipeline represents the reference implementation for Video Story Director v1.2.

Future rendering backends may replace the final rendering stage while preserving the preceding planning and rendering workflow.

---

# Scene Model

The Scene Model is the canonical internal representation of a planned scene.

It captures the planner's complete understanding of the scene independently of any rendering backend.

The Scene Model contains semantic knowledge rather than prompt wording.

Typical information includes:

- Story goals
- Scene goals
- Characters
- Environment
- Objects
- Action graph
- Camera intent
- Duration
- Continuity constraints
- Viewer outcome

The Scene Model is consumed by the Rendering Engine, which converts it into a backend-specific Rendering Specification.

The Scene Model is never exposed directly to a rendering backend.

---

# Pipeline Stages

## 1. Story Understanding

Purpose:

Understand the user's narrative intent.

Responsibilities:

* Interpret the requested story.
* Identify characters.
* Identify environments.
* Determine scene objectives.
* Resolve ambiguities where possible.

Output:

Structured story intent.

---

## 2. Scene Planning

Purpose:

Convert story intent into a realistic sequence of events.

Responsibilities:

* Define scene goals.
* Plan action order.
* Maintain continuity.
* Respect duration constraints.
* Produce actions that current video models can realistically generate.

The planner answers:

> **What should happen?**

Output:

Rendering specification.

---

## 3. Rendering Specification

Purpose:

Describe the planned scene independently of any rendering backend.

Responsibilities:

* Preserve planned actions.
* Preserve story goals.
* Preserve continuity.
* Describe required camera behavior.
* Describe visual constraints.

This representation remains backend independent.

The Rendering Specification is the contract between planning and rendering.

---

## 4. Prompt Relay

Purpose:

Improve temporal prompt adherence.

Responsibilities:

* Propagate prompt intent throughout video generation.
* Reinforce planned actions over time.
* Reduce prompt drift.
* Preserve scene objectives across temporal segments.

Prompt Relay does not modify story intent.

It reinforces the Rendering Specification during generation.

---

## 5. MSR Identity Consistency

Purpose:

Maintain stable character identity.

Responsibilities:

* Preserve facial identity.
* Preserve appearance.
* Preserve clothing.
* Preserve hairstyle.
* Preserve identity across the entire sequence.

MSR is considered the primary identity consistency mechanism for the reference pipeline.

---

## 6. Optional IC-LoRA Conditioning

Purpose:

Provide additional conditioning signals.

Possible conditioning includes:

* Pose
* Depth
* Motion
* Camera guidance
* Structural constraints

IC-LoRA supplements rendering.

It does not replace MSR.

---

## 7. Rendering Backend

Current implementation:

LTX 2.3

Responsibilities:

* Translate the Rendering Specification into backend-compatible prompts.
* Execute video generation.
* Apply backend-specific optimizations.
* Respect backend capabilities and limitations.

The backend should never change story intent.

Its responsibility is limited to translating and executing the rendering request.

---

# Responsibility Boundaries

## Story Planner

Responsible for:

* Story reasoning
* Action planning
* Scene goals
* Continuity

Not responsible for:

* Prompt Relay
* Identity consistency
* Backend optimization

---

## Rendering Engine

Responsible for:

* Rendering Specification
* Pipeline orchestration
* Prompt Relay integration
* Identity consistency integration
* Optional conditioning
* Backend execution

Not responsible for:

* Story planning
* Narrative decisions

---

## Backend

Responsible for:

* Prompt translation
* Model-specific formatting
* Generation execution

Not responsible for:

* Story reasoning
* Planning
* Narrative interpretation

---

# Design Principles

## Story First

Rendering must never alter story intent.

---

## Planner Driven

Rendering follows the planner.

The planner never follows backend limitations directly.

---

## Backend Isolation

Backend-specific behavior remains isolated from planning logic.

---

## Identity Preservation

Character identity is treated as a rendering concern rather than a planning concern.

---

## Temporal Consistency

Prompt adherence should remain stable throughout the entire rendered sequence.

---

## Extensibility

The rendering pipeline should allow new rendering technologies to replace individual stages without requiring architectural redesign.

---

# Current Reference Implementation

The current rendering pipeline targets:

* LTX 2.3
* Prompt Relay
* MSR
* Optional IC-LoRA

This configuration serves as the empirical reference implementation for Video Story Director v1.2.

Future backend support will be evaluated only after the reference implementation demonstrates stable improvements in prompt adherence, identity consistency, and temporal continuity.

---

# Future Considerations

Potential future enhancements include:

* Additional rendering backends.
* Alternative identity consistency methods.
* Advanced conditioning techniques.
* Automated rendering capability detection.
* Rendering optimization passes.

These enhancements should preserve the architectural principles defined in this document.
