---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D022",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Optional groups",
  "status": "confirmed",
  "round": 8,
  "created_at": "2026-10-15T14:38:24Z",
  "updated_at": "2026-10-15T14:45:47Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Human handoff",
    "Optional patient groups",
    "Patient channel continuity"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md",
    ".planning/decisions/20261015T085738Z-3/whatsapp-group-feasibility.md"
  ],
  "reply_recorded_at": "2026-10-15T14:45:47Z"
}
---

# Context — why ask this?

The user proposed a group per patient. Official-source research shows account and invitation limits, so the initial flow needs an explicit choice about group dependence and fallback.

## Predecessor decisions

[D021](D021-staff-takeover-of-patient-chat.md). Their accepted outcomes are prerequisites; no other round 8 outcome is assumed. Where groups are relevant, see [the feasibility note](whatsapp-group-feasibility.md).

## Question

Q29 — Optional groups: Given WhatsApp's restrictions, should per-patient groups be optional for eligible practices and consenting participants, with staff able to handle the existing one-to-one patient chat when groups are unavailable or declined?

## Recommendation and alternatives

Yes. Keep the patient-group idea, but preserve a usable human handoff for every supported practice without requiring group access.

The current decision records the user reply below. Earlier recommendations are not automatically accepted where the user supplied a different configuration.

## User reply — original words

Round 8 reply, recorded 2026-10-15T14:45:47Z; original message timestamp unavailable:

> q29: ok

## Interpretation

The user accepts optional per-patient groups for eligible practices and consenting participants, with authorized human handling of the existing one-to-one patient conversation when groups are unavailable or declined.

## Decision and rationale

Confirmed: optional patient-specific groups with a one-to-one handoff fallback. Group availability is eligibility-dependent; the patient is not required to join a group to receive human assistance.

## Consequences and affected components

Confirmed: optional patient-specific groups with a one-to-one handoff fallback. Group availability is eligibility-dependent; the patient is not required to join a group to receive human assistance. Group delivery timing, lifecycle, invitation/join failures and native tag detection remain unresolved. No group implementation or supported-account compatibility is claimed.

## Assumptions, evidence, and open questions

Group delivery timing, lifecycle, invitation/join failures and native tag detection remain unresolved. No group implementation or supported-account compatibility is claimed.

## Extra notes and follow-ups

The linked-line follow-up holds remaining WhatsApp integration verification. These product questions stay in the active session.

## History

- 2026-10-15T14:38:24Z — Prepared the round 8 question after preserving the round 7 reply and checking relevant official documentation.

- 2026-10-15T14:45:47Z — Saved round 8 reply and confirmed its explicit scope. Prior interpretation: Pending. Prior decision: Pending.
