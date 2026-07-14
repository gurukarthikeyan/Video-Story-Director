# Story State Engine

## Purpose

The Story State Engine maintains continuity across every connected scene.

Instead of recreating the story from scratch, every scene inherits the complete visual state of the previous scene.

The engine updates only the elements that change.

---

## Persistent State

The following categories always exist.

Character State

Object State

Environment State

Camera State

Timeline State

---

## Character State

Tracks

- appearance
- clothing
- accessories
- body condition
- pose
- emotional state
- position
- object ownership

Example

Baby

holding:
Cookie

expression:
Happy

location:
Kitchen Counter

---

## Object State

Tracks

- owner
- location
- condition
- orientation
- visibility

Example

Cookie Dough

Location:
Floor

Condition:
Splattered

Owner:
None

---

## Environment State

Tracks

- location
- lighting
- weather
- atmosphere
- destruction
- important environmental changes

---

## Camera State

Tracks

- framing
- height
- angle
- movement
- lens feel

If unchanged,

inherit.

---

## Timeline State

Tracks

Story progression.

Every scene begins exactly where the previous scene ended.

No unexplained jumps.

No resetting actions.

---

## Inheritance Rules

Before creating Scene N

inherit

Character State

↓

Object State

↓

Environment State

↓

Camera State

↓

Timeline State

Apply only the changes introduced by Scene N.

Everything else remains identical.

---

## Continuity Priority

If context becomes limited,

preserve information in this order.

1 Characters

2 Story

3 Objects

4 Environment

5 Camera

6 Decorative Details

Never sacrifice higher-priority information to preserve lower-priority information.

---

## Engine Philosophy

Do not recreate.

Do not reinterpret.

Do not redesign.

Only update.