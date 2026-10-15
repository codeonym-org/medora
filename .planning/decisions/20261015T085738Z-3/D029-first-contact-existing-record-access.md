---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D029",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Access to existing patient information",
  "status": "unanswered",
  "round": 9,
  "created_at": "2026-10-15T14:45:47Z",
  "updated_at": "2026-10-15T14:45:47Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D019-contact-with-multiple-patient-profiles.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Patient identity",
    "Representative access",
    "Appointment queries and changes"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D019-contact-with-multiple-patient-profiles.md",
    "docs/product-vision.md"
  ]
}
---

# Context — why ask this?

The user accepts caregiver bookings and reuse of verified relationships. The first-time/uncertain relationship boundary must prevent someone from gaining records merely by supplying a name or phone number.

## Predecessor decisions

[D016](D016-booking-for-someone-else.md); [D019](D019-contact-with-multiple-patient-profiles.md). Accepted outcomes provide the prerequisites; no other round 9 answer is assumed.

## Question

Q36 — Access to existing patient information: For an unverified contact asking about an existing patient, should staff verify the contact-patient relationship before Medora reveals past appointments or permits changes to an existing booking?

## Recommendation and alternatives

Yes. A new appointment request may still be taken for staff review, but existing private information and booking changes require the approved identity/authorization check.

This is an assistant recommendation pending the user's choice.

## User reply — original words

Pending. Prepared for round 9.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Patient identity, Representative access, Appointment queries and changes. The answer will define the corresponding first-increment workflow.

## Assumptions, evidence, and open questions

No external integration, practice-specific factual answer, notification delivery guarantee or identity-verification method is selected or asserted. Technical stack choices remain excluded.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.
