---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D026",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Where does availability come from?",
  "status": "unanswered",
  "round": 9,
  "created_at": "2026-10-15T14:45:47Z",
  "updated_at": "2026-10-15T14:45:47Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D018-linked-line-doctor-routing.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Availability setup",
    "Doctor calendar",
    "Booking source of truth"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D018-linked-line-doctor-routing.md",
    "docs/product-vision.md"
  ]
}
---

# Context — why ask this?

Reliable conversational booking needs an operational source of availability. The initial product scope has not selected whether an external calendar is a launch requirement. This is a workflow decision, not a technology stack choice.

## Predecessor decisions

[D002](D002-anchor-problem.md); [D009](D009-routine-booking-authority.md); [D018](D018-linked-line-doctor-routing.md). Accepted outcomes provide the prerequisites; no other round 9 answer is assumed.

## Question

Q33 — Where does availability come from?: For the first version, should doctors/staff manage working hours, breaks, blocked time and appointments directly in Medora, or must an existing external calendar also stay synchronized from day one?

## Recommendation and alternatives

Use Medora as the scheduling source for the first increment, with authorized staff maintaining real availability there. Preserve external calendar synchronization in the feature register for later.

This is an assistant recommendation pending the user's choice.

## User reply — original words

Pending. Prepared for round 9.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Availability setup, Doctor calendar, Booking source of truth. The answer will define the corresponding first-increment workflow.

## Assumptions, evidence, and open questions

No external integration, practice-specific factual answer, notification delivery guarantee or identity-verification method is selected or asserted. Technical stack choices remain excluded.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.
