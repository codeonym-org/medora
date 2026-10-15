---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D001",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "Staff accounts and memberships",
  "status": "unanswered",
  "round": 1,
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-15T16:38:00Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D034-practice-configuration-ownership.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Practice Membership",
    "Practice Owner",
    "Doctor"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D034-practice-configuration-ownership.md",
    "GLOSSARY.md",
    "docs/domain-model.md"
  ]
}
---

# Context — why ask this?

A person may work in several practices and an explicit admin account is confirmed. The account identity, membership and role combination now need a precise relationship.

## Predecessor decisions

- [D001-first-practice](../20261015T085738Z-3/D001-first-practice.md)
- [D034-practice-configuration-ownership](../20261015T085738Z-3/D034-practice-configuration-ownership.md)

These established requirements are inputs; no outcome of another first-round modeling question is assumed.

## Question

Dr Sara owns Practice A and also works at Practice B. Should she use one Medora staff account with separate memberships, allowing her to be Owner/Admin and Doctor in A but only Doctor in B?

## Recommendation and alternatives

Use one staff identity with practice-scoped memberships and role combinations. Entering another practice must change the active permissions and accessible records, not carry the first practice's authority across.

This is a proposed domain relationship, not a confirmed user choice or implementation decision.

## User reply — original words

Pending. Prepared for the first domain-modeling round.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Practice Membership, Practice Owner, Doctor. The reply will sharpen terminology and relationships in the glossary/model.

## Assumptions, evidence, and open questions

No database schema, account implementation, global person-matching scheme, automatic verification or request-closure policy is assumed. No application code exists to cross-check.

## Extra notes and follow-ups

The booking-policy and identity/permissions follow-ups remain open; vocabulary work does not resolve their full scope.

## History

- 2026-10-15T16:38:00Z — Prepared this scenario from the confirmed foundation; user response pending.
