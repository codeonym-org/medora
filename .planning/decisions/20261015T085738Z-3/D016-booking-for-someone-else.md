---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D016",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Booking for someone else",
  "status": "unanswered",
  "round": 6,
  "created_at": "2026-10-15T13:52:30Z",
  "updated_at": "2026-10-15T13:52:30Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Patient identity",
    "Profile matching",
    "Caregiver booking"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md"
  ]
}
---

# Context — why ask this?

The agreed administrative profile needs to identify the patient. The WhatsApp sender may be a parent or caregiver rather than that patient, so phone-based matching cannot be silently assumed.

## Predecessor decisions

[D006](D006-booking-entry.md); [D007](D007-basic-patient-profile.md). The confirmed outcomes establish this question's prerequisites. No answer to another round 6 question is assumed.

## Question

Q23 — Booking for someone else: Should the first version let a parent or caregiver book for someone else using their own WhatsApp number?

## Recommendation and alternatives

Yes: distinguish the person chatting from the patient being booked. Ask who the appointment is for, and verify authorization before revealing an existing patient's information; a matching phone number alone is insufficient.

This is a recommendation, not an accepted choice. Alternatives remain open until the user replies.

## User reply — original words

Pending. Prepared for round 6.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Affected areas: Patient identity, Profile matching, Caregiver booking. Product detail depends on the user's choice.

## Assumptions, evidence, and open questions

No review duration, routing convention, caregiver permission, or required intake field is silently selected. Technical stack choices remain excluded.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T13:52:30Z — Assistant prepared the round 6 question from confirmed prerequisites.
