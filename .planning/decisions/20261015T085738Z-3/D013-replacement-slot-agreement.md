---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D013",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "A different appointment time",
  "status": "confirmed",
  "round": 5,
  "created_at": "2026-10-15T13:46:49Z",
  "updated_at": "2026-10-15T13:52:30Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Rescheduling",
    "Patient agreement",
    "Appointment status"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md"
  ],
  "reply_recorded_at": "2026-10-15T13:52:30Z"
}
---

# Context — why ask this?

The user requires notifications for staff schedule changes. Notification alone does not establish whether the patient agreed to a replacement time.

## Predecessor decisions

[D009](D009-routine-booking-authority.md). Their confirmed outcomes provide the prerequisites; no answer to another round 5 question is assumed.

## Question

Q20 — A different appointment time: If staff proposes a different time—or changes an already confirmed appointment—should Medora ask the patient to accept the replacement before treating that new time as agreed?

## Recommendation and alternatives

Yes. Explain the change, propose the new time, and obtain the patient's agreement. Notify them clearly if the original appointment has been cancelled; do not imply a replacement is accepted merely because a message was sent.

The user accepted this recommendation in the recorded reply, with the cancellation clarification recorded for Q20.

## User reply — original words

Round 5 reply, recorded 2026-10-15T13:52:30Z; original message timestamp unavailable:

> q20: yeah, and patient is free to cancel if the time does not fit his schedule (work, school etc ..)

## Interpretation

The user accepts asking the patient to agree to a replacement appointment time and explicitly adds that the patient may cancel if it conflicts with their work, school, or other schedule. This applies to the discussed staff-initiated schedule-change situation; it does not define a monetary cancellation-fee policy or every self-initiated cancellation rule.

## Decision and rationale

Confirmed: a replacement time requires patient agreement. If it does not fit, the patient may decline and cancel rather than being forced into the replacement. Communicate changes/cancellation honestly and only after successful operations.

## Consequences and affected components

Confirmed: a replacement time requires patient agreement. If it does not fit, the patient may decline and cancel rather than being forced into the replacement. Communicate changes/cancellation honestly and only after successful operations. Replacement-offer expiry, alternate-slot selection, patient cancellation identity checks, and ordinary cancellation-policy details remain open. Do not interpret freedom to cancel as a settled financial policy.

## Assumptions, evidence, and open questions

Replacement-offer expiry, alternate-slot selection, patient cancellation identity checks, and ordinary cancellation-policy details remain open. Do not interpret freedom to cancel as a settled financial policy.

## Extra notes and follow-ups

No unrelated follow-up captured for this question.

## History

- 2026-10-15T13:46:49Z — Assistant prepared round 5 question from confirmed prerequisites.

- 2026-10-15T13:52:30Z — Recorded round 5 reply and confirmed the choice. Prior interpretation: Pending. Prior decision: Pending.
