---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D035",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Patient cancellation",
  "status": "confirmed",
  "round": 11,
  "created_at": "2026-10-15T15:38:29Z",
  "updated_at": "2026-10-15T15:44:38Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md",
    ".planning/decisions/20261015T085738Z-3/D032-first-increment-appointment-lifecycle.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Cancellation",
    "Practice policies",
    "Slot availability",
    "Patient confirmation"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md",
    ".planning/decisions/20261015T085738Z-3/D032-first-increment-appointment-lifecycle.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T15:44:38Z"
}
---

# Context — why ask this?

Cancellation requests are now in beta scope. Staff-reviewed booking does not automatically settle whether the patient can immediately release their own appointment.

## Predecessor decisions

[D013](D013-replacement-slot-agreement.md); [D029](D029-first-contact-existing-record-access.md); [D032](D032-first-increment-appointment-lifecycle.md). Accepted outcomes provide the prerequisites; no other round 11 answer is assumed.

## Question

Q43 — Patient cancellation: When a verified patient clearly asks to cancel, should Medora execute it immediately within the practice policy, or always wait for staff approval?

## Recommendation and alternatives

Cancel immediately when the configured policy allows it, notify staff and release the slot. Route policy exceptions to staff; report completion only after cancellation succeeds.

The current choice below records the user reply; earlier recommendations remain historical.

## User reply — original words



Round 11 reply, recorded 2026-10-15T15:44:38Z; original message timestamp unavailable:

> q43: yeah immediatly and staff gets notified

## Interpretation

The user explicitly wants verified patient cancellation executed immediately, with staff notification, rather than requiring a fresh staff approval. Release the slot only through a successful authorized cancellation and communicate the actual result.

## Decision and rationale

Confirmed: verified patients can cancel immediately; execute the cancellation, release the slot and notify staff. Do not add ordinary staff-approval waiting to this flow.

## Consequences and affected components

Confirmed: verified patients can cancel immediately; execute the cancellation, release the slot and notify staff. Do not add ordinary staff-approval waiting to this flow. Cancellation fees/financial consequences, verification evidence, policy messaging and exceptional failed-operation handling remain unspecified. No monetary policy is inferred from immediate cancellation.

## Assumptions, evidence, and open questions

Cancellation fees/financial consequences, verification evidence, policy messaging and exceptional failed-operation handling remain unspecified. No monetary policy is inferred from immediate cancellation.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T15:38:29Z — Prepared the round 11 question from confirmed prerequisites.

- 2026-10-15T15:44:38Z — Saved round 11 reply and confirmed the explicit choice. Prior interpretation: Pending. Prior decision: Pending.
