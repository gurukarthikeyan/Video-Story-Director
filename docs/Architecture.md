# Story Director Architecture

## Overview

Story Director is built as a collection of independent reasoning engines.

Each engine has one responsibility.

Each engine produces information used by the next engine.

This modular design improves reasoning quality, simplifies maintenance, and allows future expansion without rewriting the entire prompt.

---

## Processing Pipeline

User Request

↓

Story Planner

↓

Character Engine

↓

World Engine

↓

Story State Engine

↓

Scene Planner

↓

Frame 0 Engine

↓

LTX Prompt Engine

↓

Validation Engine

↓

Output Formatter

---

## Engine Responsibilities

### Story Planner

Determines:

- Beginning
- Middle
- Ending
- Scene goals

---

### Character Engine

Creates persistent character identities.

Defines:

- appearance
- clothing
- proportions
- movement
- personality
- recognition traits

---

### World Engine

Creates the persistent world.

Defines:

- environment
- lighting
- weather
- time of day
- important props

---

### Story State Engine

Tracks everything that changes.

Maintains:

- characters
- objects
- environment
- camera
- timeline

This engine is responsible for continuity.

---

### Scene Planner

Breaks the story into scenes.

Each scene has one visual objective.

---

### Frame 0 Engine

Generates a completely static first frame.

No motion.

No future events.

Only visual state.

---

### LTX Prompt Engine

Generates motion beginning immediately after Frame 0.

Uses chronological actions.

Simple visual language.

---

### Validation Engine

Checks:

- continuity
- consistency
- action budget
- duration
- camera rules
- scene transitions

---

### Output Formatter

Produces the final response using the required output contract.

No additional commentary.