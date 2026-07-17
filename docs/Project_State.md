# Video Story Director - Project State

> This document is the authoritative snapshot of the project's current development state.
> It should be updated whenever a significant milestone or architectural decision is completed.

---

# Project

**Name:** Video Story Director

**Current Version:** v1.2.0 (Development)

**Branch:** v1.2.0

**Status:** Active Development

---

# Current Milestone

## Milestone 1 – LTX Intelligence

Current focus:

Establish LTX as the reference backend and improve planning intelligence using real-world validation.

The objective is to maximize prompt adherence, character consistency, and temporal consistency on LTX before expanding to additional backends.

---

## Current Task

1. Document the Scene Planning Philosophy.
2. Integrate Prompt Relay into the rendering strategy.
3. Evaluate and integrate MSR as the primary identity consistency layer.
4. Support IC-LoRA as optional conditioning (pose, depth, motion, etc.).
5. Refine Module 07 based on empirical LTX testing.

---

# Last Completed

## v1.1.0

✓ Architecture finalized

✓ Prompt modules (01–11)

✓ Rendering Engine abstraction

✓ Backend architecture

✓ Build system

✓ Documentation

✓ Release system

✓ Comprehensive repository review completed

✓ Architecture review completed

✓ v1.2 direction finalized

✓ Rendering strategy updated

✓ LTX selected as reference backend

✓ MSR evaluation direction established

✓ Prompt Relay selected for temporal prompt adherence

✓ IC-LoRA designated as optional conditioning

---

# Architecture Status

Architecture: **Frozen**

The following are not planned for v1.2:

- No new prompt modules
- No module reordering
- No build system redesign
- No repository restructuring

Focus only on improving intelligence.

---

# Accepted Decisions

## D001

v1.1.0 becomes the architectural baseline.

---

## D002

Planning and rendering remain separate responsibilities.

---

## D003

Backend-specific behavior belongs only inside backend adapters.

---

## D004

Story planning should optimize for what current video models can realistically generate.

---

## D005

v1.2 focuses on improving intelligence, not architecture.

---

## D006

LTX is the reference backend for v1.2.

All planning improvements will be validated on LTX before expanding to additional video models.

---

## D007

Prompt Relay is the preferred strategy for temporal prompt adherence.

---

## D008

MSR is the primary identity consistency solution.

---

## D009

IC-LoRA is optional conditioning.

It supplements identity with pose, depth, motion, or other conditioning signals, but does not replace MSR.

---

## D010

Backend expansion is postponed until the LTX pipeline demonstrates stable improvements.

---

# Current Priorities

Priority 1

Scene Planning Intelligence

Priority 2

LTX Rendering Intelligence

Priority 3

MSR Integration

Priority 4

Prompt Relay Integration

Priority 5

Evaluation Framework

---

# Open Questions

- How should the planner reason before rendering?
- How should Prompt Relay be incorporated into Rendering Engine?
- How should MSR integrate into the pipeline?
- Which IC-LoRA conditioning signals should be supported?
- How should evaluation measure temporal consistency?

---

# Next Tasks

1. Write Scene Planning Philosophy
2. Design Prompt Relay integration
3. Design MSR workflow
4. Design IC-LoRA conditioning interface
5. Refine Module 07
6. Expand evaluation benchmarks

---

# Deferred

Backend expansion

Wan integration

Veo integration

Future backend adapters

Prompt optimization passes

Builder AST

These are postponed until the LTX workflow is mature.

---

# Repository Health

Architecture: Stable

LTX Strategy: Active Development

Planner Intelligence: Active Development

MSR Integration: Planned

Prompt Relay Integration: Planned

Evaluation Framework: Active Development

Multi-backend Support: Deferred

---

# Notes

Video Story Director should continue evolving as a backend-independent story planning framework.

Future releases should improve reasoning quality while preserving the architectural foundation established in v1.1.0.

---

Architecture Status

Frozen (v1.2)

Current Focus

Evaluation Framework
Reference Rendering Pipeline
Prompt Relay
MSR
Optional IC-LoRA