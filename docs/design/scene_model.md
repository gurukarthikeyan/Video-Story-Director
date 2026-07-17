# Scene Model

> **Status:** Draft (v1.2.0)
>
> **Applies to:** Video Story Director v1.2.x

---

# Purpose

The Scene Model is the canonical internal representation of a planned scene.

It captures the planner's complete understanding of a scene independently of any rendering backend, prompt format, or implementation detail.

The Scene Model is the primary contract between Scene Planning and the Rendering Engine.

It represents **knowledge**, not **language**.

---

# Philosophy

The Scene Model is not a prompt.

It is not backend-specific.

It is not tied to any particular AI video model.

Instead, it describes everything that Video Story Director understands about a scene before rendering begins.

Rendering technologies may evolve.

The Scene Model should remain stable.

---

# Objectives

The Scene Model exists to:

* Preserve story intent.
* Represent scene understanding.
* Separate planning from rendering.
* Enable backend-independent reasoning.
* Provide a stable contract for future rendering technologies.

---

# Design Principles

## Semantic First

The Scene Model represents meaning rather than wording.

It answers what exists and what should happen, rather than how it should be described.

---

## Backend Independent

The Scene Model contains no backend-specific instructions.

It should remain valid regardless of the rendering technology used.

---

## Stable Contract

Scene Planning produces the Scene Model.

The Rendering Engine consumes it.

Neither component should depend on implementation details of the other.

---

## Incrementally Refinable

The Scene Model may become progressively more detailed during planning.

Additional reasoning should enrich the model rather than replace earlier understanding.

---

## Deterministic

Given the same story and planning decisions, the resulting Scene Model should describe the same scene regardless of rendering backend.

---

# Conceptual Structure

The Scene Model consists of several conceptual domains.

These domains describe the complete understanding of a planned scene.

---

## Story Context

Describes where this scene exists within the larger story.

Examples include:

* Story objective
* Scene objective
* Narrative context
* Previous scene state
* Expected ending state

---

## Characters

Describes all participating characters.

Examples include:

* Primary character
* Supporting characters
* Relationships
* Identity
* Roles

The Scene Model describes who exists.

Identity preservation remains the responsibility of the Rendering Engine.

---

## Environment

Describes the setting in which the scene occurs.

Examples include:

* Location
* Time
* Weather
* Lighting
* Atmosphere
* Environmental constraints

---

## Objects

Describes significant objects required by the scene.

Examples include:

* Props
* Tools
* Vehicles
* Interactive objects

Only objects relevant to the planned scene should be represented.

---

## Story State

Represents the current state of the world.

Examples include:

* Character locations
* Object locations
* Completed actions
* Pending objectives
* Continuity information

This enables future scenes to reason about continuity.

---

## Action Graph

Represents the logical progression of actions required to achieve the scene goal.

Unlike a simple ordered list, an Action Graph captures dependency.

Example:

Inspect

↓

Reach

↓

Grab Tool

↓

Repair

↓

Verify

Each action should naturally enable the next.

---

## Camera Intent

Describes what the audience should observe.

Examples include:

* Observe interaction
* Reveal information
* Follow movement
* Emphasize emotion
* Focus on an important object

Camera Intent describes narrative purpose rather than camera mechanics.

---

## Constraints

Describes conditions that must remain true.

Examples include:

* Character identity
* Story continuity
* Environmental consistency
* Locked objects
* Required visual elements

Constraints help preserve coherence throughout rendering.

---

## Viewer Outcome

Defines what the audience should understand when the scene concludes.

Examples include:

* The repair succeeded.
* The character escaped.
* The relationship changed.
* The danger increased.

Every planned scene should communicate a clear outcome.

---

## Rendering Hints

Rendering Hints communicate semantic characteristics of the scene without referencing any specific backend.

Examples include:

* High motion
* Dialogue focused
* Emotional interaction
* Object manipulation
* Environmental emphasis

These hints assist the Rendering Engine in selecting an appropriate rendering strategy.

---

# Ownership

## Produced By

Scene Planning

---

## Consumed By

Rendering Engine

---

## Extended By

Rendering Specification

The Rendering Engine enriches the Scene Model with rendering-specific information while preserving the underlying semantic understanding.

---

# Relationship to Rendering Specification

The Scene Model describes **what the scene is**.

The Rendering Specification describes **how the scene should be rendered**.

This separation allows planning intelligence to evolve independently of rendering technologies.

---

# Progressive Refinement

Scene Planning should construct the Scene Model through successive refinement.

A typical reasoning process may include:

Story Understanding

↓

Scene Goal

↓

Characters

↓

Environment

↓

Story State

↓

Action Graph

↓

Constraints

↓

Viewer Outcome

↓

Rendering Preparation

Each refinement step adds knowledge while preserving consistency with previous decisions.

---

# Architectural Role

The Scene Model is the central semantic artifact within Video Story Director.

It provides a common language shared by planning, rendering, evaluation, and future extensions.

Maintaining a stable Scene Model allows rendering technologies, prompting strategies, identity consistency techniques, and backend implementations to evolve without altering the planner's understanding of the story.

---

# Future Evolution

Future versions of Video Story Director may extend the Scene Model with additional semantic concepts as rendering technologies mature.

Such extensions should strengthen scene understanding while preserving the architectural principles defined in this document.

The Scene Model should remain backend-independent and continue serving as the authoritative representation of narrative understanding throughout the rendering pipeline.
