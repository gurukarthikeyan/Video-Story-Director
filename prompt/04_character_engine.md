# ============================================================================
# Video Story Director - Character Engine
# Module: 04
# Layer: Story Intelligence
# Purpose: Build and preserve consistent character identity throughout the story.
# Inputs: Planning context
# Outputs: Character definitions
# ============================================================================

Create a persistent identity for every recurring character.

The purpose of this module is to establish **who each character is**, not what happens to them during the story.

A character should remain visually recognizable throughout all connected scenes.

----------------------------------------------------------------------

1. Character Identity

----------------------------------------------------------------------

Establish only the information necessary for visual consistency.

Include when applicable:

• species
• approximate age
• body type
• proportions
• primary colors
• secondary colors
• clothing
• accessories
• hairstyle, fur, feathers, scales, or equivalent
• facial features
• movement style
• distinctive visual traits

Do not add unnecessary details.

----------------------------------------------------------------------

2. Character Persistence

----------------------------------------------------------------------

Once established, a character's identity remains unchanged.

Preserve consistent:

• appearance
• clothing
• colors
• accessories
• proportions
• movement style
• distinctive visual traits

unless the story explicitly changes them.

----------------------------------------------------------------------

3. Character Relationships

----------------------------------------------------------------------

Determine how characters relate to one another.

Examples include:

• friends
• family
• rivals
• strangers
• teammates
• companions

Maintain these relationships throughout connected scenes unless the story explicitly changes them.

----------------------------------------------------------------------

4. Character Behavior

----------------------------------------------------------------------

Movement should reflect personality and physical characteristics.

Examples:

• confident characters move with purpose
• timid characters move cautiously
• children move differently from adults
• animals move according to their species
• robots move according to their construction

Behavior should remain consistent unless the story justifies a change.

----------------------------------------------------------------------

5. Character State Boundary

----------------------------------------------------------------------

This module defines permanent character identity.

Do not define temporary character state such as:

• current emotions
• injuries
• dirt or damage
• temporary clothing changes
• carried objects
• pose
• facial expression

Temporary character state belongs to the Story State Engine.

----------------------------------------------------------------------

6. Inference Guidelines

----------------------------------------------------------------------

Infer only details required for visual consistency.

Do not invent:

• unnecessary backstory
• occupations
• names
• history
• motivations

unless explicitly requested.

----------------------------------------------------------------------

7. Consistency Priority

----------------------------------------------------------------------

If later planning conflicts with an established character identity, preserve the existing identity unless the user explicitly requests a change.

Character consistency always takes priority over unnecessary variation.

Pass the completed character definitions to the World Engine.