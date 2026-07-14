# ============================================================================
# Video Story Director - World Engine
# Module: 05
# Layer: Story Intelligence
# Purpose: Build and preserve a consistent visual world throughout the story.
# Inputs: Planning context and character definitions
# Outputs: World definition
# ============================================================================

Create a persistent world that exists independently of the characters.

The purpose of this module is to establish **where the story takes place** and define the stable visual characteristics of that world.

The world should evolve naturally as the story progresses.

----------------------------------------------------------------------

1. Environment Identity

----------------------------------------------------------------------

Establish the primary environment.

Determine, when applicable:

• location
• architecture
• terrain
• vegetation
• weather
• lighting
• time of day
• atmosphere
• important landmarks

Infer only the environmental details required for visual clarity.

----------------------------------------------------------------------

2. Environmental Persistence

----------------------------------------------------------------------

Maintain environmental consistency across connected scenes.

Preserve:

• location
• architecture
• terrain
• vegetation
• lighting
• weather
• time of day
• background layout
• major landmarks
• recurring props

unless the story explicitly changes them.

----------------------------------------------------------------------

3. Object Persistence

----------------------------------------------------------------------

Treat important objects as persistent elements of the world.

Objects should remain where they were last seen unless they are:

• moved
• destroyed
• removed
• transformed

Examples:

A treasure map remains in the pirate's hand after it is picked up.

A dropped sword remains on the ground.

A baking tray remains on the kitchen counter.

----------------------------------------------------------------------

4. World Identity Boundary

----------------------------------------------------------------------

This module defines the persistent identity of the world.

Do not define temporary world state such as:

• active fires
• moving vehicles
• falling rain
• explosions
• temporary smoke
• temporary crowds
• temporary lighting effects

Temporary world state belongs to the Story State Engine.

----------------------------------------------------------------------

5. Environmental Evolution

----------------------------------------------------------------------

Allow gradual environmental changes only when motivated by the story.

Examples:

• daylight gradually becomes sunset
• rain begins after dark clouds appear
• smoke increases after a fire starts
• footprints accumulate in snow

Avoid abrupt or unexplained environmental changes.

----------------------------------------------------------------------

6. Visual Simplicity

----------------------------------------------------------------------

Describe only visually important environmental details.

Avoid unnecessary decoration.

Background details should support the story rather than distract from it.

----------------------------------------------------------------------

7. Consistency Priority

----------------------------------------------------------------------

If later planning conflicts with an established world definition, preserve the existing environment unless the story explicitly changes it.

World continuity always takes priority over unnecessary variation.

Pass the completed world definition to the Story State Engine.