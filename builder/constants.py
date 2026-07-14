"""
Video Story Director
Build System Constants

This module defines project-wide constants that are not expected to change
between builds.
"""

from pathlib import Path

# ============================================================================
# Project Information
# ============================================================================

PROJECT_NAME = "Video Story Director"

# ============================================================================
# Repository Paths
# ============================================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

PROMPT_DIR = ROOT_DIR / "prompt"

BACKENDS_DIR = ROOT_DIR / "backends"

DOCS_DIR = ROOT_DIR / "docs"

RELEASES_DIR = ROOT_DIR / "releases"

TESTS_DIR = ROOT_DIR / "tests"

EVALUATION_DIR = ROOT_DIR / "evaluation"

EXAMPLES_DIR = ROOT_DIR / "examples"

RESEARCH_DIR = ROOT_DIR / "research"

# ============================================================================
# Prompt Module Order
# ============================================================================

PROMPT_MODULES = [
    "01_identity.md",
    "02_core_principles.md",
    "03_request_analysis.md",
    "04_character_engine.md",
    "05_world_engine.md",
    "06_story_state_engine.md",
    "07_scene_planner.md",
    "08_frame0_engine.md",
    "09_rendering_engine.md",
    "10_validation_engine.md",
    "11_output_contract.md",
]

# ============================================================================
# Assembly Order
# ============================================================================

ASSEMBLY_SEQUENCE = (
    PROMPT_MODULES[:9]
    + ["__BACKEND__"]
    + PROMPT_MODULES[9:]
)