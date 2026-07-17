# GS-001 — Single Character Sequential Actions

> **Scenario ID:** GS-001
>
> **Version:** 1.0
>
> **Status:** Active
>
> **Benchmark Suite:** Golden Scenarios
>
> **Difficulty:** L1
>
> **Primary Verification:** Temporal Adherence
>
> **Related Documents**
>
> * ../../scenario_template.md
> * ../../benchmark_matrix.md
> * ../../verification_dimensions.md
> * ../../../docs/design/scene_model.md
> * ../../../docs/design/rendering_specification.md

---

# Purpose

GS-001 is the baseline verification scenario for the Video Story Director project.

It verifies that the complete rendering pipeline correctly translates a simple user request into a coherent video while preserving narrative order, temporal sequencing, character consistency, and environmental stability.

This scenario intentionally minimizes complexity and serves as the reference baseline for future capability verification, including Prompt Relay, MSR, IC-LoRA, and backend comparisons.

---

# Scenario Metadata

| Field           | Value                               |
| --------------- | ----------------------------------- |
| Scenario ID     | GS-001                              |
| Name            | Single Character Sequential Actions |
| Benchmark Suite | Golden Scenarios                    |
| Difficulty      | L1                                  |
| Status          | Active                              |
| Version         | 1.0                                 |

---

# Reference Assets

## Character

| Asset           | Value                                                               |
| --------------- | ------------------------------------------------------------------- |
| Character ID    | C001                                                                |
| Asset           | C001_young_woman                                                    |
| Character Sheet | `evaluation/assets/characters/C001_young_woman/character_sheet.png` |
| First Frame     | `evaluation/assets/characters/C001_young_woman/first_frame.png`     |

---

## Background

| Asset            | Value                                                         |
| ---------------- | ------------------------------------------------------------- |
| Background ID    | B001                                                          |
| Asset            | B001_city_park                                                |
| Background Image | `evaluation/assets/backgrounds/B001_city_park/background.png` |

---

# Pipeline Configuration

| Component      | Configuration      |
| -------------- | ------------------ |
| Backend        | LTX 2.3            |
| Prompt Relay   | Disabled           |
| MSR            | Disabled           |
| IC-LoRA        | Disabled           |
| Audio Planning | Disabled           |
| Rendering Mode | Baseline Reference |

This configuration establishes the canonical baseline against which future capability-specific benchmarks will be compared.

---

# User Request

> A young woman stands in a quiet city park on a sunny afternoon. She smiles warmly toward the camera, raises her right hand, waves twice, lowers her hand, turns to her left, and walks slowly along the park path.

---

# Expected Scene Model

## Narrative Summary

A single character greets the viewer before calmly leaving the scene.

---

## Characters

| Property | Value       |
| -------- | ----------- |
| Count    | 1           |
| Identity | Young Woman |
| Emotion  | Friendly    |
| State    | Calm        |

---

## Environment

| Property            | Value            |
| ------------------- | ---------------- |
| Location            | City Park        |
| Weather             | Sunny            |
| Lighting            | Natural Daylight |
| Crowd               | None             |
| Environment Changes | None             |

---

## Story Goal

The character performs a brief greeting before departing.

---

# Expected Rendering Specification

## Character

* Stable identity
* Consistent clothing
* Consistent hairstyle
* Natural facial expressions
* Smooth body motion

---

## Background

* Persistent environment
* Stable lighting
* No scene transitions
* No additional people
* No unexpected objects

---

## Camera

### Global Camera

* Mid Shot
* Eye Level
* Locked Camera
* Static Framing
* Natural Perspective

No camera movement should occur during this scenario.

---

# Expected Action Timeline

| Time   | Expected Action            |
| ------ | -------------------------- |
| 0–2 s  | Stand naturally and smile  |
| 2–3 s  | Raise right hand           |
| 3–5 s  | Wave twice                 |
| 5–6 s  | Lower right hand           |
| 6–7 s  | Turn left                  |
| 7–10 s | Walk slowly along the path |

Actions should occur sequentially without overlap or omission.

---

# Expected Rendering Package

## Character Assets

* Character Sheet
* First Frame

---

## Environment Assets

* Background Image

---

## Prompt Configuration

Global Prompt only.

No Prompt Relay segmentation.

---

# Verification Focus

## Primary Verification

* Temporal Adherence

---

## Secondary Verification

* Motion Quality
* Identity Consistency
* Background Consistency
* Narrative Order

---

# Success Criteria

The scenario is considered successful if:

* All actions occur in the correct order.
* Exactly two waves are performed.
* The right hand is used for waving.
* Character identity remains visually consistent.
* The background remains stable throughout the video.
* Character motion appears smooth and natural.
* No unintended actions are introduced.
* No unexpected camera movement occurs.

---

# Failure Modes

Potential failures include:

* Missing actions.
* Incorrect action order.
* Incorrect hand used.
* More or fewer than two waves.
* Character identity drift.
* Clothing or hairstyle changes.
* Background inconsistency.
* Camera movement.
* Hallucinated objects.
* Hallucinated characters.
* Animation instability.

---

# Required Evidence

Each execution should produce:

* Generated video
* Frame 0 image
* Final frame image
* Rendering logs
* Generation parameters
* Verification report
* Reviewer observations

---

# Expected Verification Dimensions

| Dimension              | Priority |
| ---------------------- | -------- |
| Temporal Adherence     | High     |
| Narrative Adherence    | High     |
| Motion Quality         | High     |
| Character Consistency  | Medium   |
| Background Consistency | Medium   |
| Camera Stability       | Medium   |
| Visual Quality         | Medium   |

---

# Benchmark Usage

GS-001 serves as the canonical baseline for:

* Pipeline regression testing
* Backend comparison
* Prompt Relay comparison
* MSR comparison
* IC-LoRA comparison
* Future rendering capability evaluation

Future capability benchmarks should reuse the same reference assets whenever possible to isolate the effect of the capability under test.

---

# Execution Procedure

1. Load the reference assets.
2. Configure the baseline pipeline.
3. Generate the Rendering Package.
4. Render the video using the reference backend.
5. Record generation parameters.
6. Complete the Verification Report.
7. Archive all generated artifacts.

---

# Expected Output

The final video should depict a friendly young woman greeting the viewer with two distinct waves before calmly turning and walking along the park path.

The resulting sequence should appear natural, temporally coherent, visually stable, and free of unintended motion or scene changes.

---

# Notes

This scenario intentionally excludes Prompt Relay, MSR, IC-LoRA, camera motion, dialogue, environmental changes, and multi-character interactions.

It establishes the simplest complete end-to-end verification of the Video Story Director architecture and serves as the reference baseline for all future capability-specific benchmark scenarios.
