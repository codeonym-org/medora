---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D034",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Who manages the practice?",
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
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D030-staff-daily-workspace.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Practice ownership",
    "Staff membership",
    "Permissions",
    "Connected lines"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D030-staff-daily-workspace.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T15:44:38Z",
  "amends": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md"
  ]
}
---

# Context — why ask this?

The user confirms a functional platform with staff and connected lines. Authority to configure its people and communication boundaries is not yet assigned.

## Predecessor decisions

[D001](D001-first-practice.md); [D011](D011-staff-approval-permissions.md); [D023](D023-handoff-staff-assignment.md); [D030](D030-staff-daily-workspace.md). Accepted outcomes provide the prerequisites; no other round 11 answer is assumed.

## Question

Q42 — Who manages the practice?: Who should control staff invitations, permissions and connected lines: a designated practice owner, or every doctor?

## Recommendation and alternatives

Use a designated practice-owner capability, with delegated permissions. Keep the existing Doctor/Receptionist/Patient roles; ownership is a responsibility within the practice, not a fourth patient-facing role. Doctors retain approval of clinical intake content.

The current choice below records the user reply; earlier recommendations remain historical.

## User reply — original words



Round 11 reply, recorded 2026-10-15T15:44:38Z; original message timestamp unavailable:

> q42: an owner (admin account)

## Interpretation

The user explicitly selects an Owner/Admin account to manage the practice. This updates the earlier three-operational-role framing and does not merely endorse the assistant's suggested ownership capability without an admin designation. In context, this is a practice owner/admin, not a global platform superadministrator.

## Decision and rationale

Confirmed: an explicit practice Owner/Admin account controls practice administration such as staff invitations, permissions and connected lines. Doctor, Receptionist and Patient remain operational roles. The user did not specify whether one person/account can combine administrative and clinical roles.

## Consequences and affected components

Confirmed: an explicit practice Owner/Admin account controls practice administration such as staff invitations, permissions and connected lines. Doctor, Receptionist and Patient remain operational roles. The user did not specify whether one person/account can combine administrative and clinical roles. Fine-grained admin permissions, delegation and role combinations remain open. Administrative control does not automatically settle clinical-record visibility; existing least-privilege and doctor clinical-approval boundaries remain. D001 is partially amended only as to the role set.

## Assumptions, evidence, and open questions

Fine-grained admin permissions, delegation and role combinations remain open. Administrative control does not automatically settle clinical-record visibility; existing least-privilege and doctor clinical-approval boundaries remain. D001 is partially amended only as to the role set.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T15:38:29Z — Prepared the round 11 question from confirmed prerequisites.

- 2026-10-15T15:44:38Z — Saved round 11 reply and confirmed the explicit choice. Prior interpretation: Pending. Prior decision: Pending.
