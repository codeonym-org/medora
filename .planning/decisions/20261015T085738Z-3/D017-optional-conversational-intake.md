---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D017",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Intake without blocking booking",
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
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "WhatsApp booking",
    "Patient intake",
    "Staff preparation"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md"
  ],
  "reply_recorded_at": "2026-10-15T14:24:28Z"
}
---

# Context — why ask this?

Basic appointment-specific intake is confirmed, but its sequence and effect on booking are not. The conversational experience should have explicit required and optional information boundaries.

## Predecessor decisions

[D007](D007-basic-patient-profile.md); [D009](D009-routine-booking-authority.md). The confirmed outcomes establish this question's prerequisites. No answer to another round 6 question is assumed.

## Question

Q24 — Intake without blocking booking: Should Medora reserve the slot once it has the minimum booking information, then collect the short intake conversationally, allowing nonessential questions to be skipped?

## Recommendation and alternatives

Yes. Keep booking easy, collect only relevant context, and show staff what is missing. Unanswered optional intake should not by itself prevent staff from confirming.

The current decision below records the reply. For Q21 the user delegated the choice; the rationale is attributed to the assistant. Earlier framing is retained as history.

## User reply — original words

Round 6 reply, recorded 2026-10-15T14:24:28Z; original message timestamp unavailable:

> q24: ok

## Interpretation

The user accepts reserving once the minimum booking information is available, then gathering short relevant intake conversationally. Nonessential questions can be skipped, and missing optional intake alone does not block staff confirmation.

## Decision and rationale

Confirmed: minimum booking data first, provisional reservation next, then brief conversational intake with optional nonessential questions and visible missing-information status for staff.

## Consequences and affected components

Confirmed: minimum booking data first, provisional reservation next, then brief conversational intake with optional nonessential questions and visible missing-information status for staff. Exact required booking fields, appointment-specific approved questions, and when staff sees incomplete intake remain product details. Skipping optional intake is not evidence that there are no concerns; existing safety/escalation boundaries remain in force.

## Assumptions, evidence, and open questions

Exact required booking fields, appointment-specific approved questions, and when staff sees incomplete intake remain product details. Skipping optional intake is not evidence that there are no concerns; existing safety/escalation boundaries remain in force.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T13:52:30Z — Assistant prepared the round 6 question from confirmed prerequisites.

- 2026-10-15T14:24:28Z — Saved round 6 reply and current decision. Prior interpretation: Pending. Prior decision: Pending.
