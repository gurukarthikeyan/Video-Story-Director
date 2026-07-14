# Frame 0 Engine

## Purpose

Generate a high-quality first-frame image prompt that serves as the visual anchor for the entire video sequence.

The first frame establishes:

- Character appearance
- Environment
- Lighting
- Composition
- Camera angle
- Art direction
- Mood
- Visual identity

All subsequent video prompts should assume this first frame exists.

---

# When to Generate

Generate a Frame 0 prompt whenever:

- The user requests a new story.
- The user starts a new scene sequence.
- The user requests an image + video workflow.
- The current story has no established visual anchor.

Do not generate a new Frame 0 if the user is simply continuing an existing story, unless explicitly requested.

---

# Primary Goal

The first frame should be visually complete and immediately recognizable.

It should look like a professionally composed still from a finished animated film rather than a rough concept sketch.

---

# Composition

Prefer strong cinematic compositions.

Examples:

- Rule of thirds
- Center framing for iconic reveals
- Symmetrical framing
- Dynamic diagonal composition
- Leading lines
- Layered foreground, midground, and background

Avoid cluttered or confusing layouts.

---

# Subject Clarity

Clearly establish the primary subject.

The viewer should instantly recognize:

- who the main character is
- where they are
- what they are doing
- what the visual focus is

Avoid competing focal points.

---

# Character Initialization

Fully establish every important character.

Include:

- appearance
- proportions
- clothing
- accessories
- expression
- pose
- species
- age impression
- distinctive visual features

Maintain consistency with the Character Engine.

---

# Environment Initialization

Clearly establish:

- location
- architecture
- terrain
- vegetation
- weather
- time of day
- season
- atmosphere

The environment should immediately communicate the setting.

---

# Lighting

Specify lighting intentionally.

Examples:

- soft morning sunlight
- warm golden hour
- overcast daylight
- cinematic moonlight
- dramatic sunset
- studio lighting
- neon city glow

Lighting should support the mood.

---

# Color Palette

Establish a consistent palette.

Examples:

- warm pastel colors
- vibrant fantasy colors
- earthy natural tones
- cool blue sci-fi lighting
- muted cinematic realism
- colorful animated style

Maintain this palette throughout the story unless intentionally changed.

---

# Camera Placement

Specify:

- framing
- viewing angle
- perspective
- distance

Examples:

Wide establishing shot

Medium shot

Close-up

Eye level

Low angle

High angle

Over-the-shoulder

Avoid vague camera descriptions.

---

# Lens Style

When appropriate, define lens characteristics.

Examples:

24mm cinematic wide

35mm natural perspective

50mm portrait

85mm close-up

Macro

Keep lens choice consistent with the intended storytelling style.

---

# Depth

Prefer layered scenes.

Foreground

↓

Subject

↓

Background

Create visual depth whenever appropriate.

Avoid flat compositions.

---

# Pose

Characters should have natural, readable poses.

Avoid:

- stiff posture
- awkward symmetry
- unclear body language

Body language should reinforce emotion.

---

# Expression

Facial expressions should clearly communicate the current emotional state.

Examples:

curious

determined

joyful

worried

playful

surprised

Match the Story State.

---

# Visual Readability

The image should remain readable even as a single frame.

Avoid:

- excessive clutter
- overlapping subjects
- hidden faces
- confusing silhouettes

Every important subject should be identifiable.

---

# Style Consistency

Maintain one consistent artistic direction.

Examples:

Pixar-inspired stylized animation

Anime

Photorealistic

Oil painting

Hand-painted fantasy

Stop-motion

Do not mix incompatible styles unless explicitly requested.

---

# Motion Readiness

Choose poses that naturally lead into motion.

Examples:

- one foot already stepping forward
- hand reaching toward an object
- dragon preparing to flap its wings
- child leaning forward before running

Avoid static "posing for a photo."

The first frame should feel like the instant before movement begins.

---

# Continuity Anchor

The Frame 0 prompt becomes the visual reference for:

- character proportions
- clothing
- environment
- lighting
- mood
- camera language
- art style

Subsequent scenes should not redefine these elements unless intentionally changed.

---

# Output Scope

The Frame 0 output should describe only the first frame.

Do not include future actions, scene transitions, or events that occur later in the sequence.

Future motion belongs in the LTX video prompts.

---

# Internal Validation

Before producing the Frame 0 prompt, verify:

- Is the main subject immediately clear?
- Are all key characters initialized?
- Is the environment fully established?
- Is the lighting intentional?
- Is the composition cinematic?
- Does the pose naturally lead into animation?
- Is the art style consistent?
- Can this frame serve as a reliable visual anchor for all following scenes?

Revise internally if necessary before generating the final Frame 0 prompt.