---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D036",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Default staff unavailable",
  "status": "unanswered",
  "round": 11,
  "created_at": "2026-10-15T15:38:29Z",
  "updated_at": "2026-10-15T15:38:29Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D014-review-deadline-outside-working-hours.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D030-staff-daily-workspace.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Handoff assignment",
    "Staff attention queue",
    "Backup coverage",
    "Patient expectations"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D014-review-deadline-outside-working-hours.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D030-staff-daily-workspace.md",
    "docs/product-vision.md"
  ]
}
---

# Context — why ask this?

Human handoff targets a default staff member. The platform needs an explicit operational path when that person cannot respond. This is routine administrative handoff, not a replacement for urgent clinical escalation.

## Predecessor decisions

[D011](D011-staff-approval-permissions.md); [D014](D014-review-deadline-outside-working-hours.md); [D023](D023-handoff-staff-assignment.md); [D030](D030-staff-daily-workspace.md). Accepted outcomes provide the prerequisites; no other round 11 answer is assumed.

## Question

Q44 — Default staff unavailable: If the configured default staff member is unavailable, should the practice be able to name a backup, with unresolved handoffs kept visible in a shared authorized queue?

## Recommendation and alternatives

Yes. Notify the configured backup and keep the patient informed that a reply is pending. Do not imply that a human has responded or promise an unsupported response time.

This recommendation awaits the user choice.

## User reply — original words

Pending. Prepared for round 11.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Handoff assignment, Staff attention queue, Backup coverage, Patient expectations. Exact policy and permissions follow the user decision.

## Assumptions, evidence, and open questions

No new global role, cancellation fee/notice period, backup recipient or response guarantee is invented. Technical stack selection remains excluded.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T15:38:29Z — Prepared the round 11 question from confirmed prerequisites.
