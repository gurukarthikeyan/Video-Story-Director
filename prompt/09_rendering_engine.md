# ============================================================================
# Video Story Director - Rendering Engine
# Module: 09
# Layer: Rendering
# Purpose: Convert the Scene Plan into a backend-independent Rendering Specification.
# Inputs: Scene Plan, Frame0 Specification
# Outputs: Rendering Specification
# ============================================================================

The Rendering Engine is the bridge between Story Intelligence and backend-specific prompt generation.

Its purpose is to transform the completed Scene Plan into a structured Rendering Specification that can be translated by any supported rendering backend.

The Rendering Engine does not generate prompts.

It defines **what must be rendered**, not **how a particular model should be instructed to render it**.

----------------------------------------------------------------------

1. Rendering Philosophy

----------------------------------------------------------------------

Separate story planning from backend implementation.

Story Intelligence determines:

• what happens

Rendering determines:

• how the planned story should be represented for rendering

Backends determine:

• how the Rendering Specification becomes a model-specific prompt.

----------------------------------------------------------------------

2. Rendering Specification

----------------------------------------------------------------------

Produce a complete Rendering Specification for every scene.

The Rendering Specification should include:

• scene identity
• scene duration
• participating characters
• environment
• Frame 0 reference
• camera intent
• motion plan
• emotional progression
• environmental progression
• continuity requirements
• rendering constraints

The Rendering Specification is backend-independent.

----------------------------------------------------------------------

3. Rendering Strategy

----------------------------------------------------------------------

Determine the appropriate rendering strategy.

Examples include:

• image-to-video
• text-to-video
• single scene
• multi-scene sequence
• continuation of an existing story

Select the strategy using the user's request and available story context.

----------------------------------------------------------------------

4. Scene Packaging

----------------------------------------------------------------------

Prepare scenes for rendering.

Determine:

• rendering order
• scene boundaries
• shared continuity
• independent scenes

Do not modify story progression.

----------------------------------------------------------------------

5. Motion Planning

----------------------------------------------------------------------

Convert planned story events into observable visual actions.

Motion should be:

• chronological
• visually clear
• physically plausible
• appropriate for the scene duration

Do not introduce new story events.

----------------------------------------------------------------------

6. Camera Intent

----------------------------------------------------------------------

Represent the purpose of the camera rather than backend-specific terminology.

Examples include:

• establish
• observe
• follow
• reveal
• emphasize
• conclude

Do not specify lens types or model-specific camera language.

----------------------------------------------------------------------

7. Continuity Requirements

----------------------------------------------------------------------

Specify which elements must remain consistent across scenes.

Examples include:

• character identity
• character state
• environment
• lighting
• active objects
• visual style
• camera language

Continuity requirements become mandatory inputs for backend translation.

----------------------------------------------------------------------

8. Rendering Constraints

----------------------------------------------------------------------

Preserve all rendering constraints established by previous modules.

Examples include:

• scene duration
• scene count
• visual style
• image availability
• backend selection
• user requirements

Do not introduce additional constraints.

----------------------------------------------------------------------

9. Backend Independence

----------------------------------------------------------------------

Do not generate backend-specific wording.

Do not assume:

• prompt syntax
• preferred adjectives
• camera terminology
• quality modifiers
• model-specific optimization techniques

These responsibilities belong exclusively to backend modules.

----------------------------------------------------------------------

10. Backend Handoff

----------------------------------------------------------------------

Produce a complete Rendering Specification.

The Rendering Specification becomes the single source of truth for every rendering backend.

Each backend consumes the same Rendering Specification and translates it into its own prompt format without modifying story intent.

----------------------------------------------------------------------

11. Internal Rule

----------------------------------------------------------------------

Before completing the Rendering Specification, internally verify:

• the story has not changed
• scene order is preserved
• continuity is maintained
• no new events were introduced
• rendering remains backend-independent

Pass the completed Rendering Specification to the selected backend.