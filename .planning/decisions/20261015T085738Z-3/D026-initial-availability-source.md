---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D026",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Where does availability come from?",
  "status": "confirmed",
  "round": 9,
  "created_at": "2026-10-15T14:45:47Z",
  "updated_at": "2026-10-15T14:52:33Z",
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
  ],
  "reply_recorded_at": "2026-10-15T14:52:33Z"
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

The user accepted the current choice in the recorded reply. Details not supplied remain explicitly open.

## User reply — original words

Round 9 reply, recorded 2026-10-15T14:52:33Z; original message timestamp unavailable:

> q33: yeah for starter

## Interpretation

The user accepts Medora as the initial scheduling source, with doctors/authorized staff managing real working hours, breaks, blocks and appointments there. External calendar synchronization remains planned for later rather than required at launch.

## Decision and rationale

Confirmed initial workflow: manage the authoritative schedule directly in Medora. External calendar integrations stay in the feature register for a future increment.

## Consequences and affected components

Confirmed initial workflow: manage the authoritative schedule directly in Medora. External calendar integrations stay in the feature register for a future increment. Minimum setup, appointment-type durations, doctor-specific working hours, migration of existing commitments and operational schedule maintenance remain to be specified. No external calendar provider or stack is selected.

## Assumptions, evidence, and open questions

Minimum setup, appointment-type durations, doctor-specific working hours, migration of existing commitments and operational schedule maintenance remain to be specified. No external calendar provider or stack is selected.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.

- 2026-10-15T14:52:33Z — Saved round 9 reply and confirmed the choice. Prior interpretation: Pending. Prior decision: Pending.
