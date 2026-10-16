---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D006",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "Receptionist doctor assignment scope",
  "status": "unanswered",
  "round": 2,
  "created_at": "2026-10-16T10:18:23Z",
  "updated_at": "2026-10-16T10:18:23Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "predecessors": [
    ".planning/decisions/20261015T163800Z-5/D001-staff-identity-and-membership.md",
    ".planning/decisions/20261015T085738Z-3/D034-practice-configuration-ownership.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Practice Membership",
    "Receptionist",
    "Doctor",
    "Administrative access"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T163800Z-5/D001-staff-identity-and-membership.md",
    ".planning/decisions/20261015T085738Z-3/D034-practice-configuration-ownership.md",
    "GLOSSARY.md",
    "docs/domain-model.md"
  ]
}
---

# Context — why ask this?

Membership roles are practice-scoped, but a practice may contain several doctors. A Receptionist role alone does not yet tell us whether the person coordinates every doctor or an assigned subset.

## Predecessor decisions

- [D001-staff-identity-and-membership](D001-staff-identity-and-membership.md)
- [D034-practice-configuration-ownership](../20261015T085738Z-3/D034-practice-configuration-ownership.md)

The linked outcomes are settled prerequisites. No other round 2 answer is assumed.

## Question

Q6 — A practice has Dr Sara and Dr Omar. Should the owner be able to assign a receptionist to Sara only, with a separate explicit option to coordinate all doctors in that practice?

## Recommendation and alternatives

Yes: make doctor coverage an explicit scope within the practice membership. The role alone should not silently grant access to every doctor's appointments or profiles. Coverage authorizes only the configured administrative work and does not itself grant clinical access. The alternative is practice-wide reception by default, which is simpler but cannot represent a restricted assignment. Shared-patient profile visibility and exact permissions need their own later decisions.

Proposed only; awaiting the user's reply.

## User reply — original words

Pending. Prepared for round 2; no reply received.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Practice Membership, Receptionist, Doctor, Administrative access. A reply will refine the domain relationship and its acceptance scenarios without selecting implementation details.

## Assumptions, evidence, and open questions

All people and times in this scenario are synthetic. No application code exists to compare. Detailed policy values, verification mechanisms and storage choices remain outside this question.

## Extra notes and follow-ups

Existing booking-policy and identity/permission follow-ups remain in progress. This round does not resolve their entire scope.

## History

- 2026-10-16T10:18:23Z — Prepared the round 2 question after saving the joint round 1 answer.
