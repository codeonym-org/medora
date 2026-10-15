---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D014",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Requests outside opening hours",
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
    ".planning/decisions/20261015T085738Z-3/D010-provisional-reservation-policy.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Review deadlines",
    "Provisional reservations",
    "Patient expectations"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D010-provisional-reservation-policy.md"
  ],
  "reply_recorded_at": "2026-10-15T14:24:28Z",
  "selected_by": "assistant",
  "selection_basis": "Explicit user delegation: q21: idk, you pick"
}
---

# Context — why ask this?

Exclusive, expiring holds are confirmed, but a patient can message at any time. The deadline must behave predictably while staff are unavailable.

## Predecessor decisions

[D010](D010-provisional-reservation-policy.md). The confirmed outcomes establish this question's prerequisites. No answer to another round 6 question is assumed.

## Question

Q21 — Requests outside opening hours: If a patient requests a slot while the practice is closed, should the staff-review deadline count only staffed working hours rather than expiring overnight?

## Recommendation and alternatives

Count staffed working hours, and always end the hold before the appointment starts. Tell the patient when staff are expected to review it; do not promise a response time the practice cannot support.

The current decision below records the reply. For Q21 the user delegated the choice; the rationale is attributed to the assistant. Earlier framing is retained as history.

## User reply — original words

Round 6 reply, recorded 2026-10-15T14:24:28Z; original message timestamp unavailable:

> q21: idk, you pick

## Interpretation

The user explicitly delegates the review-clock choice to the assistant. The following policy is an assistant selection under that delegation, not a verbatim user choice.

## Decision and rationale

Selected under delegation: count the configured review budget only during staffed working hours, cap the hold at a practice-configured cutoff before the appointment starts, and expire at the earlier limit. Release the slot and notify the patient on expiry. State expected review timing honestly. Avoid offering a reservable slot if the practice cannot review it before its cutoff.

## Consequences and affected components

Selected under delegation: count the configured review budget only during staffed working hours, cap the hold at a practice-configured cutoff before the appointment starts, and expire at the earlier limit. Release the slot and notify the patient on expiry. State expected review timing honestly. Avoid offering a reservable slot if the practice cannot review it before its cutoff. The rationale is the assistant's: avoid overnight expiry caused solely by closed hours while preventing a pending reservation from surviving until/after the appointment. Exact numerical budgets, cutoff buffers and exceptional review coverage are practice settings; no default duration is invented.

## Assumptions, evidence, and open questions

The rationale is the assistant's: avoid overnight expiry caused solely by closed hours while preventing a pending reservation from surviving until/after the appointment. Exact numerical budgets, cutoff buffers and exceptional review coverage are practice settings; no default duration is invented.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T13:52:30Z — Assistant prepared the round 6 question from confirmed prerequisites.

- 2026-10-15T14:24:28Z — Saved round 6 reply and current decision. Prior interpretation: Pending. Prior decision: Pending.
