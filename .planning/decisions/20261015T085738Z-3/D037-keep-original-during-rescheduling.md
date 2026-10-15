---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D037",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "While rescheduling is pending",
  "status": "unanswered",
  "round": 12,
  "created_at": "2026-10-15T15:44:38Z",
  "updated_at": "2026-10-15T15:44:38Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D032-first-increment-appointment-lifecycle.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Rescheduling",
    "Original booking",
    "Provisional replacement",
    "Patient agreement"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D032-first-increment-appointment-lifecycle.md"
  ]
}
---

# Context — why ask this?

Basic rescheduling is in beta scope. Keeping or releasing the original while a replacement is pending is not yet settled and directly affects patient confidence and availability.

## Predecessor decisions

[D009](D009-routine-booking-authority.md); [D013](D013-replacement-slot-agreement.md); [D032](D032-first-increment-appointment-lifecycle.md). Accepted outcomes supply the prerequisites; no other round 12 answer is assumed.

## Question

Q45 — While rescheduling is pending: When a patient requests a different time, should the original appointment remain booked until the replacement is approved and accepted, unless the original has explicitly been cancelled or is no longer available?

## Recommendation and alternatives

Yes. Reserve the proposed replacement provisionally, then switch only after staff approval and patient agreement. Do not make a patient lose their existing booking just by asking about another time.

This recommendation awaits the user reply.

## User reply — original words

Pending. Prepared for round 12.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Rescheduling, Original booking, Provisional replacement, Patient agreement. No feature is implemented or silently deferred by asking this question.

## Assumptions, evidence, and open questions

No automatic loss of existing appointments, mandatory initial group delivery or deferral approval is inferred. The session remains active and technical stack selection remains excluded.

## Extra notes and follow-ups

Pending design details are listed in [the scope review](scope-review.md). Proposed deferrals are not yet accepted.

## History

- 2026-10-15T15:44:38Z — Prepared this round 12 question after recording round 11.
