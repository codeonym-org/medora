---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D008",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Staff chat privacy",
  "status": "confirmed",
  "round": 4,
  "created_at": "2026-10-15T12:13:49Z",
  "updated_at": "2026-10-15T13:46:49Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Staff assistant",
    "Practice collaboration",
    "Conversation visibility"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T13:46:49Z"
}
---

# Context — why ask this?

A private management realm excludes patients but does not establish whether staff conversations are private from colleagues. This affects collaboration and access expectations.

## Predecessor decisions

[D001](D001-first-practice.md); [D006](D006-booking-entry.md) establish the relevant accepted practice/role/initial-scope requirements. For D006, only the explicit private staff realm is a prerequisite; unsettled channel choices are not assumed.

## Question

Q14 — Staff chat privacy: Does each doctor/receptionist have a private conversation with Medora while sharing authorized schedules and requests, or should the whole practice see one shared conversation?

## Recommendation and alternatives

Give each staff member a private assistant conversation, with shared operational records and clear action attribution. Do not share all chat transcripts by default.

The alternatives remain proposals until the user replies.

## User reply — original words



Round 4 reply, recorded 2026-10-15T13:46:49Z; original message timestamp unavailable:

> q14: yeah, private conversations! they can share it thought with other users on the medora platform

## Interpretation

Each staff user has private conversations with Medora. A user may intentionally share conversation material with other Medora users. This does not establish snapshot versus ongoing access, the recipient audience, edit/comment permissions, revocation, or permission to expose otherwise unauthorized patient records.

## Decision and rationale

Confirmed: private staff conversations with optional explicit sharing to other Medora users. The default is private; sharing details remain unresolved.

## Consequences and affected components

Separate personal conversation visibility from shared operational data. Sharing requires a deliberate user action and must respect existing record-access and practice boundaries. D012/Q19 will clarify audience and scope.

## Assumptions, evidence, and open questions

Recipient eligibility, same-practice versus cross-practice sharing, selected messages versus whole conversations, live versus snapshot access, revocation, and audit details remain open.

## Extra notes and follow-ups

Related questions are continuing within this product session. No unrelated follow-up was introduced by this reply.

## History

- 2026-10-15T12:13:49Z — Assistant prepared round 4 question from accepted prerequisites.

- 2026-10-15T13:46:49Z — Saved round 4 reply and confirmed the explicit choice.
  - Prior interpretation: Pending.
  - Prior decision summary: Pending.
