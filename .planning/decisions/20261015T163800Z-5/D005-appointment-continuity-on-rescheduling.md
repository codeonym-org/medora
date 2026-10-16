---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D005",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "Appointment continuity on rescheduling",
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
    ".planning/decisions/20261015T085738Z-3/D037-keep-original-during-rescheduling.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Appointment",
    "Rescheduling Request",
    "Appointment history"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D037-keep-original-during-rescheduling.md",
    "GLOSSARY.md",
    "docs/domain-model.md"
  ]
}
---

# Context — why ask this?

The original slot is retained until replacement approval and patient agreement. We have not decided whether the resulting consultation is the same appointment or a cancellation followed by an unrelated booking; this changes history and how the outcome is explained.

## Predecessor decisions

- [D037-keep-original-during-rescheduling](../20261015T085738Z-3/D037-keep-original-during-rescheduling.md)

The linked outcomes are settled prerequisites. No other round 2 answer is assumed.

## Question

Q5 — A confirmed Monday appointment moves to Thursday after approval and patient agreement. Should it remain the same Appointment, with a recorded time-change history, rather than count as a cancellation and an unrelated new appointment?

## Recommendation and alternatives

Keep the same Appointment and record the approved change, linked to its Rescheduling Request. Preserve the original commitment until the replacement succeeds. A genuinely cancelled appointment remains cancelled; a later fresh booking is separate. The alternative is cancel-and-create for every move, which can obscure continuity and cancellation reporting. This is domain continuity, not a database identifier or storage decision.

Proposed only; awaiting the user's reply.

## User reply — original words

Pending. Prepared for round 2; no reply received.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Appointment, Rescheduling Request, Appointment history. A reply will refine the domain relationship and its acceptance scenarios without selecting implementation details.

## Assumptions, evidence, and open questions

All people and times in this scenario are synthetic. No application code exists to compare. Detailed policy values, verification mechanisms and storage choices remain outside this question.

## Extra notes and follow-ups

Existing booking-policy and identity/permission follow-ups remain in progress. This round does not resolve their entire scope.

## History

- 2026-10-16T10:18:23Z — Prepared the round 2 question after saving the joint round 1 answer.
