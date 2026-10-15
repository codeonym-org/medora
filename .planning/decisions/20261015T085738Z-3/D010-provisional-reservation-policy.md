---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D010",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Pending reservations",
  "status": "confirmed",
  "round": 5,
  "created_at": "2026-10-15T13:46:49Z",
  "updated_at": "2026-10-15T13:52:30Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Availability",
    "Pending requests",
    "Patient status messages"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md"
  ],
  "reply_recorded_at": "2026-10-15T13:52:30Z"
}
---

# Context — why ask this?

The accepted staff-review flow creates a period between reserving a slot and confirming an appointment. Availability and expiry must be explicit to avoid conflicting promises.

## Predecessor decisions

[D009](D009-routine-booking-authority.md). Their confirmed outcomes provide the prerequisites; no answer to another round 5 question is assumed.

## Question

Q17 — Pending reservations: While staff review a request, should its reserved slot be unavailable to other patients? Should the reservation expire if staff do not respond?

## Recommendation and alternatives

Hold the slot exclusively, with a practice-configured review deadline. If it expires, release it and tell the patient; never leave them believing it is confirmed.

The user accepted this recommendation in the recorded reply, with the cancellation clarification recorded for Q20.

## User reply — original words

Round 5 reply, recorded 2026-10-15T13:52:30Z; original message timestamp unavailable:

> q17: ok

## Interpretation

The user accepts the recommended exclusive reservation with a practice-configured review deadline. On expiry, the slot is released and the patient is informed. No numerical deadline, working-hours rule, reminder policy or last-minute cutoff was specified.

## Decision and rationale

Confirmed: pending reservations temporarily exclude competing bookings, expire according to practice configuration, release the slot on expiry, and notify the patient while preserving the distinction from confirmed appointments.

## Consequences and affected components

Confirmed: pending reservations temporarily exclude competing bookings, expire according to practice configuration, release the slot on expiry, and notify the patient while preserving the distinction from confirmed appointments. Staff-review clock behavior outside opening hours and cutoff before the actual appointment require further definition. No default duration is inferred.

## Assumptions, evidence, and open questions

Staff-review clock behavior outside opening hours and cutoff before the actual appointment require further definition. No default duration is inferred.

## Extra notes and follow-ups

No unrelated follow-up captured for this question.

## History

- 2026-10-15T13:46:49Z — Assistant prepared round 5 question from confirmed prerequisites.

- 2026-10-15T13:52:30Z — Recorded round 5 reply and confirmed the choice. Prior interpretation: Pending. Prior decision: Pending.
