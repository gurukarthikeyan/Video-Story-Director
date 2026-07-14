# LTX Story Director - Design Philosophy

## Purpose

LTX Story Director is a cinematic planning framework designed to transform a simple user idea into one or more connected video scenes suitable for text-to-video models.

It does not merely expand prompts.

It acts as a virtual director.

Its primary responsibility is maintaining visual continuity, cinematic clarity, and story progression across multiple scenes.

---

## Core Principles

### 1. Story Before Description

The framework first understands the story.

Visual descriptions exist only to support the story.

---

### 2. Characters Are Persistent

Every character has a stable identity.

Appearance, clothing, proportions, accessories, and movement style remain consistent unless the story explicitly changes them.

---

### 3. The World Has Memory

Objects do not teleport.

Lighting does not randomly change.

Weather does not randomly change.

Environment changes only when justified by the story.

---

### 4. Every Scene Has One Job

A scene should complete one clear visual objective.

It should never attempt to tell an entire story.

---

### 5. Frame 0 Is Sacred

The first frame is a photograph.

It contains no motion.

It establishes the exact visual state from which animation begins.

---

### 6. Motion Starts After Frame 0

Every LTX prompt begins immediately after the first frame.

The first sentence always represents the first visible movement.

---

### 7. Continuity Is Mandatory

Every new scene inherits the previous scene.

Characters

Objects

Environment

Lighting

Camera

Story state

All persist unless intentionally changed.

---

### 8. Visual Language Only

Describe only what can be seen.

Avoid internal thoughts.

Avoid narration.

Avoid backstory.

Avoid literary writing.

---

### 9. Cinematic Simplicity

Prefer simple visual actions over complex descriptions.

One sentence should describe one visual event.

---

### 10. Model Agnostic Design

Story Director is independent of any video model.

Adapters convert Story Director output into LTX, Wan, Veo, Kling, or future formats.

The directing intelligence remains the same.