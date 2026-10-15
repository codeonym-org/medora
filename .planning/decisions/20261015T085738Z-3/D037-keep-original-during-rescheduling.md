---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D037",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "While rescheduling is pending",
  "status": "confirmed",
  "round": 12,
  "created_at": "2026-10-15T15:44:38Z",
  "updated_at": "2026-10-15T15:54:26Z",
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
  ],
  "reply_recorded_at": "2026-10-15T15:54:26Z"
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

The user accepted the scope choice below; detailed design remains in the linked follow-ups.

## User reply — original words

Round 12 reply, recorded 2026-10-15T15:54:26Z; original message timestamp unavailable:

> q45: ok

## Interpretation

The user accepts preserving the original appointment while a patient-requested replacement is pending. Replacement approval/agreement is required before switching, except when the original has explicitly been cancelled or is no longer available.

## Decision and rationale

Confirmed: exploring/reserving another time does not by itself remove the original booking. Keep the original until the replacement is approved and accepted, unless its cancellation/unavailability is explicit; communicate that exception clearly.

## Consequences and affected components

Confirmed: exploring/reserving another time does not by itself remove the original booking. Keep the original until the replacement is approved and accepted, unless its cancellation/unavailability is explicit; communicate that exception clearly. Detailed replacement-offer expiry, hold limits, cutoffs and atomic transition/failure behavior go to the booking-policy follow-up.

## Assumptions, evidence, and open questions

Detailed replacement-offer expiry, hold limits, cutoffs and atomic transition/failure behavior go to the booking-policy follow-up.

## Extra notes and follow-ups

Pending design details are listed in [the scope review](scope-review.md). Proposed deferrals are not yet accepted.

## History

- 2026-10-15T15:44:38Z — Prepared this round 12 question after recording round 11.

- 2026-10-15T15:54:26Z — Saved round 12 reply and confirmed the explicit choice. Prior interpretation: Pending. Prior decision: Pending.
