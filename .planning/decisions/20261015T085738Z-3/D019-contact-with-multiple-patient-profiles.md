---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D019",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Returning patients",
  "status": "confirmed",
  "round": 7,
  "created_at": "2026-10-15T14:24:28Z",
  "updated_at": "2026-10-15T14:35:28Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Communication contacts",
    "Patient profiles",
    "Returning-patient booking"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md"
  ],
  "reply_recorded_at": "2026-10-15T14:35:28Z"
}
---

# Context — why ask this?

Booking for another person and a distinct communication contact are confirmed. A household contact may use the same line for multiple patients; profiles and appointment histories must not be merged by phone number.

## Predecessor decisions

[D007](D007-basic-patient-profile.md); [D016](D016-booking-for-someone-else.md). Only their accepted requirements are prerequisites; unresolved details and other round 7 answers are not assumed.

## Question

Q26 — Returning patients: Should Medora reuse details from an already verified contact-patient relationship, asking who this booking is for, or collect identity details again on every booking?

## Recommendation and alternatives

Reuse known details for verified relationships and confirm which person the appointment is for. Clarify or seek staff help when matching or authorization is uncertain, and reverify when needed for sensitive access or changes. The exact verification method remains to be defined.

The user reply and current decision are recorded below; earlier recommendation wording is historical and is not automatically accepted.

## User reply — original words

Round 7 reply, recorded 2026-10-15T14:35:28Z; original message timestamp unavailable:

> q26: ok

## Interpretation

The user accepts reuse of known details for verified contact-patient relationships, while confirming the intended patient and rechecking uncertain matching or sensitive access/changes.

## Decision and rationale

Confirmed: returning users do not repeat all known identity details on each booking; reuse verified relationships and clarify who the booking is for.

## Consequences and affected components

Confirmed: returning users do not repeat all known identity details on each booking; reuse verified relationships and clarify who the booking is for. Exact verification, re-verification triggers, ambiguous matches and corrections remain open. An arbitrary phone-number match is not sufficient.

## Assumptions, evidence, and open questions

Exact verification, re-verification triggers, ambiguous matches and corrections remain open. An arbitrary phone-number match is not sufficient.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:24:28Z — Prepared the round 7 question from accepted prerequisites.

- 2026-10-15T14:35:28Z — Saved round 7 reply; status confirmed. Prior interpretation: Pending. Prior decision: Pending.
