---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D038",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Groups in the first beta",
  "status": "confirmed",
  "round": 12,
  "created_at": "2026-10-15T15:44:38Z",
  "updated_at": "2026-10-15T15:54:26Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D005-release-readiness.md",
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md",
    ".planning/decisions/20261015T085738Z-3/D022-optional-patient-group-handoff.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Beta scope",
    "Human handoff",
    "Optional patient groups"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D005-release-readiness.md",
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md",
    ".planning/decisions/20261015T085738Z-3/D022-optional-patient-group-handoff.md"
  ],
  "reply_recorded_at": "2026-10-15T15:54:26Z"
}
---

# Context — why ask this?

Optional groups are accepted, but their delivery timing remains unsettled and the official eligibility/invocation constraints have not been integration-tested. This is a scope decision rather than a provider/stack selection.

## Predecessor decisions

[D002](D002-anchor-problem.md); [D005](D005-release-readiness.md); [D021](D021-staff-takeover-of-patient-chat.md); [D022](D022-optional-patient-group-handoff.md). Accepted outcomes supply the prerequisites; no other round 12 answer is assumed.

## Question

Q46 — Groups in the first beta: Should the first beta require complete one-to-one human handoff, while optional WhatsApp groups can be added once account eligibility, invitations and agent invocation have been verified?

## Recommendation and alternatives

Yes. Make the core handoff complete first; keep optional groups registered without making unverified group support a blocker for every practice.

The user accepted the scope choice below; detailed design remains in the linked follow-ups.

## User reply — original words

Round 12 reply, recorded 2026-10-15T15:54:26Z; original message timestamp unavailable:

> q46: ok

## Interpretation

The user accepts complete one-to-one human handoff as the beta baseline, with optional patient groups added only after their eligibility, invitations and agent invocation have been verified. Group support is not a universal beta prerequisite.

## Decision and rationale

Confirmed: baseline beta handoff works through the existing patient chat; optional patient groups remain registered and depend on verified support.

## Consequences and affected components

Confirmed: baseline beta handoff works through the existing patient chat; optional patient groups remain registered and depend on verified support. No release date is assigned. Group lifecycle/product details go to communication follow-up; eligibility/tag delivery verification stays in the existing WhatsApp technical-research follow-up.

## Assumptions, evidence, and open questions

No release date is assigned. Group lifecycle/product details go to communication follow-up; eligibility/tag delivery verification stays in the existing WhatsApp technical-research follow-up.

## Extra notes and follow-ups

Pending design details are listed in [the scope review](scope-review.md). Proposed deferrals are not yet accepted.

## History

- 2026-10-15T15:44:38Z — Prepared this round 12 question after recording round 11.

- 2026-10-15T15:54:26Z — Saved round 12 reply and confirmed the explicit choice. Prior interpretation: Pending. Prior decision: Pending.
