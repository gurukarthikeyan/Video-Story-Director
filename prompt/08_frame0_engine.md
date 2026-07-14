# ============================================================================
# Video Story Director - Frame 0 Engine
# Module: 08
# Layer: Rendering
# Purpose: Define the visual anchor that establishes the initial state of the story before animation begins.
# Inputs: Scene Plan
# Outputs: Frame 0 Specification
# ============================================================================

Generate a complete visual specification for the first frame of a new story or scene sequence.

The purpose of this module is to define **what exists at the exact moment before animation begins**.

The Frame 0 specification becomes the visual anchor for all subsequent scenes.

----------------------------------------------------------------------

1. When to Generate

----------------------------------------------------------------------

Generate a new Frame 0 only when:

• starting a new story
• starting a new scene sequence
• the user requests an image-to-video workflow
• no visual anchor currently exists

Do not generate a new Frame 0 when continuing an existing story unless explicitly requested.

----------------------------------------------------------------------

2. Visual Anchor

----------------------------------------------------------------------

Frame 0 establishes the initial visual state of the story.

It should define:

• characters
• environment
• lighting
• composition
• camera placement
• artistic direction
• mood

Every subsequent scene should inherit this visual foundation unless intentionally changed.

----------------------------------------------------------------------

3. Subject Initialization

----------------------------------------------------------------------

Clearly establish the primary subject.

The viewer should immediately recognize:

• who is present
• where they are
• what the visual focus is

Avoid competing focal points.

----------------------------------------------------------------------

4. Character Initialization

----------------------------------------------------------------------

Initialize every important character using the Character Engine.

Establish:

• appearance
• proportions
• clothing
• accessories
• pose
• expression
• distinctive visual traits

Do not redefine established character identity.

----------------------------------------------------------------------

5. Environment Initialization

----------------------------------------------------------------------

Initialize the environment using the World Engine.

Establish:

• location
• architecture
• terrain
• vegetation
• weather
• lighting
• time of day
• atmosphere

Do not redefine the established world.

----------------------------------------------------------------------

6. Composition

----------------------------------------------------------------------

Prefer strong cinematic composition.

Examples include:

• rule of thirds
• centered composition
• leading lines
• layered depth
• symmetrical framing
• dynamic diagonals

Avoid clutter and visual ambiguity.

----------------------------------------------------------------------

7. Camera Foundation

----------------------------------------------------------------------

Establish:

• framing
• viewing angle
• perspective
• camera distance

Do not determine backend-specific camera wording.

----------------------------------------------------------------------

8. Visual Style

----------------------------------------------------------------------

Establish a consistent artistic direction.

Examples include:

• stylized animation
• anime
• photorealistic
• painterly
• stop-motion

Do not mix incompatible styles unless explicitly requested.

----------------------------------------------------------------------

9. Motion Readiness

----------------------------------------------------------------------

Frame 0 contains no motion.

Characters and objects should appear naturally prepared for the first planned action.

Avoid static portrait-like posing.

----------------------------------------------------------------------

10. Continuity Anchor

----------------------------------------------------------------------

Frame 0 becomes the reference for:

• character appearance
• environment
• lighting
• composition
• artistic style
• visual identity

Subsequent rendering should preserve these elements unless intentionally changed.

----------------------------------------------------------------------

11. Frame 0 Handoff

----------------------------------------------------------------------

Produce a complete Frame 0 Specification.

Pass the specification to the Rendering Engine for backend-specific prompt generation.