# Benchmark Matrix

> **Version:** v1.2.0
>
> **Status:** Active
>
> **Purpose:** Define the complete benchmark strategy for verifying the Video Story Director rendering pipeline.
>
> **Related Documents**
>
> * verification_philosophy.md
> * verification_dimensions.md
> * verification_report_template.md
> * scenario_template.md
> * ../Architecture.md
> * ../design/rendering_pipeline.md
> * ../design/rendering_specification.md

---

# Purpose

The Benchmark Matrix defines the official verification strategy for Video Story Director.

Rather than serving as a collection of independent test cases, the Benchmark Matrix organizes verification into structured benchmark suites that evaluate individual rendering capabilities as well as the complete rendering pipeline.

Its objectives are to:

* Define the official benchmark suites.
* Establish progressive verification complexity.
* Identify the capabilities exercised by each scenario.
* Support repeatable regression testing.
* Provide objective comparison between pipeline versions.

The Benchmark Matrix acts as the master index for all verification scenarios.

---

# Benchmark Philosophy

Benchmarks should verify one primary capability at a time.

Additional capabilities may be exercised, but every benchmark must have a clearly defined primary verification objective.

This principle enables precise diagnosis of failures and objective comparison between rendering pipeline revisions.

---

# Benchmark Categories

Verification scenarios are organized into four benchmark suites.

## 1. Golden Scenarios

Golden Scenarios verify the complete rendering pipeline.

They represent stable reference scenarios that remain consistent throughout the lifetime of the project.

These scenarios are used for:

* Full regression testing
* Release validation
* Pipeline comparison
* End-to-end verification

---

## 2. Capability Verification

Capability benchmarks verify individual rendering capabilities in isolation.

Examples include:

* Prompt Relay
* MSR
* IC-LoRA
* Future rendering capabilities

These benchmarks focus on a single architectural responsibility.

---

## 3. Exploratory Scenarios

Exploratory scenarios evaluate new ideas before they become part of the official benchmark suite.

These scenarios are experimental and may change frequently.

Successful exploratory scenarios may eventually be promoted to Golden Scenarios.

---

## 4. Performance Benchmarks

Performance benchmarks evaluate technical characteristics rather than rendering correctness.

Examples include:

* Generation time
* Memory usage
* VRAM consumption
* Rendering throughput

Performance benchmarks complement functional verification but do not replace it.

---

# Difficulty Levels

Benchmark complexity is classified into five levels.

| Level  | Description                 |
| ------ | --------------------------- |
| **L1** | Single action or operation  |
| **L2** | Sequential actions          |
| **L3** | Multi-character interaction |
| **L4** | Long continuous scenes      |
| **L5** | Complex cinematic sequences |

Difficulty represents scenario complexity rather than rendering quality.

---

# Capability Matrix

The following capabilities may be verified independently or in combination.

| Capability                | Purpose                               |
| ------------------------- | ------------------------------------- |
| Narrative Planning        | Preserve story intent                 |
| Character Identity        | Maintain character consistency        |
| Background Consistency    | Preserve persistent environments      |
| Camera Control            | Execute cinematic camera plans        |
| Motion Planning           | Execute character and object movement |
| Temporal Segmentation     | Preserve action timing                |
| Prompt Relay              | Route temporal prompts correctly      |
| MSR                       | Preserve character identity           |
| IC-LoRA                   | Apply optional conditioning           |
| Audio Planning *(Future)* | Synchronize dialogue and sound        |
| Rendering Backend         | Execute Rendering Package             |
| Runtime Performance       | Measure execution efficiency          |

---

# Golden Scenario Matrix

The following scenarios define the official regression suite.

| ID     | Scenario                | Difficulty | Primary Verification           |
| ------ | ----------------------- | ---------- | ------------------------------ |
| GS-001 | Single Character Action | L1         | Temporal Adherence             |
| GS-002 | Identity Preservation   | L2         | Identity Consistency           |
| GS-003 | Camera Control          | L2         | Camera Adherence               |
| GS-004 | Character Interaction   | L3         | Narrative Adherence            |
| GS-005 | Environment Continuity  | L3         | Environment Consistency        |
| GS-006 | Temporal Sequence       | L4         | Temporal Planning              |
| GS-007 | Long Scene              | L4         | Narrative Continuity           |
| GS-008 | Cinematic Sequence      | L5         | Multi-Dimensional Verification |

Additional Golden Scenarios may be introduced as the project evolves.

---

# Capability Verification Suites

Capability verification is organized independently of the Golden Scenarios.

## Prompt Relay

Examples:

* PR-001 — Single Segment
* PR-002 — Multiple Segments
* PR-003 — Long Timeline
* PR-004 — Overlapping Temporal Events
* PR-005 — Extended Sequence

---

## MSR

Examples:

* MSR-001 — Single Character
* MSR-002 — Multiple Characters
* MSR-003 — Character Rotation
* MSR-004 — Partial Occlusion
* MSR-005 — Long Identity Persistence

---

## IC-LoRA

Examples:

* IC-001 — Pose Conditioning
* IC-002 — Depth Conditioning
* IC-003 — Motion Conditioning
* IC-004 — Combined Conditioning
* IC-005 — Long Sequence Conditioning

---

# Benchmark Progression

Benchmark development should proceed in the following order.

1. Golden Scenario Template
2. GS-001 through GS-008
3. Prompt Relay Verification Suite
4. MSR Verification Suite
5. IC-LoRA Verification Suite
6. Future Capability Verification Suites

This progression establishes a stable regression baseline before validating optional rendering capabilities.

---

# Execution Policy

Verification should be performed according to the following policy.

## Daily Development

Run only the benchmarks affected by the current change.

---

## Feature Completion

Run the complete capability verification suite associated with the modified feature.

Examples:

* Prompt Relay changes → Prompt Relay Suite
* MSR changes → MSR Suite

---

## Release Candidate

Execute the complete Golden Scenario regression suite.

---

## Major Release

Execute:

* Golden Scenarios
* Capability Verification Suites
* Performance Benchmarks

Major releases should only be approved after successful completion of the complete verification process.

---

# Regression Policy

Every architectural or implementation change should be evaluated using repeatable benchmarks.

Regression testing exists to ensure that improvements in one capability do not unintentionally reduce performance in another.

Golden Scenarios provide long-term stability, while capability verification suites allow focused investigation of individual components.

---

# Repository Organization

```text
evaluation/
│
├── README.md
├── benchmark_matrix.md
├── verification_philosophy.md
├── verification_dimensions.md
├── verification_report_template.md
├── scenario_template.md
│
├── capabilities/
│   ├── prompt_relay/
│   ├── msr/
│   ├── ic_lora/
│   └── future/
│
├── scenarios/
│   ├── golden/
│   └── exploratory/
│
└── results/
```

---

# Architectural Summary

The Benchmark Matrix defines the official verification strategy for Video Story Director.

By separating Golden Scenarios, capability verification, exploratory experiments, and performance benchmarks, the project establishes a structured and repeatable approach to validating architectural improvements.

This strategy enables objective comparison of rendering pipelines, supports regression testing, and provides the evidence required for integrating future rendering capabilities while preserving the project's architectural principles.
