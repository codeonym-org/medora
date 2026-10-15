---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D017",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Intake without blocking booking",
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
  ]
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

This is a recommendation, not an accepted choice. Alternatives remain open until the user replies.

## User reply — original words

Pending. Prepared for round 6.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Affected areas: WhatsApp booking, Patient intake, Staff preparation. Product detail depends on the user's choice.

## Assumptions, evidence, and open questions

No review duration, routing convention, caregiver permission, or required intake field is silently selected. Technical stack choices remain excluded.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T13:52:30Z — Assistant prepared the round 6 question from confirmed prerequisites.
