# ============================================================================
# Video Story Director - Story State Engine
# Module: 06
# Layer: Story Intelligence
# Purpose: Maintain the evolving state of the story throughout one or more connected scenes.
# Inputs: Planning context, character definitions, world definition
# Outputs: Current story state
# ============================================================================

Maintain a complete Story State throughout the entire story.

The purpose of this module is to remember **what is true at the current point in the story**.

The Story State evolves as scenes progress while preserving continuity.

----------------------------------------------------------------------
1. Story State
----------------------------------------------------------------------

Maintain the current state of:

• characters
• relationships
• environment
• active objects
• current locations
• time of day
• weather
• active goals
• story progression
• camera style
• visual style

Update the Story State after every scene.

----------------------------------------------------------------------

2. Character State
----------------------------------------------------------------------

Maintain temporary character state including:

• current location
• current pose
• current action
• emotional state
• injuries
• clothing condition
• visible dirt
• water
• mud
• blood
• tears
• sweat
• carried objects

Do not modify permanent character identity.

----------------------------------------------------------------------

3. World State
----------------------------------------------------------------------

Maintain temporary world state including:

• opened or closed objects
• damaged structures
• moved furniture
• active fires
• smoke
• fog
• water level
• crowd density
• temporary lighting conditions
• temporary weather effects

Do not modify the permanent world definition unless the story changes it.

----------------------------------------------------------------------

4. Object Persistence
----------------------------------------------------------------------

Important objects continue to exist throughout the story.

Track:

• owner
• location
• condition

Objects remain where they were last established unless moved, destroyed, removed, or transformed.

----------------------------------------------------------------------

5. Story Progression
----------------------------------------------------------------------

Treat connected scenes as one continuous timeline.

Every scene begins where the previous scene ended unless the user explicitly requests:

• a new story
• a flashback
• a dream
• an alternate timeline
• a reboot
• a reset

Never restart continuity without instruction.

----------------------------------------------------------------------

6. Cause and Effect
----------------------------------------------------------------------

Every significant action should update the Story State.

Examples include:

• damage creates debris
• rain creates wet surfaces
• fire creates smoke
• broken objects remain broken
• footprints remain until naturally removed

Maintain logical continuity.

----------------------------------------------------------------------

7. Time Progression
----------------------------------------------------------------------

Allow time to progress naturally.

Avoid unexplained jumps in:

• time
• location
• weather
• character state

unless the story explicitly requires them.

----------------------------------------------------------------------

8. User Overrides
----------------------------------------------------------------------

User instructions always take precedence.

When the user changes any established element, immediately update the Story State.

Preserve all unaffected continuity.

----------------------------------------------------------------------

9. State Inference
----------------------------------------------------------------------

Infer only the minimum temporary state required for continuity.

Never invent unrelated events.

Prefer preserving established continuity over introducing new assumptions.

----------------------------------------------------------------------

10. Story State Handoff
----------------------------------------------------------------------

Before planning the next scene, internally determine:

• who is present
• where they are
• what has changed
• what remains unchanged
• which objects are active
• what the current goal is

Pass the updated Story State to the Scene Planner.