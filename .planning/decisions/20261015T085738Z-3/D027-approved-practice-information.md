---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D027",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Questions beyond appointments",
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
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Practice information",
    "Patient questions",
    "Staff handoff"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T14:52:33Z"
}
---

# Context — why ask this?

The user described appointment questions and other matters in WhatsApp. The safe and useful initial practical-information scope should be explicit, with an authoritative practice source.

## Predecessor decisions

[D006](D006-booking-entry.md); [D023](D023-handoff-staff-assignment.md). Accepted outcomes provide the prerequisites; no other round 9 answer is assumed.

## Question

Q34 — Questions beyond appointments: Should the agent answer practical questions such as opening hours, address, consultation fees and practice-approved preparation instructions, using information maintained by the practice?

## Recommendation and alternatives

Yes. Answer from approved practice information; if it is missing or uncertain, ask the configured staff member. Keep the existing boundaries against diagnosis or prescribing.

The user accepted the current choice in the recorded reply. Details not supplied remain explicitly open.

## User reply — original words

Round 9 reply, recorded 2026-10-15T14:52:33Z; original message timestamp unavailable:

> q34: yes, good idea so they avoid embarassement!

## Interpretation

The user accepts practical practice-information answers and explicitly identifies reduced embarrassment as a benefit. This supports discreet, approachable answers to questions such as fees and preparation. No actual patient-study finding is claimed; this rationale comes from the product owner.

## Decision and rationale

Confirmed: answer practical questions from information maintained/approved by the practice; route missing or uncertain information to configured staff. The user's stated reason is helping patients avoid embarrassment.

## Consequences and affected components

Confirmed: answer practical questions from information maintained/approved by the practice; route missing or uncertain information to configured staff. The user's stated reason is helping patients avoid embarrassment. Practice information ownership, approval/update flow, missing/outdated information handling and the exact set of launch questions remain to be defined. Clinical diagnosis/prescribing boundaries remain unchanged.

## Assumptions, evidence, and open questions

Practice information ownership, approval/update flow, missing/outdated information handling and the exact set of launch questions remain to be defined. Clinical diagnosis/prescribing boundaries remain unchanged.

## Extra notes and follow-ups

The wider feature register remains intact. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:45:47Z — Prepared the round 9 question from confirmed prerequisites.

- 2026-10-15T14:52:33Z — Saved round 9 reply and confirmed the choice. Prior interpretation: Pending. Prior decision: Pending.
