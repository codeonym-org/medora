---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D028",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "A confirmation message fails",
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
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Appointment state",
    "Notification delivery",
    "Staff attention queue"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T14:52:33Z"
}
---

# Context — why ask this?

Successful appointment operations and successful patient notification are different outcomes. The user requires notifications but has not chosen what a delivery failure does to the booking.

## Predecessor decisions

[D009](D009-routine-booking-authority.md); [D013](D013-replacement-slot-agreement.md); [D015](D015-practice-and-doctor-routing.md). Accepted outcomes provide the prerequisites; no other round 9 answer is assumed.

## Question

Q35 — A confirmation message fails: If staff confirms an appointment but the WhatsApp notification cannot be delivered, should the appointment stay confirmed while staff see the delivery failure and Medora retries?

## Recommendation and alternatives

Yes. Track appointment status and message delivery separately. Alert staff, retry according to policy, and do not silently cancel or claim the patient was informed.

The user accepted the current choice in the recorded reply. Details not supplied remain explicitly open.

## User reply — original words

Round 9 reply, recorded 2026-10-15T14:52:33Z; original message timestamp unavailable:

> q35: ok

## Interpretation

The user accepts keeping the successfully confirmed appointment while tracking a failed WhatsApp notification separately, notifying staff and retrying under policy. Failure to deliver does not silently undo the booking.

## Decision and rationale

Confirmed: appointment state and notification-delivery state are separate; preserve the confirmed booking, surface failed delivery to staff, and retry according to practice/system policy without claiming the patient was informed.

## Consequences and affected components

Confirmed: appointment state and notification-delivery state are separate; preserve the confirmed booking, surface failed delivery to staff, and retry according to practice/system policy without claiming the patient was informed. Retry timing, limits, escalation, alternative contact methods and what staff do if delivery never succeeds remain open. No guaranteed delivery or automatic alternate-channel consent is inferred.

## Assumptions, evidence, and open questions

Retry timing, limits, escalation, alternative contact methods and what staff do if delivery never succeeds remain open. No guaranteed delivery or automatic alternate-channel consent is inferred.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.

- 2026-10-15T14:52:33Z — Saved round 9 reply and confirmed the choice. Prior interpretation: Pending. Prior decision: Pending.
