---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D016",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Booking for someone else",
  "status": "confirmed",
  "round": 6,
  "created_at": "2026-10-15T13:52:30Z",
  "updated_at": "2026-10-15T14:24:28Z",
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
  ],
  "reply_recorded_at": "2026-10-15T14:24:28Z"
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

The current decision below records the reply. For Q21 the user delegated the choice; the rationale is attributed to the assistant. Earlier framing is retained as history.

## User reply — original words

Round 6 reply, recorded 2026-10-15T14:24:28Z; original message timestamp unavailable:

> q23: yeah its possible and the line holder is the communication channel

## Interpretation

The user confirms booking for someone else. The holder/sender of the WhatsApp line is the communication contact, which can be different from the patient. A contact can therefore communicate about bookings for another person. This does not automatically authorize that contact to view every existing patient record.

## Decision and rationale

Confirmed: support booking on behalf of another person and keep the communication contact separate from the patient profile. Deliver the booking conversation through the contact's line.

## Consequences and affected components

Confirmed: support booking on behalf of another person and keep the communication contact separate from the patient profile. Deliver the booking conversation through the contact's line. Returning-patient matching, multiple patients per contact, representative authorization, corrections, and what existing information can be disclosed remain to be defined. A phone number is a communication endpoint, not by itself proof of patient identity or guardianship.

## Assumptions, evidence, and open questions

Returning-patient matching, multiple patients per contact, representative authorization, corrections, and what existing information can be disclosed remain to be defined. A phone number is a communication endpoint, not by itself proof of patient identity or guardianship.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T13:52:30Z — Assistant prepared the round 6 question from confirmed prerequisites.

- 2026-10-15T14:24:28Z — Saved round 6 reply and current decision. Prior interpretation: Pending. Prior decision: Pending.
