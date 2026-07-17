# Scene Planning Philosophy

> **Status:** Draft (v1.2.0)
>
> **Applies to:** Video Story Director v1.2.x

---

# Purpose

Scene Planning is the intellectual core of Video Story Director.

Its purpose is not to write prompts.

Its purpose is to understand a story, reason about what should happen, and construct a coherent Scene Model that can be rendered consistently by AI video generation systems.

Scene Planning exists to answer one question:

> **What should happen, and why?**

Everything that follows in the rendering pipeline exists to communicate that understanding to a rendering backend.

---

# Philosophy

Video Story Director approaches scene planning as a film director rather than a prompt writer.

A director does not think in sentences.

A director thinks in stories.

They understand the purpose of a scene, determine what the audience should experience, decide how the characters behave, and only then consider how the scene should be filmed.

Likewise, Scene Planning separates narrative reasoning from rendering implementation.

The planner never writes prompts.

The planner builds understanding.

---

# Primary Objective

The objective of Scene Planning is to transform story intent into a complete Scene Model.

The Scene Model becomes the authoritative understanding of the scene.

Every later stage of the rendering pipeline operates from this shared understanding.

---

# Core Principles

## 1. Story Before Rendering

Rendering exists to communicate the story.

The planner must never change the story to satisfy rendering preferences.

Rendering adapts to the story—not the other way around.

---

## 2. Goals Before Actions

Every scene exists to accomplish something.

Actions are meaningful only when they contribute toward a scene goal.

Planning therefore begins with intent rather than motion.

---

## 3. Believability Before Complexity

A believable scene is more valuable than a complicated scene.

When multiple solutions exist, the planner should favor the simplest sequence that naturally communicates the intended outcome.

---

## 4. Continuity Before Novelty

Characters, environments, objects, and story state should remain internally consistent.

Unexpected changes should occur only when explicitly required by the story.

---

## 5. Clarity Before Detail

The audience should easily understand what is happening.

Additional details should strengthen understanding rather than distract from it.

---

# Planning Responsibilities

Scene Planning is responsible for:

* Understanding narrative intent.
* Defining scene goals.
* Building the Scene Model.
* Planning believable action sequences.
* Maintaining continuity.
* Estimating realistic pacing.
* Preparing scenes for rendering.

Scene Planning is not responsible for:

* Prompt wording.
* Backend-specific optimizations.
* Identity consistency techniques.
* Rendering parameters.
* Prompt Relay.
* MSR.
* IC-LoRA.

These belong to the Rendering Engine.

---

# Planning Pipeline

Every planned scene follows the same reasoning process.

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
Build Action Graph
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

This process emphasizes reasoning before expression.

---

# Scene Goals

Every scene should have a single primary objective.

Examples include:

* Obtain an object.
* Escape a location.
* Introduce a character.
* Reveal information.
* Resolve a conflict.

Large narrative objectives should be decomposed into smaller scene goals whenever possible.

---

# Action Graph

Actions should form a logical progression rather than an isolated list.

Each action should naturally enable the next.

Example:

```text
Inspect
    ↓
Reach
    ↓
Grab
    ↓
Repair
    ↓
Verify
```

This structure reflects how humans naturally perform tasks and improves the likelihood of coherent video generation.

---

# Viewer Outcome

Every scene should answer one question:

> **What should the audience understand when this scene ends?**

The planner should ensure that every major action contributes toward communicating that outcome.

---

# Action Budget

Scene Planning recognizes that every scene has limited temporal capacity.

The planner should estimate an appropriate amount of meaningful action based on the available duration.

This estimate is a planning heuristic rather than a strict limitation.

Its purpose is to encourage realistic pacing and improve rendering reliability.

---

# Cognitive Load

Current video generation models have finite capacity for interpreting complex scenes.

The planner should avoid unnecessarily increasing cognitive load by requesting excessive simultaneous motion, unrelated actions, abrupt environmental changes, or competing visual priorities.

Whenever possible, complexity should emerge from coherent progression rather than simultaneous events.

---

# Scene Model

The Scene Model is the canonical output of Scene Planning.

It represents the planner's complete understanding of the scene independently of any rendering backend.

The Scene Model contains semantic understanding rather than prompt wording.

Typical information includes:

* Story goals.
* Scene goals.
* Characters.
* Environment.
* Objects.
* Story state.
* Action graph.
* Camera intent.
* Duration.
* Constraints.
* Viewer outcome.

The Scene Model becomes the authoritative input for the Rendering Engine.

---

# Relationship to Rendering

Scene Planning ends when the Scene Model is complete.

Rendering begins when the Rendering Engine transforms the Scene Model into a Rendering Specification.

The planner determines **what** should happen.

The Rendering Engine determines **how** that understanding is expressed for the selected rendering pipeline.

Maintaining this separation preserves architectural clarity and allows rendering technologies to evolve independently of narrative reasoning.

---

# Future Evolution

Future versions of Video Story Director may improve planning intelligence through additional reasoning techniques, heuristics, or empirical validation.

Such improvements should strengthen the planner's understanding while preserving the core principles defined in this document.

The philosophy of Scene Planning is intended to remain stable even as implementation continues to evolve.
