---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D003",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "Request versus expired reservation",
  "status": "unanswered",
  "round": 1,
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-15T16:38:00Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D010-provisional-reservation-policy.md",
    ".planning/decisions/20261015T085738Z-3/D014-review-deadline-outside-working-hours.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Appointment Request",
    "Reservation",
    "Appointment"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D010-provisional-reservation-policy.md",
    ".planning/decisions/20261015T085738Z-3/D014-review-deadline-outside-working-hours.md",
    "GLOSSARY.md",
    "docs/domain-model.md"
  ]
}
---

# Context — why ask this?

Reservation expiry releases time, but the confirmed foundation does not decide whether the patient's underlying request survives. This scenario distinguishes the lifecycles without choosing storage structures.

## Predecessor decisions

- [D009-routine-booking-authority](../20261015T085738Z-3/D009-routine-booking-authority.md)
- [D010-provisional-reservation-policy](../20261015T085738Z-3/D010-provisional-reservation-policy.md)
- [D014-review-deadline-outside-working-hours](../20261015T085738Z-3/D014-review-deadline-outside-working-hours.md)

These established requirements are inputs; no outcome of another first-round modeling question is assumed.

## Question

A patient requests Tuesday at 10:00, but the Reservation expires before staff review it. Should the Appointment Request remain open for another slot, or should expiry close the whole request?

## Recommendation and alternatives

Keep the request open as needing a new slot, while clearly marking the old reservation expired and telling the contact. Staff or the patient can explicitly withdraw/close the request; an expired hold must never imply a confirmed appointment.

This is a proposed domain relationship, not a confirmed user choice or implementation decision.

## User reply — original words

Pending. Prepared for the first domain-modeling round.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Appointment Request, Reservation, Appointment. The reply will sharpen terminology and relationships in the glossary/model.

## Assumptions, evidence, and open questions

No database schema, account implementation, global person-matching scheme, automatic verification or request-closure policy is assumed. No application code exists to cross-check.

## Extra notes and follow-ups

The booking-policy and identity/permissions follow-ups remain open; vocabulary work does not resolve their full scope.

## History

- 2026-10-15T16:38:00Z — Prepared this scenario from the confirmed foundation; user response pending.
