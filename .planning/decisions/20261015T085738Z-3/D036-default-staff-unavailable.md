---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D036",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Default staff unavailable",
  "status": "confirmed",
  "round": 11,
  "created_at": "2026-10-15T15:38:29Z",
  "updated_at": "2026-10-15T15:44:38Z",
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
  ],
  "reply_recorded_at": "2026-10-15T15:44:38Z"
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

The current choice below records the user reply; earlier recommendations remain historical.

## User reply — original words



Round 11 reply, recorded 2026-10-15T15:44:38Z; original message timestamp unavailable:

> q44: yeah

## Interpretation

The user accepts a configured backup for unavailable default staff and visibility of unresolved handoffs in a shared authorized queue, with honest pending-response communication.

## Decision and rationale

Confirmed: practices may configure backup staff; unresolved handoffs remain in an authorized shared queue, with backup notification and accurate patient status.

## Consequences and affected components

Confirmed: practices may configure backup staff; unresolved handoffs remain in an authorized shared queue, with backup notification and accurate patient status. Backup selection details, availability detection, reassignment and escalation timing remain open. No response-time guarantee or all-staff access to private chat is created.

## Assumptions, evidence, and open questions

Backup selection details, availability detection, reassignment and escalation timing remain open. No response-time guarantee or all-staff access to private chat is created.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T15:38:29Z — Prepared the round 11 question from confirmed prerequisites.

- 2026-10-15T15:44:38Z — Saved round 11 reply and confirmed the explicit choice. Prior interpretation: Pending. Prior decision: Pending.
