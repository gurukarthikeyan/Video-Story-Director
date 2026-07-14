"""
Video Story Director
Build Configuration

This module contains build-specific settings that may change between releases.
"""

# ============================================================================
# Build Configuration
# ============================================================================

VERSION = "1.1.0"

BACKEND = "ltx"

OUTPUT_TEMPLATE = "Video_Story_Director_{backend}_v{version}.txt"

# ============================================================================
# Build Options
# ============================================================================

INCLUDE_BUILD_HEADER = True

PRINT_BUILD_REPORT = True

FAIL_ON_WARNING = False