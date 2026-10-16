---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D004",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "One active reservation per request",
  "status": "unanswered",
  "round": 2,
  "created_at": "2026-10-16T10:18:23Z",
  "updated_at": "2026-10-16T10:18:23Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "predecessors": [
    ".planning/decisions/20261015T163800Z-5/D003-request-after-reservation-expiry.md",
    ".planning/decisions/20261015T085738Z-3/D037-keep-original-during-rescheduling.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Appointment Request",
    "Reservation",
    "Availability"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T163800Z-5/D003-request-after-reservation-expiry.md",
    ".planning/decisions/20261015T085738Z-3/D037-keep-original-during-rescheduling.md",
    "GLOSSARY.md",
    "docs/domain-model.md"
  ]
}
---

# Context — why ask this?

An open request can outlive a reservation. Offering several choices must now be distinguished from provisionally removing several slots from availability.

## Predecessor decisions

- [D003-request-after-reservation-expiry](D003-request-after-reservation-expiry.md)
- [D037-keep-original-during-rescheduling](../20261015T085738Z-3/D037-keep-original-during-rescheduling.md)

The linked outcomes are settled prerequisites. No other round 2 answer is assumed.

## Question

Q4 — A patient is choosing between Tuesday at 10:00 and Wednesday at 14:00. Should one Appointment Request hold only one selected slot at a time, while the other times remain suggestions?

## Recommendation and alternatives

Yes: allow one active Reservation per Appointment Request. On an authorized switch, replace the old hold with the new one; if the switch fails, do not claim it succeeded or silently discard a still-valid hold. A confirmed original appointment during rescheduling is separate and remains protected by the existing rule. The alternative is holding several choices, which consumes capacity before the patient chooses. This does not set a global per-person limit or settle duplicate-request policy.

Proposed only; awaiting the user's reply.

## User reply — original words

Pending. Prepared for round 2; no reply received.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Appointment Request, Reservation, Availability. A reply will refine the domain relationship and its acceptance scenarios without selecting implementation details.

## Assumptions, evidence, and open questions

All people and times in this scenario are synthetic. No application code exists to compare. Detailed policy values, verification mechanisms and storage choices remain outside this question.

## Extra notes and follow-ups

Existing booking-policy and identity/permission follow-ups remain in progress. This round does not resolve their entire scope.

## History

- 2026-10-16T10:18:23Z — Prepared the round 2 question after saving the joint round 1 answer.
