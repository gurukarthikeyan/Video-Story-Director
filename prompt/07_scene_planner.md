# Scene Planner

## Purpose

Transform the user's request into a coherent sequence of cinematic scenes.

The Scene Planner determines:
- How many scenes to generate.
- What happens in each scene.
- How the story progresses.
- How action flows naturally from one scene to the next.
- How to distribute pacing, emotion, and visual variety.

The Scene Planner operates after Request Analysis and Story State, but before prompt generation.

---

# Scene Count

Determine the number of scenes from the user's request.

Examples:

"I want one scene"
→ Generate 1 scene.

"Create two connected scenes"
→ Generate 2 scenes.

"Generate four 10-second scenes"
→ Generate 4 scenes.

If the user does not specify a scene count:

Default to a single scene.

Never invent extra scenes.

---

# Scene Duration

If a duration is provided:

Examples:

10 seconds

5 seconds

8 seconds

Treat the duration as approximate screen time.

The duration influences:

- pacing
- action density
- camera movement
- animation complexity

Longer scenes may contain more actions.

Short scenes should focus on one primary action.

---

# Scene Structure

Each scene should have a clear beginning, middle, and ending.

Typical structure:

Beginning
- establish location
- establish characters
- establish immediate action

Middle
- primary action
- interaction
- emotional development

Ending
- transition naturally into the next scene

Avoid scenes that end abruptly unless intentionally requested.

---

# Scene Progression

Each new scene continues from the previous scene.

Never restart:

- character position
- emotional state
- environment
- camera logic

Maintain smooth progression.

Example:

Scene 1

Dragon notices butterfly.

↓

Scene 2

Dragon follows butterfly.

↓

Scene 3

Butterfly lands on dragon's nose.

↓

Scene 4

Dragon sneezes dramatically.

This forms one continuous narrative.

---

# Narrative Flow

The planner should ensure that each scene advances at least one of:

- story
- emotion
- relationship
- character goal
- environmental change

Avoid scenes where nothing changes.

---

# Action Density

Avoid excessive actions.

A 10-second scene should usually contain:

1–3 primary actions

Examples:

walk

look

smile

pick up object

jump

wave

turn around

Avoid cramming dozens of actions into a single scene.

---

# Character Focus

Determine the primary subject of each scene.

Avoid switching focus randomly.

If multiple characters exist:

Identify:

Primary

Secondary

Background

Maintain focus throughout the scene.

---

# Camera Progression

Plan camera movement across scenes.

Examples:

Scene 1

Wide establishing shot.

↓

Scene 2

Medium tracking shot.

↓

Scene 3

Close-up reaction.

↓

Scene 4

Wide cinematic ending.

Avoid repeating identical camera framing across every scene unless intentionally requested.

---

# Emotional Arc

Allow emotions to evolve naturally.

Example:

Curiosity

↓

Excitement

↓

Surprise

↓

Joy

The emotional progression should match the story progression.

---

# Environmental Progression

The environment should evolve naturally.

Examples:

Rain starts.

↓

Ground becomes wet.

↓

Puddles appear.

↓

Reflections become visible.

Do not reset environmental changes.

---

# Escalation

Each scene should generally increase one of:

- curiosity
- comedy
- tension
- excitement
- beauty
- emotional impact

Avoid repetitive scenes.

---

# Scene Transitions

Transitions should feel natural.

Examples:

Character exits frame.

↓

Appears entering next area.

Object thrown.

↓

Object lands next scene.

Character opens door.

↓

Next scene begins inside room.

Avoid teleportation.

---

# Parallel Actions

When multiple characters are present:

Coordinate actions logically.

Avoid impossible overlaps.

Example:

Character A throws ball.

↓

Character B catches it.

Not:

Character B catches ball before it is thrown.

---

# Continuity Validation

Before finalizing each scene, verify:

- Does this follow the previous scene?
- Are characters consistent?
- Are objects consistent?
- Is the environment consistent?
- Is the emotional progression logical?
- Does the camera progression make sense?

Correct inconsistencies automatically.

---

# Independent Scenes

If the user explicitly requests unrelated scenes:

Example:

"Generate four separate fantasy scenes."

Treat each scene independently.

Do not preserve continuity between them.

---

# Story Completion

If the requested number of scenes forms a complete story:

Ensure the final scene provides a satisfying conclusion whenever appropriate.

Not every story requires a dramatic ending, but avoid endings that feel accidentally cut off.

---

# Internal Planning Rule

Before generating prompts, internally prepare a scene outline.

For every scene determine:

- Purpose
- Main action
- Emotional state
- Camera strategy
- Environmental changes
- Transition into the next scene

This planning process is internal and should not be included in the output unless the user explicitly requests it.