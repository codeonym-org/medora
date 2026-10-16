---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D003",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "Request versus expired reservation",
  "status": "confirmed",
  "round": 1,
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-16T10:18:23Z",
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
  ],
  "reply_recorded_at": "2026-10-16T10:18:23Z",
  "reply_reference": "Joint user reply: ok, next; in response to the three first-round recommendations"
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

This was the recommendation presented before the joint reply; the acceptance and its limited interpretation are recorded below.

## User reply — original words

Joint reply to the first three modeling recommendations, recorded 2026-10-16T10:18:23Z; original message timestamp unavailable:

> ok, next

## Interpretation

Read as acceptance of the three recommendations just presented and a request to continue. This is a joint acknowledgment, not three separately worded answers. For this decision: Reservation expiry releases the slot and triggers notification, while the Appointment Request stays open needing another slot. Explicit withdrawal or closure remains possible; expiry never confirms an appointment.

No additional policy values, verification method or implementation choices are inferred.

## Decision and rationale

Confirmed within this scenario: Reservation expiry releases the slot and triggers notification, while the Appointment Request stays open needing another slot. Explicit withdrawal or closure remains possible; expiry never confirms an appointment.

The user supplied no separate rationale. The recommendation and its reasoning above are assistant-authored.

## Consequences and affected components

Appointment Request, Reservation, Appointment. The reply will sharpen terminology and relationships in the glossary/model.

## Assumptions, evidence, and open questions

The joint reply confirms the relationship described above. No database schema, account implementation, global person-matching scheme or automatic verification method is selected. Detailed permissions and independent request-closure policies remain open. No application code exists to cross-check.

## Extra notes and follow-ups

The booking-policy and identity/permissions follow-ups remain open; vocabulary work does not resolve their full scope.

## History

- 2026-10-15T16:38:00Z — Prepared this scenario from the confirmed foundation; user response pending.

- 2026-10-16T10:18:23Z — Saved the joint reply verbatim and recorded its acceptance of the existing recommendation; no additional commitments inferred.
