# Decision Log

## D001

Date:
2026-07-15

Decision:
Freeze architecture for v1.2.

Reason:
Architecture review concluded that the modular design is mature. Further improvements should focus on reasoning rather than structural changes.

Status:
Accepted

## D006

Date:
2026-07-16

Decision:

LTX becomes the reference backend for v1.2 development.

Reason:

Planning improvements should be validated on a single backend before expanding to additional models.

Status:

Accepted

## D007

Date:
2026-07-16

Decision:

Prompt Relay is adopted as the preferred temporal prompt adherence strategy.

Reason:

Prompt Relay offers the strongest current direction for maintaining prompt intent across long video sequences.

Status:

Accepted

## D008

Date:
2026-07-16

Decision:

MSR becomes the primary identity consistency solution.

Reason:

Identity consistency is treated as a core rendering capability rather than a backend-specific feature.

Status:

Accepted

## D009

Date:
2026-07-16

Decision:

IC-LoRA is treated as optional conditioning.

Reason:

IC-LoRA provides additional control signals such as pose, depth, or motion while MSR remains responsible for identity preservation.

Status:

Accepted

## D010

Date:
2026-07-16

Decision:

Pause work on additional backend integrations during v1.2.

Reason:

Focus engineering effort on producing the strongest possible LTX pipeline before generalizing to Wan, Veo, or future backends.

Status:

Accepted

## D011

Date:
2026-07-16

Decision:

The Video Story Director rendering pipeline is defined as:

Story Planning
↓

Prompt Relay
↓

MSR Identity Consistency
↓

Optional IC-LoRA Conditioning
↓

LTX Rendering

Reason:

This establishes the reference rendering pipeline for v1.2 and provides a stable target for future evaluation and optimization.

Status:

Accepted

## D005

v1.2 Architecture Freeze

The v1.2 architecture is considered feature complete.

Future work should focus on implementation, evaluation, and optimization rather than architectural redesign.

Architectural changes should only be introduced when implementation reveals a genuine design limitation.