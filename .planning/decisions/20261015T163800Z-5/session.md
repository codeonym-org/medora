---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5",
  "title": "Practice identity, communication identity and appointment lifecycle",
  "status": "active",
  "session_kind": "domain-modeling",
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-16T10:18:23Z",
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
- D001 accepted staff account versus membership → D006 receptionist coverage within a practice.
- D002 accepted contact versus shared address → exact verification and representative-access rules still open in the identity follow-up.
- D003 accepted request survival after hold expiry → D004 active-hold limit per request.
- Confirmed foundation retains the original during rescheduling → D005 appointment continuity after an approved move.
- Round 2 questions are independent; do not infer one answer from another.

## Decision index and rounds

| ID / link | Round | Question | Predecessors | Status | Outcome |
| --- | --- | --- | --- | --- | --- |
| [D000](D000-modeling-scope.md) | 0 | Scope and confirmed foundations | Previous session | confirmed | Stack-neutral modeling |
| [D001](D001-staff-identity-and-membership.md) | 1 | Staff accounts and memberships | Linked earlier decisions | confirmed | One account, independent practice memberships and role combinations |
| [D002](D002-shared-contact-point.md) | 1 | A shared patient-side number | Linked earlier decisions | confirmed | Separate people may share a Contact Point |
| [D003](D003-request-after-reservation-expiry.md) | 1 | Request versus expired reservation | Linked earlier decisions | confirmed | Request stays open after the reservation expires |
| [D004](D004-one-active-reservation-per-request.md) | 2 | One active reservation per request | Linked settled decisions | unanswered | Pending |
| [D005](D005-appointment-continuity-on-rescheduling.md) | 2 | Appointment continuity on rescheduling | Linked settled decisions | unanswered | Pending |
| [D006](D006-receptionist-doctor-assignment-scope.md) | 2 | Receptionist doctor assignment scope | Linked settled decisions | unanswered | Pending |

## Current frontier

Round 1 is recorded and accepted through the joint reply "ok, next". Round 2 tests D004 one active hold per request, D005 appointment continuity on rescheduling and D006 receptionist doctor coverage. These independent scenarios have settled prerequisites; all three replies are pending.

## Unresolved or deferred branches

Round 2 relationships are proposals only. Global patient identity, exact verification and permission matrices, duplicate-request handling, shared-patient profile access, request inactivity/closure policy and numerical booking settings remain unresolved in the existing follow-ups.

## Shared understanding

One Staff Account may have independent Practice Memberships with multiple roles. Communication Contacts may share a Contact Point without the address proving identity or authority. Expiry releases a Reservation but leaves its Appointment Request open needing another slot. Definitions are updated in the glossary; the complete domain model is not yet confirmed.

## Final user confirmation

Pending for the complete session. The user accepted the first three recommendations with "ok, next"; this is not confirmation of unanswered later scenarios or authorization to implement their proposals.

## Related follow-ups and work

Issue: https://github.com/codeonym-org/medora/issues/5.

Draft PR: https://github.com/codeonym-org/medora/pull/6.

[Initial domain model](../../../docs/domain-model.md).

[Booking policy detail](../../follow-ups/20261015T155426Z-define-detailed-booking-policies/follow-up.md).
[Identity/permissions detail](../../follow-ups/20261015T155426Z-define-identity-permissions-and-sharing/follow-up.md).

## History

- 2026-10-15T16:38:00Z — Initialized domain-modeling session and prepared the first three scenarios.

- 2026-10-16T10:18:23Z — Recorded joint acceptance of D001–D003, updated resolved vocabulary and prepared independent round 2 scenarios D004–D006.
