# Verification Report Template

> **Version:** v1.2.0
>
> **Status:** Active
>
> **Purpose:** Provide a standardized template for documenting verification experiments performed using the Video Story Director rendering pipeline.
>
> **Related Documents**
>
> * verification_philosophy.md
> * verification_dimensions.md
> * benchmark_matrix.md
> * ../design/scene_model.md
> * ../design/rendering_specification.md
> * ../Architecture.md

---

# Purpose

Every verification experiment should be documented using a consistent structure.

A Verification Report records:

* the scenario being executed,
* the rendering pipeline configuration,
* the generated results,
* the verification outcome,
* and any observations or recommendations.

The objective is to produce repeatable, comparable, and evidence-based records for every significant experiment.

---

# Report Structure

Each report should contain the following sections.

1. Experiment Information
2. Pipeline Configuration
3. Scenario Information
4. Expected Architectural Artifacts
5. Execution Configuration
6. Execution Results
7. Verification Results
8. Failure Analysis
9. Improvement Opportunities
10. Overall Assessment

---

# 1. Experiment Information

Record the identity of the experiment.

| Field         | Description                     |
| ------------- | ------------------------------- |
| Experiment ID | Unique experiment identifier    |
| Date          | Execution date                  |
| Version       | Video Story Director version    |
| Git Branch    | Repository branch               |
| Git Commit    | Commit hash                     |
| Tester        | Person executing the experiment |

---

# 2. Pipeline Configuration

Record the rendering pipeline used for this experiment.

| Field                     | Description                     |
| ------------------------- | ------------------------------- |
| Reference Backend         | Rendering backend               |
| Prompt Relay              | Enabled / Disabled              |
| MSR                       | Enabled / Disabled              |
| IC-LoRA                   | Enabled / Disabled              |
| Additional Capabilities   | Optional rendering capabilities |
| Rendering Package Version | Version identifier              |

This section documents **what pipeline** produced the results.

---

# 3. Scenario Information

Identify the benchmark scenario.

| Field                  | Description                        |
| ---------------------- | ---------------------------------- |
| Scenario ID            | Golden Scenario identifier         |
| Scenario Name          | Benchmark title                    |
| Difficulty Level       | L1–L5                              |
| Primary Verification   | Primary verification dimension     |
| Secondary Verification | Additional verification dimensions |

This section links the experiment to the Benchmark Matrix.

---

# 4. Expected Architectural Artifacts

Reference the expected architectural outputs.

## User Request

Reference or summarize the original user request.

---

## Expected Scene Model

Reference the expected Scene Model.

---

## Expected Rendering Specification

Reference the expected Rendering Specification.

---

## Expected Rendering Package

Reference the expected Rendering Package when applicable.

These references provide the baseline against which the generated video is verified.

---

# 5. Execution Configuration

Record execution parameters.

| Field           | Description                   |
| --------------- | ----------------------------- |
| Seed            | Random seed                   |
| Resolution      | Output resolution             |
| FPS             | Frames per second             |
| Duration        | Video duration                |
| Frame Count     | Total frames                  |
| Inference Steps | Backend inference steps       |
| Sampler         | Sampling method               |
| Scheduler       | Scheduler configuration       |
| Hardware        | Optional hardware information |

This information supports reproducibility.

---

# 6. Execution Results

Record objective execution metrics.

| Metric           | Description                |
| ---------------- | -------------------------- |
| Generation Time  | Total rendering time       |
| Peak VRAM Usage  | Maximum GPU memory         |
| Peak RAM Usage   | Maximum system memory      |
| Backend Warnings | Execution warnings         |
| Backend Errors   | Execution errors           |
| Output Status    | Success / Partial / Failed |

Execution metrics should remain factual and free of subjective interpretation.

---

# 7. Verification Results

Evaluate the experiment using the Verification Dimensions.

| Verification Dimension               | Score | Notes |
| ------------------------------------ | ----: | ----- |
| Narrative Adherence                  |       |       |
| Character Continuity                 |       |       |
| Rendering Specification Completeness |       |       |
| Temporal Planning                    |       |       |
| Capability Integration               |       |       |
| Rendering Package Integrity          |       |       |
| Backend Execution                    |       |       |
| Runtime Performance                  |       |       |
| Identity Consistency                 |       |       |
| Camera Adherence                     |       |       |
| Motion Quality                       |       |       |
| Environment Consistency              |       |       |
| Temporal Adherence                   |       |       |
| Visual Quality                       |       |       |

Scores should follow the scoring methodology defined by the Verification Framework.

---

# 8. Failure Analysis

If verification objectives are not achieved, identify the most likely architectural stage responsible.

Possible sources include:

* Narrative Planning
* Scene Model
* Rendering Specification
* Rendering Package
* Prompt Relay
* MSR
* IC-LoRA
* Rendering Backend
* Unknown

The objective is diagnosis rather than blame.

---

# 9. Improvement Opportunities

Record actionable improvements identified during the experiment.

Examples include:

* Adjust temporal segmentation.
* Improve Character Sheet Specification.
* Refine camera planning.
* Modify Rendering Specification.
* Tune Prompt Relay configuration.
* Optimize MSR settings.
* Improve backend parameters.

Recommendations should be specific and measurable whenever possible.

---

# 10. Overall Assessment

Summarize the verification outcome.

Possible outcomes include:

| Status                 | Meaning                                                   |
| ---------------------- | --------------------------------------------------------- |
| Pass                   | Primary verification objectives achieved.                 |
| Pass with Observations | Objectives achieved with notable issues.                  |
| Partial Pass           | Some objectives achieved; targeted improvements required. |
| Fail                   | Primary verification objectives not achieved.             |

The assessment should briefly summarize the experiment and identify the most significant findings.

---

# Evidence

Whenever possible, attach or reference supporting evidence.

Examples include:

* Generated videos
* Key frames
* Character Sheets
* Background images
* Rendering logs
* Backend console output
* Verification screenshots

Evidence should enable independent review of the reported results.

---

# Architectural Summary

A Verification Report is the canonical record of a rendering experiment within Video Story Director.

By documenting configuration, execution, verification, and analysis in a standardized format, the project establishes a repeatable process for evaluating architectural changes, rendering capabilities, and backend performance.

Verification Reports form the evidence base for future development, regression testing, and comparative benchmarking across project versions.
