---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5",
  "title": "Practice identity, communication identity and appointment lifecycle",
  "status": "active",
  "session_kind": "domain-modeling",
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-15T16:38:00Z",
  "repository": "codeonym-org/medora",
  "issue_number": 5,
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "participants": [
    "user",
    "assistant"
  ],
  "facilitator": "assistant",
  "origin": {
    "conversation_url": null,
    "message_reference": "User invocation of mattpocock-skills:domain-modeling",
    "related_task": "Model the domain without selecting a stack"
  },
  "predecessor_sessions": [
    ".planning/decisions/20261015T085738Z-3/session.md"
  ],
  "supersedes": [],
  "superseded_by": [],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T155426Z-define-detailed-booking-policies/follow-up.md",
    ".planning/follow-ups/20261015T155426Z-define-identity-permissions-and-sharing/follow-up.md"
  ]
}
---

# Purpose and context

Build precise shared language and relationships for Medora using its confirmed product foundation. Capture resolved terminology immediately and stress-test unresolved concepts with concrete situations.

## Scope and constraints

In scope: practice membership/roles, patient/contact/communication identity, appointment request/reservation/appointment semantics and relevant lifecycle boundaries. Out of scope: stack selection, database schemas, implementation and arbitrary numerical practice-policy defaults. Expand to other domain concepts only as prerequisites settle.

## Decision tree

- Established foundation → glossary definitions already settled.
- Staff account versus practice membership → role combinations and practice-scoped authority.
- Contact person versus shared sender address → matching, preferences and representative authority.
- Reservation expiry versus request closure → request/reservation/appointment lifecycles.
- Later scenarios depend on these answers; do not silently settle them.

## Decision index and rounds

| ID / link | Round | Question | Predecessors | Status | Outcome |
| --- | --- | --- | --- | --- | --- |
| [D000](D000-modeling-scope.md) | 0 | Scope and confirmed foundations | Previous session | confirmed | Stack-neutral modeling |
| [D001](D001-staff-identity-and-membership.md) | 1 | Staff accounts and memberships | Linked earlier decisions | unanswered | Pending |
| [D002](D002-shared-contact-point.md) | 1 | A shared patient-side number | Linked earlier decisions | unanswered | Pending |
| [D003](D003-request-after-reservation-expiry.md) | 1 | Request versus expired reservation | Linked earlier decisions | unanswered | Pending |

## Current frontier

First modeling round: D001 staff identity/membership; D002 shared patient-side contact address; D003 request after reservation expiry. All are independent scenarios with pending replies.

## Unresolved or deferred branches

The three current relationships are unresolved. Patient profile scope remains practice-owned according to the foundation; no global cross-practice patient identity is chosen. Exact permissions, verification, numerical booking policies and implementation boundaries remain in the existing follow-ups.

## Shared understanding

The glossary captures established product terms only. Contact Point and Staff Account identity arrangements remain proposals outside the glossary until resolved. Requests, reservations, appointments and delivery outcomes have distinct meanings, but the detailed lifecycle model remains active work.

## Final user confirmation

Pending. Domain modeling is active; no new relationship decision is inferred from the invocation.

## Related follow-ups and work

Issue: https://github.com/codeonym-org/medora/issues/5.

[Initial domain model](../../../docs/domain-model.md).

[Booking policy detail](../../follow-ups/20261015T155426Z-define-detailed-booking-policies/follow-up.md).
[Identity/permissions detail](../../follow-ups/20261015T155426Z-define-identity-permissions-and-sharing/follow-up.md).

## History

- 2026-10-15T16:38:00Z — Initialized domain-modeling session and prepared the first three scenarios.
