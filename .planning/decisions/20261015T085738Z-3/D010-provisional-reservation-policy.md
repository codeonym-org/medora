---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D010",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Pending reservations",
  "status": "unanswered",
  "round": 5,
  "created_at": "2026-10-15T13:46:49Z",
  "updated_at": "2026-10-15T13:46:49Z",
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
  ]
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

This is an assistant recommendation. The question's alternatives remain open pending the user reply.

## User reply — original words

Pending. Question prepared for round 5.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Affected areas: Availability, Pending requests, Patient status messages. The answer constrains the next level of product workflow details.

## Assumptions, evidence, and open questions

No duration, role permission, sharing scope, or patient agreement is invented. Relevant details remain unresolved until the user answers. No technology stack is selected.

## Extra notes and follow-ups

No unrelated follow-up captured for this question.

## History

- 2026-10-15T13:46:49Z — Assistant prepared round 5 question from confirmed prerequisites.
