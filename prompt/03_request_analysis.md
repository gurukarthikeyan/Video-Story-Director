# ============================================================================
# Request Analysis Engine
# Module: 03
# Purpose: Interpret the user's request before any story planning begins.
# ============================================================================

Before planning the story, analyze the user's request and establish the planning context.

Determine the following information:

----------------------------------------------------------------------
Story Structure
----------------------------------------------------------------------

Identify:

• number of scenes
• duration of each scene
• whether scenes are connected or independent

If scene count is omitted, assume a single scene.

----------------------------------------------------------------------

Story Intent

----------------------------------------------------------------------

Identify the primary action or event the user wants to visualize.

Determine:

• beginning
• progression
• expected ending

Do not invent unrelated story events.

----------------------------------------------------------------------

Characters

----------------------------------------------------------------------

Identify every character explicitly mentioned.

Determine:

• quantity
• relationships
• roles
• whether recurring across scenes

Do not redesign named characters.

Only infer missing visual details when necessary.

----------------------------------------------------------------------

Environment

----------------------------------------------------------------------

Determine:

• primary location
• time of day if specified
• weather if specified
• environmental hazards
• important objects
• recurring locations

Assume one continuous environment unless the story requires a change.

----------------------------------------------------------------------

Tone

----------------------------------------------------------------------

Determine the intended tone.

Examples include:

• comedy
• adventure
• suspense
• emotional
• dramatic
• whimsical
• cinematic
• realistic

Maintain the same tone throughout connected scenes unless the story naturally evolves.

----------------------------------------------------------------------

Constraints

----------------------------------------------------------------------

Identify all explicit user constraints.

Examples:

• animation style
• camera preference
• number of scenes
• duration
• visual style
• specific characters
• specific objects
• pacing

User constraints always take priority over inferred details.

----------------------------------------------------------------------

Planning Summary

----------------------------------------------------------------------

Internally establish a complete understanding of the request before any story planning begins.

Do not expose this analysis.

Proceed only after the request has been fully interpreted.