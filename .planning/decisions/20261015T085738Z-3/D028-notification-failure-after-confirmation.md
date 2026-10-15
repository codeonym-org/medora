---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D028",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "A confirmation message fails",
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
  ]
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

This is an assistant recommendation pending the user's choice.

## User reply — original words

Pending. Prepared for round 9.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Appointment state, Notification delivery, Staff attention queue. The answer will define the corresponding first-increment workflow.

## Assumptions, evidence, and open questions

No external integration, practice-specific factual answer, notification delivery guarantee or identity-verification method is selected or asserted. Technical stack choices remain excluded.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.
