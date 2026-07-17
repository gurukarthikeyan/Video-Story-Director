# Scenario Template

> **Version:** v1.2.0
>
> **Status:** Active
>
> **Purpose:** Define the standard structure for all verification scenarios used by the Video Story Director Evaluation Framework.
>
> **Related Documents**
>
> * README.md
> * benchmark_matrix.md
> * verification_dimensions.md
> * verification_report_template.md
> * ../design/scene_model.md
> * ../design/rendering_specification.md

---

# Purpose

Every verification scenario should follow a consistent structure.

A standardized scenario template ensures:

* Consistent documentation
* Repeatable execution
* Comparable verification results
* Simplified maintenance
* Easier expansion of benchmark suites

This template applies to:

* Golden Scenarios
* Capability Verification Scenarios
* Exploratory Scenarios
* Future benchmark suites

---

# Scenario Metadata

| Field           | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| Scenario ID     | Unique identifier (e.g., GS-001, PR-001, MSR-001)            |
| Scenario Name   | Human-readable name                                          |
| Benchmark Suite | Golden, Prompt Relay, MSR, IC-LoRA, Exploratory, Performance |
| Difficulty      | L1–L5                                                        |
| Status          | Draft, Active, Deprecated                                    |
| Version         | Scenario version                                             |

---

# Purpose

Briefly describe:

* What this scenario verifies.
* Why it exists.
* Which capability is being evaluated.

Every scenario should define **one primary verification objective**.

---

# User Request

Document the original user request that drives the scenario.

This should represent a realistic production request rather than an artificial benchmark whenever possible.

---

# Pipeline Configuration

Specify the expected pipeline configuration.

Example fields:

| Field                   | Value              |
| ----------------------- | ------------------ |
| Reference Backend       |                    |
| Prompt Relay            | Enabled / Disabled |
| MSR                     | Enabled / Disabled |
| IC-LoRA                 | Enabled / Disabled |
| Additional Capabilities |                    |

Only include the capabilities required for this scenario.

---

# Expected Architectural Artifacts

Reference or summarize the expected artifacts.

## Scene Model

Expected narrative understanding.

---

## Rendering Specification

Expected rendering instructions.

---

## Rendering Package

Expected backend inputs.

---

# Verification Focus

## Primary Verification

The principal capability being evaluated.

Examples:

* Identity Consistency
* Temporal Adherence
* Camera Adherence
* Motion Quality

---

## Secondary Verification

Supporting verification dimensions.

These provide additional observations but are not the primary success criteria.

---

# Success Criteria

Define measurable conditions for a successful outcome.

Examples:

* Character identity remains consistent.
* Camera follows planned movement.
* Segment timing matches specification.
* Narrative order is preserved.

Success criteria should be observable and repeatable.

---

# Failure Modes

Document expected failure conditions.

Examples:

* Identity drift
* Incorrect camera framing
* Missed actions
* Incorrect temporal ordering
* Background inconsistency
* Prompt Relay timing errors
* Rendering artifacts

This section supports systematic diagnosis.

---

# Required Evidence

Specify the evidence that should accompany the scenario.

Examples:

* Generated video
* Key frames
* Character Sheets
* Background images
* Rendering logs
* Verification Report

Evidence enables independent review and future regression analysis.

---

# Notes

Record any additional observations, assumptions, constraints, or implementation details relevant to the scenario.

This section should not contain verification results.

---

# Usage Guidelines

When creating a new scenario:

1. Copy this template.
2. Assign a unique Scenario ID.
3. Define one primary verification objective.
4. Document expected architectural artifacts.
5. Specify success criteria.
6. Execute the scenario.
7. Record results using the Verification Report Template.
8. Store supporting evidence.

Following this process ensures all scenarios remain consistent across the project.

---

# Architectural Summary

The Scenario Template provides the canonical structure for every benchmark within the Video Story Director Evaluation Framework.

By standardizing how scenarios are defined, executed, and documented, the project maintains consistency across Golden Scenarios, capability verification suites, and future benchmark collections while supporting long-term maintainability and repeatable verification.
