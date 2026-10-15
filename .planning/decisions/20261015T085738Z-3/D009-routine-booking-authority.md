---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D009",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Routine booking approval",
  "status": "confirmed",
  "round": 4,
  "created_at": "2026-10-15T12:13:49Z",
  "updated_at": "2026-10-15T13:46:49Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Booking confirmations",
    "Practice policies",
    "Staff review"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T13:46:49Z"
}
---

# Context — why ask this?

The product vision requires authorized scheduling and truthful confirmations, but the default routine-booking approval policy is not defined. The question is independent of which channel receives the request.

## Predecessor decisions

[D001](D001-first-practice.md); [D002](D002-anchor-problem.md) establish the accepted practice model and basic-booking scope.

## Question

Q16 — Routine booking approval: When a patient selects a valid available slot, should Medora confirm automatically within the practice rules, require staff approval for every request, or let each practice choose?

## Recommendation and alternatives

Let each practice choose. Automatic confirmation applies only to eligible routine bookings; requests outside its configured rules go to staff.

The alternatives remain proposals until the user replies.

## User reply — original words



Round 4 reply, recorded 2026-10-15T13:46:49Z; original message timestamp unavailable:

> q16: id say patient book an appointement, agent reserve a slot, when staff confirms, agent notifies the user, if staff changes schedule / refuse etc ... patient get notified as well

## Interpretation

The agent creates a provisional reservation from the patient conversation. Staff review determines confirmation, rejection, or scheduling changes; the agent informs the patient of those outcomes. A provisional slot is not a confirmed appointment. The user chooses a staff-review workflow, not the assistant's proposed configurable auto-confirmation default. Staff changes require notification; this alone does not settle patient acceptance of a replacement time.

## Decision and rationale

Confirmed: request → agent reserves slot pending staff review → staff confirms/rejects/changes → agent notifies the patient of the outcome. Patient-facing status must distinguish reserved/awaiting confirmation from confirmed, and communicate actual successful outcomes.

## Consequences and affected components

Scheduling needs provisional reservation and staff-review states. Determine hold exclusivity/expiry, approver roles, patient agreement to replacement times, and notification failure behavior. Never label the appointment confirmed before staff approval and successful persistence.

## Assumptions, evidence, and open questions

Reservation exclusivity, expiry, review deadlines, who can approve, review conflicts, handling replacement slots, and failed notification behavior are not yet chosen. Urgent medical concerns retain the established separate human escalation/safety boundaries.

## Extra notes and follow-ups

Related questions are continuing within this product session. No unrelated follow-up was introduced by this reply.

## History

- 2026-10-15T12:13:49Z — Assistant prepared round 4 question from accepted prerequisites.

- 2026-10-15T13:46:49Z — Saved round 4 reply and confirmed the explicit choice.
  - Prior interpretation: Pending.
  - Prior decision summary: Pending.
