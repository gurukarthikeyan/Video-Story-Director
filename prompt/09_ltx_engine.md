# LTX Engine

## Purpose

Generate high-quality LTX Video prompts from the established Story State and Scene Plan.

The LTX Engine converts cinematic intent into prompts optimized for image-conditioned video generation while preserving continuity, visual quality, and natural motion.

The generated prompt should describe what happens during the scene, assuming the supplied Frame 0 image already exists.

---

# Primary Objective

Produce prompts that generate:

- smooth motion
- believable physics
- expressive characters
- coherent storytelling
- stable identity
- cinematic composition

Every prompt should feel like a professional animation direction rather than a static image description.

---

# Image-Conditioned Generation

Assume the input image already defines:

- character appearance
- clothing
- environment
- lighting
- composition
- color palette
- visual style

Do not unnecessarily repeat these details.

Instead, describe how the scene evolves from the supplied image.

---

# Motion-First Prompting

Prioritize movement over appearance.

Describe:

- body movement
- facial animation
- eye movement
- head movement
- hand gestures
- posture changes
- interaction
- environmental motion
- secondary motion

Movement should always be intentional.

---

# Natural Motion

Motion should follow believable timing.

Examples:

Head turns before body.

Eyes focus before reaching.

Weight shifts before walking.

Wings compress before flapping.

Hands slow before stopping.

Avoid robotic animation.

---

# Action Hierarchy

Describe actions in order.

Primary action

↓

Secondary action

↓

Reaction

↓

Environmental response

↓

Idle continuation

This creates readable motion.

---

# Character Animation

Characters should display:

- breathing
- blinking
- subtle eye movement
- natural posture adjustment
- weight shifting
- expressive facial animation

Avoid frozen characters.

---

# Facial Performance

Expressions should evolve naturally.

Examples:

Smile grows gradually.

Eyes widen in surprise.

Brows lower during concentration.

Lip movement matches emotion.

Avoid sudden emotional changes.

---

# Secondary Motion

Include physically appropriate secondary motion.

Examples:

Hair sways.

Clothing ripples.

Tail follows movement.

Ears bounce.

Scarves flutter.

Jewelry swings.

Dragon wings flex.

Secondary motion improves realism.

---

# Environmental Animation

Animate the world when appropriate.

Examples:

Leaves move.

Grass sways.

Clouds drift.

Water ripples.

Rain falls.

Fog rolls.

Smoke rises.

Fire flickers.

Avoid static environments.

---

# Camera Motion

Camera movement should support storytelling.

Examples:

Static

Slow push-in

Slow pull-back

Pan

Tilt

Tracking shot

Crane

Orbit

Handheld

Avoid unnecessary camera movement.

Only move the camera when it improves the shot.

---

# Camera Stability

Avoid excessive camera shake.

Prefer:

smooth

controlled

cinematic

motivated

Stable framing generally produces better image-conditioned results.

---

# Object Interaction

Objects should behave realistically.

Examples:

Character picks up cup.

Cup moves with hand.

Door opens before character enters.

Ball rolls after being released.

Avoid impossible object behavior.

---

# Physical Continuity

Respect physics.

Momentum

Weight

Balance

Gravity

Collision

Wind

Water

Avoid floating or impossible movement unless intentionally stylized.

---

# Motion Density

A scene should contain only as many actions as comfortably fit within its duration.

Approximate guidance:

5 seconds

1–2 major actions

10 seconds

2–4 major actions

15 seconds

3–5 major actions

Do not overload scenes.

---

# Emotional Animation

Body language should reinforce emotion.

Examples:

Happy

Relaxed posture

Open gestures

Light movement

Sad

Slower movement

Lower shoulders

Downward gaze

Excited

Quick movement

Bright expressions

Energetic gestures

---

# Dialogue

If dialogue exists:

Prioritize visible performance.

Examples:

Natural mouth movement

Eye contact

Subtle gestures

Conversation pacing

Do not generate spoken dialogue unless the user requests it.

---

# Sound Awareness

Although LTX generates video only, actions should naturally support later sound design.

Examples:

Footsteps

Wing flaps

Door creaks

Rain

Water splashes

Paper rustling

Metal impacts

Glass breaking

Avoid impossible silent actions.

---

# Style Preservation

Preserve:

art style

lighting

character identity

camera language

color palette

visual quality

Do not redefine these unless Story State changes.

---

# Scene Completion

Every scene should end in a stable state that naturally transitions into the following scene.

Avoid ending mid-action unless intentionally requested.

---

# Multi-Scene Generation

When multiple scenes are requested:

Generate each scene independently while maintaining:

- continuity
- character state
- environment
- emotional progression
- camera language
- story progression

Every scene should begin where the previous one ended.

---

# Prompt Writing Style

Write prompts using:

clear

descriptive

cinematic

natural language

Avoid:

bullet lists

technical syntax

parameter notation

camera metadata

JSON

Prompt text should read like concise film direction.

---

# Internal Validation

Before finalizing each prompt, verify:

- Does motion begin naturally from the supplied first frame?
- Are actions physically believable?
- Is character identity preserved?
- Is emotional progression logical?
- Is camera movement appropriate?
- Is the environment animated when appropriate?
- Is the prompt concise without omitting important motion?

Revise internally if needed before output.