---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D029",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Access to existing patient information",
  "status": "confirmed",
  "round": 9,
  "created_at": "2026-10-15T14:45:47Z",
  "updated_at": "2026-10-15T14:52:33Z",
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
  ],
  "reply_recorded_at": "2026-10-15T14:52:33Z"
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

The user accepted the current choice in the recorded reply. Details not supplied remain explicitly open.

## User reply — original words

Round 9 reply, recorded 2026-10-15T14:52:33Z; original message timestamp unavailable:

> q36: ok

## Interpretation

The user accepts staff verification of an uncertain/new contact-patient relationship before revealing existing appointment information or permitting changes to an existing booking. A new request can still enter review without disclosing old records.

## Decision and rationale

Confirmed: existing private information and booking changes require the approved verification/authorization check; staff verify unverified contact-patient relationships. New appointment requests may be collected for staff review.

## Consequences and affected components

Confirmed: existing private information and booking changes require the approved verification/authorization check; staff verify unverified contact-patient relationships. New appointment requests may be collected for staff review. Exact evidence/checks, caregiver authorization, verification recording, account/number changes, staff workflow and re-verification triggers remain detailed product decisions.

## Assumptions, evidence, and open questions

Exact evidence/checks, caregiver authorization, verification recording, account/number changes, staff workflow and re-verification triggers remain detailed product decisions.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.

- 2026-10-15T14:52:33Z — Saved round 9 reply and confirmed the choice. Prior interpretation: Pending. Prior decision: Pending.
