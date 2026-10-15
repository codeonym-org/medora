---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D009",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Routine booking approval",
  "status": "unanswered",
  "round": 4,
  "created_at": "2026-10-15T12:13:49Z",
  "updated_at": "2026-10-15T12:13:49Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Booking confirmations",
    "Practice policies",
    "Staff review"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    "docs/product-vision.md"
  ]
}
---

# Context — why ask this?

The product vision requires authorized scheduling and truthful confirmations, but the default routine-booking approval policy is not defined. The question is independent of which channel receives the request.

## Predecessor decisions

[D001](D001-first-practice.md); [D002](D002-anchor-problem.md) establish the accepted practice model and basic-booking scope.

## Question

Q16 — Routine booking approval: When a patient selects a valid available slot, should Medora confirm automatically within the practice rules, require staff approval for every request, or let each practice choose?

## Recommendation and alternatives

Let each practice choose. Automatic confirmation applies only to eligible routine bookings; requests outside its configured rules go to staff.

The alternatives remain proposals until the user replies.

## User reply — original words

Pending. Question prepared for round 4.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Affected areas: Booking confirmations, Practice policies, Staff review. The answer will constrain the related staff and patient workflows.

## Assumptions, evidence, and open questions

No default is inferred from the assistant recommendation. Technical stack selection remains excluded; exact permissions and failure behavior need later product decisions.

## Extra notes and follow-ups

No unrelated follow-up captured for this question.

## History

- 2026-10-15T12:13:49Z — Assistant prepared round 4 question from accepted prerequisites.
