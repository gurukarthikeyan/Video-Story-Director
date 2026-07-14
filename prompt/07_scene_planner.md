# ============================================================================
# Video Story Director - Scene Planner
# Module: 07
# Layer: Story Intelligence
# Purpose: Transform the Story State into a sequence of coherent cinematic scenes.
# Inputs: Story State
# Outputs: Scene Plan
# ============================================================================

Transform the current Story State into one or more cinematic scenes.

The purpose of this module is to determine **what happens in each scene** before any rendering strategy or backend-specific prompt generation begins.

----------------------------------------------------------------------

1. Scene Count

----------------------------------------------------------------------

Determine the required number of scenes from the user's request.

If omitted, generate a single scene.

Never invent additional scenes.

----------------------------------------------------------------------

2. Scene Duration

----------------------------------------------------------------------

Determine the intended duration of each scene.

Scene duration influences:

• pacing
• action density
• visual complexity
• camera opportunities

Longer scenes may contain additional sequential actions.

Shorter scenes should focus on one primary event.

----------------------------------------------------------------------

3. Scene Purpose

----------------------------------------------------------------------

Every scene should have one primary purpose.

Examples include:

• introduce a character
• establish a location
• advance the story
• reveal new information
• resolve a conflict
• conclude the story

Avoid scenes with multiple unrelated objectives.

----------------------------------------------------------------------

4. Scene Structure

----------------------------------------------------------------------

Plan each scene as a clear sequence:

• beginning
• progression
• conclusion

The conclusion should naturally transition into the next scene when scenes are connected.

----------------------------------------------------------------------

5. Narrative Progression

----------------------------------------------------------------------

Every connected scene should advance at least one of:

• story progression
• character development
• relationships
• emotional progression
• environmental progression
• active goals

Avoid scenes where nothing meaningfully changes.

----------------------------------------------------------------------

6. Character Focus

----------------------------------------------------------------------

Determine the visual focus of each scene.

Identify when applicable:

• primary character
• secondary characters
• background characters

Maintain consistent visual focus throughout the scene.

----------------------------------------------------------------------

7. Action Planning

----------------------------------------------------------------------

Plan actions as a chronological sequence of observable events.

Avoid simultaneous or contradictory actions.

Match action density to the scene duration.

----------------------------------------------------------------------

8. Camera Intent

----------------------------------------------------------------------

Plan the narrative purpose of the camera.

Examples include:

• establish location
• follow movement
• emphasize emotion
• highlight an object
• reveal important information

Do not determine backend-specific camera wording.

----------------------------------------------------------------------

9. Emotional Progression

----------------------------------------------------------------------

Allow emotions to evolve naturally across connected scenes.

Avoid abrupt emotional changes unless motivated by the story.

----------------------------------------------------------------------

10. Environmental Progression

----------------------------------------------------------------------

Plan environmental changes only when motivated by the story.

Preserve previously established world state.

----------------------------------------------------------------------

11. Scene Transitions

----------------------------------------------------------------------

Transitions between connected scenes should be visually and logically continuous.

Examples include:

• continuing movement
• entering a new location
• following an object
• continuing an interaction

Avoid unexplained discontinuities.

----------------------------------------------------------------------

12. Independent Scenes

----------------------------------------------------------------------

If the user explicitly requests unrelated scenes:

Plan each scene independently.

Do not preserve continuity between them.

----------------------------------------------------------------------

13. Story Completion

----------------------------------------------------------------------

When the requested scenes form a complete story:

Plan a satisfying conclusion appropriate for the requested tone.

Not every story requires a dramatic ending.

----------------------------------------------------------------------

14. Scene Plan Handoff

----------------------------------------------------------------------

For every planned scene, internally determine:

• scene purpose
• participating characters
• environment
• planned actions
• emotional state
• transition

Pass the completed Scene Plan to the Rendering Engine.